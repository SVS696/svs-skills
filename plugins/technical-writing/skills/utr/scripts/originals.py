"""Download the listed reading copies or verify an installation offline."""

import argparse
import hashlib
import subprocess
import tempfile
from pathlib import Path

from gost_markdown import check_copy, convert

# Each entry identifies the exact copy described in references/sources.md.
FILES = (
    ("GOST-R-58049-2017.pdf", "4f734dc5b1ead2c0e83b837754268947be2365facd277ca46cecf5ffe005e5c5",
     "https://files.stroyinf.ru/Data2/1/4293739/4293739569.pdf"),
    ("GOST-R-59194-2020.pdf", "830261164041cbbf3e98666efeb27a685155d5ce56f8e6e7b1e8640422dcd538",
     "https://files.stroyinf.ru/Data/753/75310.pdf"),
    ("GOST-34.602-2020.pdf", "5dd9b0cd29158833aeaeb2269b6ed9f5f171a8e685ce1ee1908c011a7025b243",
     "https://files.stroyinf.ru/Data/760/76009.pdf"),
    ("GOST-2.105-95.pdf", "f0bbf416e61d0e698504dc3ddad3b837655eec0bb09813c13e306321a89d39fd",
     "https://usfeu.ru/media/filer_public/44/d8/44d830d8-e009-44e3-af4e-0d88053cd800/gost_2105-95.pdf"),
    ("GOST-R-2.105-2019.pdf", "6345e7cf6ad42b8db4f11b5fb2a0d42951272e9aea5bb0f870caf26266065a2f",
     "https://kd.vnesenie-v-reestr.ru/uploads/norms/gost-r-2-105-2019.pdf"),
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
    root = Path(__file__).resolve().parents[1]
    destination = root / "standards"
    legacy = root / "references" / "originals"
    for name, expected, url in FILES:
        target = destination / name
        is_pdf = target.suffix == ".pdf"
        if is_pdf and (destination / f"{target.stem}.json").is_file():
            check_copy(destination, target.stem, expected)
        elif not is_pdf and target.is_file():
            if sha256(target) != expected:
                raise SystemExit(f"{name}: file differs from the recorded edition.")
        elif args.check:
            raise SystemExit(f"{name}: local reading copy missing.")
        else:
            destination.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(dir=destination) as staging:
                source = legacy / name
                if not source.exists():
                    source = Path(staging) / name
                    subprocess.run(["curl", "--fail", "--location", "--silent", "--show-error",
                                    "--proto", "=https", "--proto-redir", "=https",
                                    "--max-time", "120", "--retry", "1",
                                    "--output", str(source), url], check=True)
                if sha256(source) != expected:
                    raise SystemExit(f"{name}: file differs from the recorded edition.")
                if is_pdf:
                    convert(source, destination, url, expected)
                    check_copy(destination, target.stem, expected)
                else:
                    try:
                        target.hardlink_to(source)
                    except FileExistsError:
                        if sha256(target) != expected:
                            raise SystemExit(f"{name}: another installation wrote a different file.")
        print(f"OK {target.with_suffix('.md').name if is_pdf else name}")


if __name__ == "__main__":
    main()
