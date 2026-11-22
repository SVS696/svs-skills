# How to write and check a passage

These working checks cover the nine topics in Part 1 of ASD-STE100 Issue 9. Page numbers below count from the PDF cover. Rule numbers identify where to test an exception or check an exact provision. The examples in this guide are original software documentation examples. For a formal review, read the full rule and apply the official dictionary. [Source and edition](sources.md)

| Passage or feature | Issue 9 rules | First PDF page |
|---|---|---|
| General vocabulary, terms, word forms, spelling | 1.1–1.14 | 45 |
| Compound names | 2.1–2.2 | 63 |
| Actions, tense, and voice | 3.1–3.7 | 67 |
| Sentence structure | 4.1–4.5 | 77 |
| Operator procedures | 5.1–5.5 | 87 |
| Explanations and descriptions | 6.1–6.6 | 95 |
| Safety messages | 7.1–7.3 | 103 |
| Punctuation and counting | 8.1–8.7 | 107 |
| Rewriting and consistent language | 9.1–9.4 | 115 |

### 1. Choose words for their intended meaning

Look up a common word before you use it in a formal STE text. Match the dictionary entry to the word's function in the sentence and its intended meaning. Confirm the permitted verb or adjective form. A word can have different entries for two parts of speech. A word with several everyday meanings can have only one permitted meaning in a given entry.

Use technical nouns and technical verbs when the term fits an allowed category. Check approved product names, abbreviations, operations and local terminology against the project's term source. Avoid local jargon and competing names for one item. Use the spelling specified by the governing directive. The standard uses American spelling by default. See the [lookup procedure and working vocabulary](vocabulary.md) for the distinction between approval of a label and approval of an ordinary word.

### 2. Unpack long compound nouns

For a new noun group, keep the group within three words. Show the relation between its parts with a verb or preposition. To edit “account deletion request approval date,” first determine whether the date records approval of a request or approval of a deletion. A possible result is “the date when the administrator approved the request to delete the account.”

Copy an established long technical name exactly on first use. When the context permits, define one shorter form and use it consistently. Keep hyphens that identify meaningful groups. In an interface procedure, preserve the actual control label even when it is long.

### 3. Make the action visible

Prefer an action verb to a noun that hides who acts. “The client sends the report” identifies both the actor and the action. For procedures, address the reader directly. For descriptions, use the active voice when the source identifies the actor. Rule 3.6 allows the passive in descriptive text when the actor is unknown. If a requirement needs an accountable actor and the source omits it, record a question.

In the strict profile, check the permitted forms and tenses against rules 3.1–3.5. The basic choices include an infinitive, a command, simple present, past or future, and an adjectival past participle. Examine chains of auxiliaries and progressive or perfect forms. Preserve timing before you simplify them. Check an “-ing” form for its permitted use in a technical noun. A frozen identifier such as `isProcessing` stays in its contract spelling.

### 4. Build sentences readers can parse

Give each condition a clear scope. Repeat a short noun when a pronoun could refer to two objects. Retain articles and other words that signal the subject, object and ownership. Spell out contractions. Use a list when a long chain of alternatives hides the decision. Give each list item the same grammatical relation to the lead sentence.

Use connectors that describe the actual relationship. “Then” establishes order. “If” sets a condition. “Because” introduces the reason. Do not insert a causal relationship when the source describes timing only.

### 5. Write procedures for the person who acts

Put a prerequisite before its command. Use a command for the step. Put each independent instruction in its own sentence. Keep simultaneous operations together when success depends on acting at the same time. Preserve the required sequence of dependent steps. Place a required action in the step itself. A note can explain what the reader sees or why a step exists.

For a strict check, limit a procedural sentence to 20 words, counted under section 8. To shorten a step, separate the condition from supporting information. For example, “If the status is READY, select **Export**.” A following sentence can explain the file format.

### 6. Explain one topic at a time

Introduce the component before you describe its states or outputs. Repeat the appropriate technical noun as the explanation develops. Put the normal behavior in its own paragraph. Describe each exception beside the behavior it changes. Check that a paragraph covers one subject and that its sentences follow a useful order. For a strict check, the limits are 25 words per descriptive sentence and six sentences per paragraph.

### 7. Preserve safety instructions

Use the hazard level and signal word specified by the governing source. Start with the condition or action that protects the reader. Explain the identified harm or consequence. Put the instruction where the reader can act on it before exposure. If the source does not identify the hazard or the applicable level, preserve the available instruction and ask the responsible specialist. An ordinary validation error does not establish a safety hazard.

### 8. Apply punctuation and counting rules

Split clauses joined by a semicolon. Use a hyphen to group words when that grouping changes how readers parse a name. Use parentheses sparingly for such items as a reference, an identifier, or a defined abbreviation. Apply rule 8.3 when formal compliance is required.

Use rules 8.4–8.7 for a formal count. A colon before a vertical list ends the introductory sentence for this count. Count a parenthetical group, a measurement with its unit, an alphanumeric identifier or a quoted label as one element under the applicable rule. A hyphenated expression also counts as one. Other special cases include names and headings. A whitespace count cannot establish a violation by itself. Keep the original punctuation inside code, literal labels, and string values.

### 9. Test the whole rewrite

When word replacement makes a sentence awkward or changes its meaning, rebuild the sentence around the action. Check common words used in combination. A verb followed by a particle can have a different meaning from the verb alone. Use a direct verb with the intended sense or the exact name of the command. Choose consistent terms, spelling and phrasing through the whole procedure. After the change, compare the result with the source and execute the steps on paper.
