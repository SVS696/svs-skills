# Patterns for project documents

Choose the pattern that fits the reader's task. These patterns extend the adapted language profile for software teams. EARS, BCP 14 and ISO/IEC/IEEE 29148 serve different purposes. A document can use one without adopting the others. [Sources](sources.md)

## System requirements and acceptance

For a requirement, retain the responsible component, trigger or current state, force of the statement, observable result and exceptions. Separate the reason from required behavior. Split independently testable obligations. Keep changes together if the source requires one atomic outcome. Check time origin, units, inclusive bounds, the scope of “each” and any time limit.

The following EARS examples use *shall* for a system obligation. Use the project's convention. Keep a permission as a permission.

| Pattern | Use it when | Example |
|---|---|---|
| Invariant | The obligation always applies in scope | The service shall retain the original request ID. |
| Event | An event starts the obligation | When the upload ends, the server shall return a receipt. |
| State | An obligation continues while a condition holds | While the account is locked, the service shall reject sign-in requests. |
| Unwanted behavior | A defined fault or unwanted input requires a response | If the signature is invalid, then the server shall reject the file. |
| Optional feature | The obligation applies to systems with a stated feature | Where batch export is available, the client shall display the batch size. |
| Combined | The source gives both a state and an event | While the account is locked, when the timer expires, the service shall record the expiry. |

For acceptance, name the initial data and state, the action, and an observable outcome. Test at least one source-defined boundary. For “less than 5 MiB,” a file of exactly 5 MiB is outside the range. Preserve the distinction between a missing outcome and an explicit rejection. An unknown response requires an open question.

## API and protocol

Retain exact verbs, paths, codes, header names, casing, nullability and literal examples. Say whether a missing field, an empty field, and an explicit `null` produce different results. For a retry, identify the key, side effects and response the contract promises. If the source specifies only one of those, keep the others open.

When the document adopts BCP 14, preserve uppercase normative keywords and their strength. An obligation and a prohibition bind the implementer. A recommendation admits justified exceptions. An option leaves a choice to the implementer. A common lowercase modal in an ordinary sentence does not acquire the BCP 14 keyword meaning merely because the contract also uses BCP 14. Do not change case inside a quotation.

## Architecture and decisions

Record the chosen option, the reason supplied by the source and its scope. Preserve observations and assumptions as distinct statements. “The measured queue reached 180 jobs” records a measurement. “The queue can grow to 1,000 jobs” needs its own evidence or explicit status as an assumption. A reason for choosing a database does not automatically become a permanent restriction on other designs.

## Procedures and skill instructions

Name the input or initial state. State who acts if the text addresses more than one role. Give the action, expected output, and condition to stop or continue. Keep an exception beside the step it changes. Use exact tool names and paths when the reader needs them.

Example procedure:

1. Read the hash from the publication receipt.
2. Compare it with the hash of the approved article.
3. If the hashes differ, report the mismatch and stop.
4. If the hashes match, record the version from the receipt.

Reading a receipt establishes only what that receipt attests. If the source also requires an independent read of the published version, retain that additional step.
