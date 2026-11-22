---
name: simplified-technical-english
description: Write, rewrite or check English analyst tickets and technical documents, including translations into English. Use the reader’s project terminology and preserve the source meaning. Also supports formal ASD-STE100 checks when requested or required by the project.
---

# Simplified Technical English

For an ordinary analyst ticket, write the change in the team's own English. Name the action, who performs it when that matters, and what a reader can observe. Keep the supplied terms, conditions, exceptions, permissions, reasons, and exact interface text. If the source leaves the actor open, keep the condition without guessing who acted. Preserve whether the change uses an existing component or introduces one. A sentence that the reader can already apply can stay as written.

**Example ticket.** Source wording: “Following selection of **Save**, the application undertakes a return to the list. Filters selected by the analyst are retained.” Ticket text: “When the analyst selects **Save**, the app returns to the list with the same filters.” This gives the tester one action and two things to observe. The ticket needs no extra sections.

## Choose the requested output

- **Write or rewrite.** Return the text in the requested language, structure, and format. Preserve code, identifiers, project template headings, link targets, UI labels and quoted messages exactly, including strings in another language. Change them if the task calls for that change. Edit a file if requested.
- **Check.** Leave the input unchanged. Report each substantive issue with its location, its effect on the reader, and a supported correction or question. With a draft alone, assess clarity. To check a change in meaning, compare with the source.
- **Rewrite and check.** Return the revised text. Add only material unresolved issues or any check results the reader requested.

## Choose the guidance that applies

1. **Everyday technical English.** For a ticket, API change, internal proposal or ordinary procedure, read for meaning. Prefer direct verbs and consistent names. Keep the project's accepted terminology, including long labels. Preserve the difference between an observed fact, a proposed change and a requirement. The [writing guide](references/writing.md) has a short everyday section. The [word guide](references/vocabulary.md) helps when a term has more than one meaning.
2. **A specific ambiguity.** If two readings would change the action or result, use the [worked cases](references/ambiguity-and-cases.md). Resolve the issue from the source, or ask a focused question. A sentence with a passive verb or a pronoun can be perfectly clear.
3. **A document convention.** Follow EARS syntax, BCP 14 keywords, a prescribed template, or a safety-message format when the request, source contract or governing project instructions call for it. Apply the convention to the passages it governs. The [document patterns](references/document-patterns.md) give examples. A ticket about an API change can use ordinary English.
4. **Formal ASD-STE100.** Use this route when the request or governing document explicitly requires compliance or an assessment against a named edition. “Simplify this” and a reference to technical English alone select the everyday route. Confirm the applicable issue and scope. For a formal assessment, check Part 1 and the vocabulary in Part 2, including applicable technical terms. Record the edition, document version and findings. If necessary material is missing, state what remains unverified. [Formal guide](references/writing.md) · [Sources and local originals](references/sources.md)

Before returning the text, compare it with the source. For changed behavior, try the normal case and any material exception or boundary the source supplies. Keep this check brief and internal unless the user asks for evidence or it reveals a problem. Use the same comparison after a readability edit. Keep a decision open only when choosing an answer would change the meaning or the reader's next action.
