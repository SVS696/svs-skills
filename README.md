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

После установки скиллы вызываются явно через `/plugin:skill` или подхватываются
моделью автоматически по описанию.

## Как устроено

Маркетплейс — это `.claude-plugin/marketplace.json`, который агрегирует плагины
двумя способами:

- **Ссылкой на репозиторий** (`source: github`) — когда репозиторий сам по себе
  является плагином (`skills/<имя>/SKILL.md` в корне). Так подключён
  [`simplicity-skills`](https://github.com/SVS696/simplicity-skills).
- **Вендорингом** (`source: ./plugins/<имя>`) — когда скилл это лёгкая дока, а
  его «домашний» репозиторий — тяжёлый проект, который незачем тянуть целиком.
  Так подключён `vidscribe`.

## Обновление

```text
/plugin marketplace update svs      # обновить каталог
/plugin update simplicity@svs       # обновить плагин
```

## Лицензия

MIT — см. [LICENSE](./LICENSE). Каждый плагин может иметь собственную лицензию в
своём репозитории.
