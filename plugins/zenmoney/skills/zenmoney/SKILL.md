---
name: zenmoney
description: "Personal finance management through ZenMoney API — accounts, transactions, budgets, reminders, analytics, and ML category suggestions. Triggers: деньги, расходы, бюджет, счета, транзакции, финансы, money, spending, budgets."
---

# ZenMoney Personal Finance Assistant

Управление личными финансами через ZenMoney API. Все инструменты возвращают JSON.

> **Требуется MCP-сервер.** Эти инструменты предоставляет MCP-сервер
> [`zenmoney-mcp`](https://github.com/SVS696/zenmoney-mcp) — он не входит в плагин,
> настраивается отдельно (один раз):
> ```bash
> git clone https://github.com/SVS696/zenmoney-mcp && cd zenmoney-mcp
> npm install && npm run build
> ```
> Затем добавь сервер в `.mcp.json` и положи `ZENMONEY_TOKEN` (получить: `npm run auth`
> или из настроек экспорта BUDGERA). После этого инструменты `get_accounts`,
> `create_transaction` и т.д. доступны Claude напрямую. Этот скилл — карта
> инструментов и правила маршрутизации поверх них.

## Tool reference

**Чтение:**
- `get_accounts` — `include_archived`
- `get_transactions` — `start_date`(req), `end_date`, `account_id`, `category_id`, `type`(expense/income/transfer), `limit`(max 500), `offset`
- `get_categories` — без аргументов
- `get_instruments` — `include_all` (валюты + курсы)
- `get_budgets` — `month`(req, yyyy-MM)
- `get_reminders` — `include_processed`, `active_only`, `limit`, `offset`, `marker_from`(yyyy-MM-dd), `marker_to`(yyyy-MM-dd), `category`(name), `type`
- `get_analytics` — `start_date`(req), `end_date`, `group_by`(category/account/merchant), `type`(expense/income/all)
- `suggest` — `payee`(req) → ML-подсказка категории
- `get_merchants` — `search`, `limit`, `offset`
- `check_auth_status` — проверка токена
- `analyze_budget_detailed` — детальный разбор: доходы vs расходы, план vs факт, календарь платежей, прогноз баланса
- `setup_budget_mode` — `mode`(balance_vs_expense / income_vs_expense)

**Запись:**
- `create_transaction` — `type`(req), `amount`(req), `account_id`(req), `to_account_id`, `category_ids`, `date`, `payee`, `comment`, `currency_id`, `income_amount`
- `update_transaction` — `id`(req), partial fields
- `delete_transaction` — `id`(req)
- `create_account` — `title`, `type`(cash/ccard/checking), `currency_id`(req), `balance`, `credit_limit`
- `create_budget` / `update_budget` / `delete_budget` — `month`(req), `category`(req, name/UUID/"ALL"), `income`, `outcome`, locks
- `create_reminder` / `update_reminder` / `delete_reminder` — `interval`(req), amount, account, dates, `generate_markers`(default 12)
- `create_reminder_marker` / `delete_reminder_marker`

## Быстрый маршрутизатор

| Задача | Tool(s) |
|---|---|
| Баланс, счета | `get_accounts()` |
| Расходы за период | `get_transactions(start_date, type="expense")` |
| Аналитика расходов | `get_analytics(start_date, group_by="category")` |
| Добавить расход/доход | `suggest(payee)` → `create_transaction(...)` |
| Перевод между счетами | `create_transaction(type="transfer", account_id, to_account_id)` |
| Бюджет на месяц | `get_budgets(month)` |
| Установить бюджет | `create_budget(month, category, outcome)` |
| Детальный анализ бюджета | `analyze_budget_detailed` |
| Напоминания / подписки | `get_reminders()` |
| Плановые платежи за период | `get_reminders(marker_from, marker_to, type="expense")` |
| Категории / валюты | `get_categories()` / `get_instruments()` |
| UUID счёта/категории по имени | `get_accounts()` / `get_categories()` |

## Smart features

- **Естественные даты:** «в этом месяце» → текущий месяц; «в январе» → 2026-01-01/31; «за 30 дней» → последние 30 дней.
- **ML-категории:** перед `create_transaction` всегда вызывай `suggest(payee)`.
- **Авто-контекст:** «Сколько потратил?» → аналитика за текущий месяц; «Баланс» → счета.

## Платёжный период

Если у пользователя не календарный месяц, а свой расчётный период (напр. 20-е →
19-е), уточни день начала и используй его для вычисления `marker_from`/`marker_to`
в `get_reminders` и `month` в бюджетах. Сервер может хранить
`billing_period_start_day` в своём config.

## Режимы get_reminders

- **Legacy** (без marker_from/to): напоминания по startDate desc — для просмотра недавних.
- **Marker** (с marker_from + marker_to): фильтр по маркерам в периоде; возвращает `markers_total_outcome/income`, `type`, `markers_count`. Рекомендуется для подсчёта плановых расходов и анализа подписок.

## Режимы бюджета (analyze_budget_detailed)

- `balance_vs_expense` — все движения денег, включая внебалансовые счета. ⚠️ Экспериментальный, может расходиться с ZenMoney.
- `income_vs_expense` — исключает лишние переводы, фокус на реальных доходах/расходах. ✅ Совпадает с ZenMoney.

Настройка: `setup_budget_mode(mode="income_vs_expense")`.

## Форматы данных

- Даты `yyyy-MM-dd`, месяцы `yyyy-MM`, UUID из `get_accounts`/`get_categories`.
- Валюта — instrument id из `get_instruments`.
- Типы транзакций: `expense`, `income`, `transfer`. Типы счетов: `cash`, `ccard`, `checking`.
- Интервалы напоминаний: `day`, `week`, `month`, `year`.
- Удаление транзакций необратимо — подтверждай перед `delete_transaction`.
