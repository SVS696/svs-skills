"""Download the listed reading copies or verify an installation offline."""

import argparse
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

# Each entry identifies the exact copy described in references/sources.md.
FILES = (
    ("ASD-STE100_ISSUE9.pdf", "d1f4ea9e7cd6e46b47aa9057209f99e78c0e9cfc4e27a5b07895b05c1a166431",
     "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf"),
    ("Bernth-EasyEnglish-1997.pdf", "fc6bf81bc664f0a223274d940ae5820a4ec5d7d5888d854fbe06e843772310ef",
     "https://aclanthology.org/A97-1024.pdf"),
    ("Bernth-CLAW-1998.pdf", "7e2fadc9f5cd72444e9b7beb8d0e94c8d5c165d801ceb9a0fc60e90f59f59b33",
     "https://mt-archive.net/90/CLAW-1998-Bernth.pdf"),
    ("ISO-IEC-IEEE-29148-2018.pdf", "27c8f1f355985a902dd4d1467ff1823e8102fdb35e8832232c4121b307d70450",
     "https://byui-cse.github.io/cse372-course/Reading/CSE372Week10-IEEE.pdf"),
    ("RFC2119.txt", "3c2ceb7bfc84cd34720f4a5271338ab9d8280d34bdd1eb250c64306202f2ed8b",
     "https://www.rfc-editor.org/rfc/rfc2119.txt"),
    ("RFC8174.txt", "5ca0e2f90be0bc5928ee465f76518fee316dfa775aed885658a29a419cc293b7",
     "https://www.rfc-editor.org/rfc/rfc8174.txt"),
)


def sha256(path):
    with path.open("rb") as source:
        digest = hashlib.sha256()
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
        return digest.hexdigest()


def receipt_for(directory, source, expected):
    stem = Path(source).stem
    paths = [directory / f"{stem}.md", *sorted(directory.glob(f"{stem}-p*.png"))]
    return {"source_sha256": expected, "files": {p.name: sha256(p) for p in paths}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify Markdown and illustrations offline.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    destination = root / "standards"
    for name, expected, url in FILES:
        stem = Path(name).stem
        receipt = destination / f"{stem}.json"
        if receipt.is_file():
            if json.loads(receipt.read_text()) != receipt_for(destination, name, expected):
                raise SystemExit(f"{stem}: local reading copy differs from the receipt.")
        elif args.check:
            raise SystemExit(f"{stem}: local reading copy missing.")
        else:
            from reading_copy import build
            destination.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(dir=destination) as tmp:
                staging = Path(tmp)
                original = root / "references" / "originals" / name
                if not original.is_file():
                    original = staging / name
                    subprocess.run(["curl", "--fail", "--location", "--silent", "--show-error",
                                    "--proto", "=https", "--proto-redir", "=https",
                                    "--max-time", "120", "--retry", "1", "--output", str(original), url],
                                   check=True)
                if sha256(original) != expected:
                    raise SystemExit(f"{name}: source differs from the recorded edition.")
                build(original, staging, url)
                record = receipt_for(staging, name, expected)
                for filename in record["files"]:
                    (staging / filename).replace(destination / filename)
                staged_receipt = staging / receipt.name
                staged_receipt.write_text(json.dumps(record, indent=2) + "\n")
                staged_receipt.replace(receipt)
        print(f"OK {stem}.md")


if __name__ == "__main__":
    main()
