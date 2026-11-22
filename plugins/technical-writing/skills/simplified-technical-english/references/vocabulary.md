# Check an English word or project term

Use Part 2 of the applicable ASD edition for a formal STE decision. The official local file, its fingerprint and its page ranges are listed in [Sources and local originals](sources.md). The product contract, interface or terminology database defines project names. The working vocabulary below supplies candidate meanings for an adapted software document. A project owner can choose a different term or meaning.

## Everyday term choice

Use the term from the product, the API or the team's glossary. Preserve a button label such as **Empty queue** exactly. In an ordinary procedure, “Select **Empty queue**” tells the reader what to do. A word’s status in the ASD dictionary does not change the interface label. Consult the working glossary below only when it helps distinguish concepts in the source.

## Formal lookup in Issue 9

1. Read the whole clause. Write down the meaning and the part of speech needed here. For a verb, identify the subject and action. For a noun, identify the thing it names.
2. Open Part 2. Read the introductory key when needed, then find the headword in the alphabetical entries. Read *all* entries for that spelling. An uppercase headword identifies an approved entry. A lowercase headword directs the writer to alternatives. A match in an example or in the change history does not establish approval.
3. Match the sense and the part of speech. For a verb or adjective, confirm the form. If the listed alternative has a different meaning here, rewrite the whole clause. Preserve the action and its result. Do not replace every occurrence of a spelling across the document.
4. For a product term, record its source, meaning and grammatical role. Issue 9 calls a technical name a **technical noun**. Classify it under rule 1.5 or classify a technical verb under rule 1.12. For an unapproved general word inside a technical noun, also check rule 1.6. The same spelling used as both a technical noun and a technical verb requires independent support for both roles. Preserve exact identifiers, labels and quoted messages.
5. Record a result that a reader can verify. For a common word give the issue, headword, part of speech and page. For a technical term give its source and applicable category. Mark unresolved terms explicitly. A match in this working vocabulary establishes no official dictionary status.

**Verified example.** On physical PDF page 231 (printed page 2-1-E5), *empty* has separate adjective and verb entries. In “The queue is empty,” the adjective describes a state with no contents. In “Empty the queue,” the word directs an action. If the approved procedure removes every entry, a possible rewrite is “Remove all entries from the queue.” If the operation only hides entries from the current view, that rewrite changes the result. Consult the product operation before choosing a verb.

## Working glossary for software documents

These examples illustrate possible software meanings. Use the project’s wording and behavior. Sample numbers, roles, storage rules, responses and side effects apply only to their examples.

| Term | Part of speech | Meaning in this example | Example |
|---|---|---|---|
| acknowledgement | noun | Message that confirms receipt | The acknowledgement contains the request ID. Receipt does not prove completion. |
| archive | verb | Move an item to the project's retained history | The service archives the report for seven years. |
| audit log | noun | History of actions that the system records for review | The audit log identifies the account that changed the limit. |
| available | adjective | Accessible for the stated use at the time of the check | The export is available for download. |
| cancel | verb | End the specified request as permitted by its current state | Operators can cancel a queued request. |
| component | noun | Named part of the system with a defined responsibility | The parser is the component that reads the manifest. |
| confirm | verb | Provide the confirmation that the source requires | The approver confirms the change in the approval form. |
| default | noun | Value applied under a stated condition | The default for a missing limit is 20. |
| delete | verb | Remove the named object at the specified level | The user deletes the draft. The audit log keeps its identifier. |
| duration | noun | Elapsed time between named events | The job duration starts when the worker accepts the job. |
| enabled | adjective | Configured to permit a feature | Export is enabled for this account. |
| endpoint | noun | Network address or API operation identified by the project's contract | The client calls the status endpoint. |
| event | noun | Occurrence at a point in time | The service records an event when the job ends. |
| failure | noun | Inability to complete a specified operation | A write failure prevents publication of the report. |
| identifier | noun | Value that distinguishes an item within a specified scope | The identifier is unique within the account. |
| input | noun | Data that a component receives | The input contains the requested date. |
| limit | noun | Bound whose unit and inclusion rule the contract specifies | The limit permits up to 20 results, including the twentieth. |
| missing | adjective | Absent from the named location or input | The field is missing from the request. |
| pending | adjective | Awaiting a named decision or action | The change is pending approval. |
| permission | noun | Authority to perform a specified action | Only reviewers have permission to approve the change. |
| denial | noun | Refusal of a specified operation | The client displays “Permission denied” after the denial of access. |
| persist | verb | Store data so that it survives a stated event | The service persists the receipt before it returns success. |
| publish | verb | Make the specified version available at the named destination | The editor publishes version 3 to the public site. |
| receipt | noun | Record that confirms the event defined by the contract | The receipt confirms the upload of version 3. |
| reject | verb | Refuse an input or transition | If the required field is missing, the server rejects the request. |
| request | noun | Input that asks a service to perform an operation | The request contains one account ID. |
| restore | verb | Return data to the state captured by a named source | The operator restores the table from the snapshot. |
| retry | verb | Attempt the same operation again under the stated identity rules | The client retries the request with the original key. |
| role | noun | Named set of responsibilities or permissions in the product | The Reviewer role permits approval of drafts. |
| rollback | noun | Operation that reverses changes within a defined boundary | The rollback restores both records. |
| save | verb | Write the specified data to its destination | The service saves the draft in the workspace. |
| state | noun | Condition that remains true until a transition occurs | The job stays in the queued state until a worker accepts it. |
| status code | noun | Value that the protocol assigns to a response | The response contains status code `409`. |
| timeout | noun | Duration allowed for the named operation in this example | The connection timeout is 30 s from the start of the attempt. |
| validate | verb | Apply named acceptance rules to an input | The server validates the date against the schema. |
| version | noun | Distinct revision identified by the project | Save the version that the operator approved. |

### If the assignment includes glossary maintenance

An entry in a maintained project glossary needs the canonical spelling, part of speech, definition and source. Add the approved abbreviation or alias if readers encounter it. A new project's proposed term stays provisional until the responsible source establishes it. For example, `job_id` can identify a job while `request_id` identifies a request to create or inspect one. Merge those terms only when the contract explicitly identifies the same object.
