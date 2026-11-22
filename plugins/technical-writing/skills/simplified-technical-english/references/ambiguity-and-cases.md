# Ambiguity checks and worked cases

IBM EasyEnglish detects grammatical structures that admit more than one interpretation. A checker can expose the readings. The source or a human decision determines which one is correct. Use this method without requiring an IBM tool. The examples below are original. [IBM research and source paper](sources.md)

## Select an ambiguity that changes behavior

For an ordinary ticket, start with the action a reader would take. If the sentence has one clear reading in project context, keep it. A passive construction, a pronoun or a long label alone does not require a finding. Use one of the following questions when two plausible interpretations change a role, condition, action or result. The table supplies targeted checks and does not add a mandatory review stage.

| Feature | Try both readings | Correction once the source selects a reading |
|---|---|---|
| Participle or trailing modifier | “The operator identified the device using the diagnostic link.” Did the operator use the link to identify a device? Or did the operator identify the particular device that used the link? | “The operator used the diagnostic link to identify the device.” For the other reading, write “The operator identified the device that used the diagnostic link.” |
| Scope of a shared word | “Archive signed reports and receipts.” Must the receipts be signed too? | For signed reports and signed receipts, name both groups. For all receipts, write “Archive all receipts. Archive each signed report.” |
| Mixed conditions | “Allow export for reviewers and owners or administrators.” Does the user need multiple roles? Can any one of the three roles export? | Use a decision table or enumerate the permitted combinations only after confirming the rule. |
| Two passive verbs | “The records were reported deleted by the operator.” Did the operator delete the records, report their deletion, or do both? | Assign each supported action to its actor. If only the reporting actor is known, leave the deleting actor unknown. |
| Pronoun or demonstrative | “When the worker calls the scheduler, it resets the timer.” Which component resets it? | Use the component name. If the source does not specify it, ask who resets the timer. |
| Stacked nouns | Does “service certificate renewal notice” concern renewal of a service certificate, or a notice from the renewal service? | Name the issuer, the renewed object, and the recipient where the source supplies them. |
| Negative or qualifier | In “Only operators may retry,” does “only” restrict the role or the operation? Would moving the word change that restriction? | Keep “only” beside the restricted term. Preserve the permission and the exclusion of all other roles. |

When two readings lead to different actions, report them as alternatives. An edit that selects one without evidence gives the reader a new requirement.

## Worked cases

The examples below use their own source facts. In an ordinary edit, use cases to check the meaning of changed passages. Report a case when it exposes a difference or the reader requests evidence. A separate test plan or reviewer is optional unless the project requires one.

### Ordinary ticket with an exact label

Source: “Following the reopening of a saved report, the continued display of its previously selected filters in **Report filter selection history** is required.” Ticket text: “When a user reopens a saved report, **Report filter selection history** shows the filters saved with that report.” The long label still identifies the correct control. The reader can match the label to the control and check whether the reopened report has the saved filters.

### Permission, time, and exception

Source: “Only a reviewer may retry a FAILED export at least 30 s after cancellation, unless the account is locked.”

Adapted text: “Only a reviewer may retry a FAILED export. The account must be unlocked, and at least 30 s must have elapsed since cancellation.”

A reviewer with an unlocked account at exactly 30 s has permission. At 29 s the reviewer cannot retry. A locked account or a different role cannot retry even at 31 s. The rule does not require an automatic retry. If the source simply said “after 30 s” and exact equality mattered, query the boundary.

### A protocol that explicitly adopts BCP 14

Source: “For BCP 14 purposes, a server MUST return the original ID on a repeated request. The client MAY retry.”

Reject an edit that says “The client retries and the server can return the ID.” The edit changes permission to behavior and weakens an obligation. A supported edit is “The client MAY retry. If the request is a repeat, the server MUST return the original ID.” Check the ID from the first request against the ID in the response to a repeat. If this change must define repeat detection and the source omits that rule, ask what identifies a repeat. The source does not establish a response for a new request.

### One transaction

Source: “The writer stores the item and its receipt in one transaction. If either write fails, neither change remains.”

An edit with two independent numbered steps can allow the item to remain after the receipt fails. Correct it to “In one transaction, the writer stores the item and its receipt. If either write fails, neither change remains.” Test success, a failure on the first write and a failure on the second. Both records are present on success. Neither remains on either failure.

### Unresolved reference

Source: “The parser calls the validator after it reads the manifest.” Replacing *it* with *the parser* chooses an actor without evidence. In check mode, report the two actors. Ask “Which component reads the manifest before the call?” In rewrite mode, preserve the uncertainty until the source resolves it.

### A test case that narrows a requirement

Source: “For any other error, show the usual message.” A test that says “For an error with a different code” silently requires a code. An error with no code still falls under the source rule. Preserve the scope in the requirement and in its acceptance criteria.

### What a check reports

For a substantive finding in an ordinary draft, quote the relevant words, explain the possible change in behavior and suggest a supported correction or question. For a formal STE review, identify the applicable dictionary entry or rule. Record the issue, scope, checked exceptions and missing material. A count of short sentences alone cannot verify agreement with the source or official word approval.
