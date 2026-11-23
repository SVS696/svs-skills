# Technical writing skills

Select the skill by the language of the deliverable. The language of the request can differ.

| Deliverable | Skill | Local sources |
|---|---|---|
| Russian requirements, technical specifications and procedures | [УТР](skills/utr/SKILL.md) | [ГОСТы и прикладной словарь](skills/utr/references/sources.md) |
| English requirements, technical specifications and procedures | [Simplified Technical English](skills/simplified-technical-english/SKILL.md) | [ASD-STE100 Issue 9, IBM EasyEnglish and BCP 14](skills/simplified-technical-english/references/sources.md) |

Copy either complete skill directory to your skills directory. To add the reference publications to that copy, run `python3 scripts/originals.py` from its root. Both skills build local Markdown in `standards/`. For Russian editions, install Poppler, Pillow, PyMuPDF, NumPy and opencv-python-headless. For English editions, install pdfplumber and PyMuPDF. The Issue 9 converter reads the tagged table cells in the publisher PDF. To verify the files without a network connection, run `python3 scripts/originals.py --check`.

## Authoring and evaluation

Each manifest identifies the requested output language, when to use the skill, how to report a check, and what the reader needs to act. The working guides and examples are inside the skill. A missing source limits the findings that depend on it. These choices apply the [OpenAI Cookbook guidance for skills](https://developers.openai.com/cookbook/examples/skills_in_api#operational-best-practices) and the [GPT-6.2 family prompting guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra.md#prompting-best-practices).

Check a release from a copy of one skill. Request a rewrite and a check on a requirement that grants permission unless a status is HOLD. Verify the actor, modality, timer origin and exception. Repeat with the official publication absent. A formal finding must identify the missing evidence. Also try a request to implement an API without writing documentation. Neither language skill applies to that request.

On 22 November 2026, separate read-only runs of GPT-6.2 Sol and GPT-6.2 Astra completed the same three cases. Each model selected the Russian skill for checking a Russian requirement and the English skill for a translation requested in Russian. Both preserved the permission to retry at 30 seconds after a response and the prohibition in HOLD. Both declined to assert formal STE compliance without the publisher PDF. Neither selected a language skill for implementing a numeric sorter.

For a scope check, give the skill an ordinary ticket, then a passage that explicitly adopts a standard. Check the actual output in each case.

| Input | Expected result |
|---|---|
| A ticket renames a button to **Master Warning Control Panel**. | The ticket gives the exact new label. The word *Warning* in the label does not create a safety message. |
| A ticket grants the operator permission to open a single search result. | The operator keeps the choice. The ticket needs no new sections to express it. |
| A protocol adopts BCP 14 and says that the client MAY resend a request. | The edited clause preserves the permission and the case of MAY. |
| A Russian system specification adopts GOST 34.602-2020. The customer confirms that a required section has no requirements. | The section stays in the specification with that information. |
| An existing project template uses English headings and links to them from Russian paragraphs. | An edit to the prose keeps the headings and their link targets exactly as supplied. |
