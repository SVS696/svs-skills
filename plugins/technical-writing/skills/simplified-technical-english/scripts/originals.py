"""Download the listed reading copies or verify an installation offline."""

import argparse
import hashlib
import subprocess
import tempfile
from pathlib import Path

# Each entry identifies the exact copy described in references/sources.md.
FILES = (
    ("ASD-STE100_ISSUE9.pdf", "d1f4ea9e7cd6e46b47aa9057209f99e78c0e9cfc4e27a5b07895b05c1a166431",
     "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf"),
    ("Bernth-EasyEnglish-1997.pdf", "fc6bf81bc664f0a223274d940ae5820a4ec5d7d5888d854fbe06e843772310ef",
     "https://aclanthology.org/A97-1024.pdf"),
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without downloading.")
    args = parser.parse_args()
    destination = Path(__file__).resolve().parents[1] / "references" / "originals"
    for name, expected, url in FILES:
        target = destination / name
        if target.exists():
            if sha256(target) != expected:
                raise SystemExit(f"{name}: existing file differs from the recorded edition.")
        elif args.check:
            raise SystemExit(f"{name}: file missing.")
        else:
            destination.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(dir=destination) as staging:
                download = Path(staging) / name
                subprocess.run(["curl", "--fail", "--location", "--silent", "--show-error",
                                "--proto", "=https", "--proto-redir", "=https",
                                "--max-time", "120", "--retry", "1",
                                "--output", str(download), url], check=True)
                if sha256(download) != expected:
                    raise SystemExit(f"{name}: download differs from the recorded edition.")
                # The link publishes a complete file without replacing a concurrent install.
                try:
                    target.hardlink_to(download)
                except FileExistsError:
                    if sha256(target) != expected:
                        raise SystemExit(f"{name}: another installation wrote a different file.")
        print(f"OK {name}")


if __name__ == "__main__":
    main()
