# svs-skills

Личный маркетплейс Claude Code скиллов от [@SVS696](https://github.com/SVS696).

## Установка

```text
/plugin marketplace add SVS696/svs-skills
```

Затем поставь нужные плагины:

```text
/plugin install simplicity@svs
/plugin install vidscribe@svs
/plugin install cli-agents@svs
/plugin install singularity-app@svs
/plugin install zenmoney@svs
/plugin install humanizer@svs
```

Или вне сессии:

```bash
claude plugin marketplace add SVS696/svs-skills
claude plugin install simplicity@svs
```

## Что внутри

| Плагин | Скиллы | Назначение |
|--------|--------|------------|
| **simplicity** | `/simplicity:simplicity-spec`, `/simplicity:simplicity-code` | Проходы на простоту — ловят переусложнение в ТЗ/архитектуре/инфре и в коде до того, как результат уйдёт пользователю |
| **vidscribe** | `/vidscribe:vidscribe` | Локальная транскрипция видео и встреч (faster-whisper + pyannote + CLI-коррекция). Скилл = дока к CLI; сам CLI ставится из [SVS696/vidscribe](https://github.com/SVS696/vidscribe) |
| **cli-agents** | `/cli-agents:cli-agents` | Внешние Claude и Codex CLI для изолированного review, дискуссий и multi-model council. Read-only по умолчанию, есть live stream; Gemini опционален |
| **singularity-app** | `/singularity-app:singularity` | Клиент [Singularity App](https://singularity-app.com) API (задачи, проекты, привычки, kanban). Токен в `~/.config/singularity-app/config.json` |
| **zenmoney** | `/zenmoney:zenmoney` | Управление финансами через ZenMoney API. Карта инструментов поверх MCP-сервера [SVS696/zenmoney-mcp](https://github.com/SVS696/zenmoney-mcp) (ставится отдельно) |
| **humanizer** | `/humanizer:humanizer` | Убирает признаки AI-генерации из текста + русские правила R1–R9 (тире, ёлочки «», канцелярит, рунглиш). Форк [blader/humanizer](https://github.com/blader/humanizer) → [SVS696/humanizer](https://github.com/SVS696/humanizer) с русской адаптацией |

После установки скиллы вызываются явно через `/plugin:skill` или подхватываются
моделью автоматически по описанию.

## Как устроено

Маркетплейс — это `.claude-plugin/marketplace.json`, который агрегирует плагины
двумя способами:

- **Ссылкой на репозиторий** (`source: github`) — когда репозиторий сам по себе
  является плагином (`skills/<имя>/SKILL.md` в корне). Так подключены
  [`simplicity-skills`](https://github.com/SVS696/simplicity-skills),
  [`cli-agents`](https://github.com/SVS696/cli-agents),
  [`singularity-skill`](https://github.com/SVS696/singularity-skill).
- **Вендорингом** (`source: ./plugins/<имя>`) — когда «домашний» репозиторий
  лучше не трогать: либо это тяжёлый проект (Python/MCP), который незачем тянуть
  целиком (`vidscribe`, `zenmoney`), либо это форк, который надо держать чистым
  для синхронизации с апстримом (`humanizer` — форк blader/humanizer). Скилл
  копируется в `plugins/<имя>/skills/<имя>/SKILL.md`.

## Обновление

```text
/plugin marketplace update svs      # обновить каталог
/plugin update simplicity@svs       # обновить плагин
```

## Лицензия

MIT — см. [LICENSE](./LICENSE). Каждый плагин может иметь собственную лицензию в
своём репозитории.
