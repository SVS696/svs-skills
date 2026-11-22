---
name: simplified-technical-english
description: Rewrite or check English technical documentation, requirements, procedures, APIs, and skill instructions. Select this skill when the requested output is English, including a technical translation into English. Apply ASD-STE100 and IBM EasyEnglish. Use the specified edition and dictionary when the user requests a formal STE check.
---

# Simplified Technical English

Use the source text, the intended reader, and any supplied contract or glossary. The files in this folder support an offline edit. For a translation, use the source in its original language to check the English result.

## Choose the result

- **Rewrite.** Return the new text in the requested format. Preserve its structure, identifiers, quotations, code, and links. Edit a file when the user asks for a file edit.
- **Check.** Leave the input unchanged. Give the location, the rule or source, the effect on the reader, and the smallest supported correction. If the user supplies only a draft, report what you can establish from that draft. A comparison of meaning requires the source.
- **Rewrite and check.** Return the revised text, then report open decisions or material differences. Give a clean result when the text passes the stated checks.
- **Formal check.** Identify the issue, the scope, the project terminology, and the exact document version. Check each applicable rule in Part 1 and each applicable word in Part 2 of the full standard. Use the local original if available. If a required item is missing, name it and limit the conclusion to the checks you completed. [Sources and local originals](references/sources.md)

## Make the edit

1. From the source, identify the actor, action, object, trigger, authority and result. Mark limits, exceptions, exact labels and the reason for the rule. Keep any unresolved issue open.
2. Classify each passage as a procedure, description, safety instruction, or project requirement. Apply the relevant sections of the [writing guide](references/writing.md). Use the [word guide](references/vocabulary.md) to check meaning, part of speech, word form and technical terms.
3. For a requirement, interface, technical decision or skill, apply the relevant [document pattern](references/document-patterns.md). Draft directly in technical English for the intended reader.
4. Use the [ambiguity checks](references/ambiguity-and-cases.md) where a reader might derive two behaviors. Resolve each ambiguity from the source. If the evidence permits both readings, show both and ask the smallest question that separates them.
5. Compare the result with the source. Try one normal case and one meaningful boundary or exception. Record a difference if the actor, allowed action, ordering, data, time, scope, or output changes. Preserve any unknowns. A readable sentence can still change a requirement.
