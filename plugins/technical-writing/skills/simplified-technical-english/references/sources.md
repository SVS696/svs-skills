# Source editions and local originals

Use this catalogue when the task calls for a specific source, a formal assessment or installation of reading copies. An ordinary ticket can be written and checked from its source text and project terms, fully offline. For a formal STE check, open the complete edition that governs the document. Page numbers below are one-based PDF pages, including the cover.

## ASD-STE100 Issue 9

ASD issued Issue 9 on 15 January 2025. The complete publisher PDF has 434 pages. Part 1 begins on page 43. Part 2 begins on page 129. The dictionary introduction and usage information are on pages 131–147. The alphabetical tables start on page 149. The last lexical entries appear on page 433. Page 434 closes the dictionary. Word lookup must use these tables rather than the list of changes at the start of the PDF. [Publisher's downloads](https://www.asd-ste100.org/STE_downloads.html) · [Full official Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

In a private installation the full rules and dictionary are in `references/originals/ASD-STE100_ISSUE9.pdf`. The public skill carries original editorial guidance. Page 2 of the official PDF reserves reproduction and publication to written authorization, with special rights for listed organizations. Obtain a personal copy from the publisher when the assignment requires the original and the file is absent. Keep the publisher's full original and notices intact. In a formal review, verify the issue specified by the contract even when a newer issue exists.

## IBM EasyEnglish

Arendse Bernth describes a checker that finds structural ambiguity and suggests alternatives. Its examples help a reviewer investigate ambiguous participles, coordination, passive constructions and pronoun reference when a second reading affects the reader. The source describes a research tool. It provides no approved ASD vocabulary or certification process. The 1997 paper is available locally as `references/originals/Bernth-EasyEnglish-1997.pdf` when installed. [IBM publication record](https://research.ibm.com/publications/easyenglish-a-tool-for-improving-document-quality) · [1997 paper from ACL Anthology](https://aclanthology.org/A97-1024.pdf) · [1998 paper record](https://aclanthology.org/1998.amta-papers.15/)

## Requirements and protocols

ISO/IEC/IEEE 29148:2018 covers requirements engineering. Use its applicable provisions when the project adopts that standard. Its public catalogue record is available online. The full licensed standard is separate from this skill. EARS supplies patterns for requirements when the user or project selects that notation. The examples in this skill explain how to use the patterns offline. [ISO catalogue](https://www.iso.org/standard/72089.html) · [EARS guide by Alistair Mavin](https://alistairmavin.com/ears/)

RFC 2119 (March 1997) defines requirement levels for specifications that adopt its convention. RFC 8174 (May 2017) clarifies when the uppercase keywords have their special meanings. Together they form BCP 14. The private source directory can contain the complete publisher texts. [RFC 2119 text](https://www.rfc-editor.org/rfc/rfc2119.txt) · [RFC 8174 text](https://www.rfc-editor.org/rfc/rfc8174.txt)

## Restore or verify optional originals

Use this maintenance command when you need the optional reading copies. Everyday writing does not require a download or an integrity check. From the skill directory, run `python3 scripts/originals.py` to download the listed editions to this skill. The command uses Python 3.10 or later and curl. It checks the SHA-256 of each download and preserves an existing file with a different hash. For an offline check, run `python3 scripts/originals.py --check`. Run these commands when installing or verifying the reading copies.

For a manual installation, save an original from the corresponding publisher link above to the `references/originals/` directory inside your private copy of this skill. Use the filename in this table. Calculate its SHA-256 and compare it with the table. Open each PDF and confirm the edition or title. If the publisher changes a file, verify the new edition and record the new hash before using it as evidence. A downloaded HTML error page does not qualify as the original.

| Filename | SHA-256 of the verified download |
|---|---|
| `ASD-STE100_ISSUE9.pdf` | `d1f4ea9e7cd6e46b47aa9057209f99e78c0e9cfc4e27a5b07895b05c1a166431` |
| `Bernth-EasyEnglish-1997.pdf` | `fc6bf81bc664f0a223274d940ae5820a4ec5d7d5888d854fbe06e843772310ef` |
| `RFC2119.txt` | `3c2ceb7bfc84cd34720f4a5271338ab9d8280d34bdd1eb250c64306202f2ed8b` |
| `RFC8174.txt` | `5ca0e2f90be0bc5928ee465f76518fee316dfa775aed885658a29a419cc293b7` |
