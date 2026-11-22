# Patterns for project documents

Use the ticket, API note, decision or procedure that the project already expects. When an applicable contract or a user request names a convention, follow it in the part it governs. The optional extensions below show the effect of that choice. [Sources](sources.md)

## Analyst tickets and acceptance

For a requirement, retain the responsible component, trigger or current state, force of the statement, observable result and exceptions. Separate the reason from required behavior. Split independently testable obligations. Keep changes together if the source requires one atomic outcome. Check time origin, units, inclusive bounds, the scope of “each” and any time limit.

For example, “While an import is running, the dashboard shows its progress” is sufficient for a ticket with that stated change. A tester can start an import and read the dashboard. Add acceptance criteria when the reader needs them or the project requires them. Use the conditions the source provides. For “less than 5 MiB,” exactly 5 MiB is outside the allowed range. This alone does not specify an error message, a status code, or an alert.

## When the project requests EARS

Use these patterns when the project or user selects EARS for system requirements. They apply to the requirements in scope. Use ordinary prose in a surrounding ticket or explanation unless the project extends the convention there. In these EARS examples, *shall* expresses a system obligation. A permission keeps its original force.

| Pattern | Use it when | Example |
|---|---|---|
| Invariant | The obligation always applies in scope | The service shall retain the original request ID. |
| Event | An event starts the obligation | When the upload ends, the server shall return a receipt. |
| State | An obligation continues while a condition holds | While the account is locked, the service shall reject sign-in requests. |
| Unwanted behavior | A defined fault or unwanted input requires a response | If the signature is invalid, then the server shall reject the file. |
| Optional feature | The obligation applies to systems with a stated feature | Where batch export is available, the client shall display the batch size. |
| Combined | The source gives both a state and an event | While the account is locked, when the timer expires, the service shall record the expiry. |

## API changes and protocol specifications

Retain exact verbs, paths, codes, header names, casing, nullability and literal examples. Describe differences between a missing field, an empty field and an explicit `null` when the change depends on those states. For a retry, preserve the key, side effects and response specified by the contract. Raise an unspecified detail when it affects the change being described. An unrelated interface detail needs no open question.

A regular API ticket can say “If the attachment is missing, the server returns `422`” when the source specifies that result. The ticket can keep this sentence even if another service has a protocol specification.

### When the protocol adopts BCP 14

When the document adopts BCP 14, preserve uppercase normative keywords and their strength. An obligation and a prohibition bind the implementer. A recommendation admits justified exceptions. An option leaves a choice to the implementer. A common lowercase modal in an ordinary sentence does not acquire the BCP 14 keyword meaning merely because the contract also uses BCP 14. Do not change case inside a quotation.

## Architecture and decisions

For an actual design decision, record the chosen option, the reason supplied by the source and its scope. Preserve observations and assumptions as distinct statements. “The measured queue reached 180 jobs” records a measurement. “The queue can grow to 1,000 jobs” needs its own evidence or explicit status as an assumption. A reason for choosing a database does not automatically become a permanent restriction on other designs.

## Procedures and skill instructions

Write a procedure when the reader needs to perform an action. A product requirement can simply describe what the system does. For a procedure, name the input or initial state. State who acts if the text addresses more than one role. Give the action, expected output, and condition to stop or continue. Keep an exception beside the step it changes. Use exact tool names and paths when the reader needs them.

In this example, a release procedure requires a receipt check.

1. Read the hash from the publication receipt.
2. Compare it with the hash of the approved article.
3. If the hashes differ, report the mismatch and stop.
4. If the hashes match, record the version from the receipt.

Reading a receipt establishes only what that receipt attests. If the source also requires an independent read of the published version, retain that additional step.
