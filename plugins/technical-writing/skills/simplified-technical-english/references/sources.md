# Source editions and local originals

Use this catalogue when the task calls for a specific source, a formal assessment or installation of reading copies. An ordinary ticket can be written and checked from its source text and project terms, fully offline. For a formal STE check, open the complete edition that governs the document. Page numbers in the Markdown reading copies include the cover. Each page links to its source edition.

## ASD-STE100 Issue 9

ASD issued Issue 9 on 15 January 2025. The complete publisher PDF has 434 pages. Part 1 begins on page 43. Part 2 begins on page 129. The dictionary introduction and usage information are on pages 131–147. The alphabetical tables start on page 149. The last lexical entries appear on page 433. Page 434 closes the dictionary. Word lookup must use these tables rather than the list of changes at the start of the PDF. [Publisher's downloads](https://www.asd-ste100.org/STE_downloads.html) · [Full official Issue 9 PDF](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)

The local Markdown edition in `standards/ASD-STE100_ISSUE9.md` retains the rules and the four dictionary columns. Capitalization distinguishes approved entries from words with alternatives. Check the printed page if typography affects the finding. The public skill carries original editorial guidance. Page 2 of the official PDF reserves reproduction and publication to written authorization, with special rights for listed organizations. Obtain a personal copy from the publisher when the assignment requires the original and the file is absent. Keep the publisher's full original and notices intact. In a formal review, verify the issue specified by the contract even when a newer issue exists.

## IBM EasyEnglish

Arendse Bernth describes a checker that finds structural ambiguity and suggests alternatives. Its examples help a reviewer investigate ambiguous participles, coordination, passive constructions and pronoun reference when a second reading affects the reader. The source describes a research tool. It provides no approved ASD vocabulary or certification process. The local copy in `standards/Bernth-EasyEnglish-1997.md` follows the seven pages of the ANLP paper. The scan has OCR errors. Check exact quotations against the source page. [IBM publication record](https://research.ibm.com/publications/easyenglish-a-tool-for-improving-document-quality) · [1997 paper from ACL Anthology](https://aclanthology.org/A97-1024.pdf) · [1998 paper record](https://aclanthology.org/1998.amta-papers.15/)

### Bernth 1998 — EasyEnglish: Preprocessing for MT

This CLAW workshop paper shows how English wording affects machine translation. Sections 3.1 and 3.2 cover ambiguous attachments, implicit subjects and hyphens. The references on printed page 40 list *EasyEnglish: Addressing Structural Ambiguity* as a separate work then in preparation. The local Markdown copy uses OCR of the 12 scanned pages (printed pages 30–41). Check exact wording, especially the German translation examples, against the linked page image. [CLAW paper](https://mt-archive.net/90/CLAW-1998-Bernth.pdf)

### Bernth 1998 — EasyEnglish: Addressing Structural Ambiguity

This is a reading note based on the public abstract. The publisher lists the chapter on pages 164–173. The full chapter requires access to the proceedings. Bernth describes how the checker offers different rewrites when grammar permits more than one interpretation. For example, in “review cached requests and responses,” *cached* could describe only requests or both groups. Ask which items are cached before choosing the wording. This example was written for the skill. [Publisher record](https://doi.org/10.1007/3-540-49478-2_16) · [ACL abstract](https://aclanthology.org/1998.amta-papers.15/)

## Comparing controlled languages

Sharon O’Brien compared eight sets of writing rules, including AECMA Simplified English and IBM Easy English. All eight favored short sentences. Some set word limits, and others gave qualitative guidance. Section 4 separates rules shared by all eight from rules shared by at least four. Appendix A gives the author’s proposed starting set. For a formal check, apply the edition named by the project. [CLT 2003 paper](https://mt-archive.net/00/CLT-2003-Obrien.pdf)

## Requirements and protocols

ISO/IEC/IEEE 29148:2018 covers requirements engineering. Use its applicable provisions when the project adopts that standard. The local reading copy in `standards/ISO-IEC-IEEE-29148-2018.md` uses the November 2018 second edition available in the BYU–Idaho course. Its 104 PDF pages include the front matter, three annexes and bibliography. The local copy keeps the university license notices. [Course PDF](https://byui-cse.github.io/cse372-course/Reading/CSE372Week10-IEEE.pdf) EARS supplies patterns for requirements when the user or project selects that notation. The examples in this skill explain how to use the patterns offline. [ISO catalogue](https://www.iso.org/standard/72089.html) · [EARS guide by Alistair Mavin](https://alistairmavin.com/ears/)

RFC 2119 (March 1997) defines requirement levels for specifications that adopt its convention. RFC 8174 (May 2017) clarifies when the uppercase keywords have their special meanings. Together they form BCP 14. Both complete RFCs are available locally in Markdown. [RFC 2119 text](https://www.rfc-editor.org/rfc/rfc2119.txt) · [RFC 8174 text](https://www.rfc-editor.org/rfc/rfc8174.txt)

## Restore or verify optional originals

From the skill directory, run `uv run --with pdfplumber==0.11.11 --with pymupdf==1.27.2.3 python scripts/originals.py`. If these packages are already installed, run `python3 scripts/originals.py`. Install Tesseract with English language data to convert the CLAW scan. The command needs curl to download missing editions. It verifies each source against the table below. It can reuse originals from an earlier installation.

The installer writes Markdown, illustrations and checksum receipts to `standards/`. Copy this directory with the skill for offline use. To verify a copy offline, run `python3 scripts/originals.py --check`.

| Filename | SHA-256 of the verified download |
|---|---|
| `ASD-STE100_ISSUE9.pdf` | `d1f4ea9e7cd6e46b47aa9057209f99e78c0e9cfc4e27a5b07895b05c1a166431` |
| `Bernth-EasyEnglish-1997.pdf` | `fc6bf81bc664f0a223274d940ae5820a4ec5d7d5888d854fbe06e843772310ef` |
| `RFC2119.txt` | `3c2ceb7bfc84cd34720f4a5271338ab9d8280d34bdd1eb250c64306202f2ed8b` |
| `RFC8174.txt` | `5ca0e2f90be0bc5928ee465f76518fee316dfa775aed885658a29a419cc293b7` |
| `ISO-IEC-IEEE-29148-2018.pdf` | `27c8f1f355985a902dd4d1467ff1823e8102fdb35e8832232c4121b307d70450` |
| `Bernth-CLAW-1998.pdf` | `7e2fadc9f5cd72444e9b7beb8d0e94c8d5c165d801ceb9a0fc60e90f59f59b33` |
| `OBrien-CLT-2003.pdf` | `730a65ff45a5d1a2845850d780f77ae2dde47c10ea605094f7306a7be670664f` |
