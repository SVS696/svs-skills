"""A personal skill installation can contain just one skill folder."""

import re
import shutil
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


class StandaloneLanguageSkillTest(unittest.TestCase):
    def test_offline_reference_routes_survive_a_folder_copy(self):
        skills = Path(__file__).resolve().parents[1] / "skills"
        for name in ("utr", "simplified-technical-english"):
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp).resolve() / name
                shutil.copytree(skills / name, package, ignore=shutil.ignore_patterns("originals", "standards"))
                entry = package / "SKILL.md"
                # The public package lists each optional edition and its source hash.
                catalogue = (package / "references/sources.md").read_text(encoding="utf-8")
                editions = re.findall(r"^\| `([^`]+)` \|.*`[a-f0-9]{64}` \|$", catalogue, re.M)
                self.assertTrue(editions, name)
                if name == "utr":
                    originals = {package / "standards" / Path(f).with_suffix(".md" if f.endswith(".pdf") else ".txt")
                                 for f in editions}
                else:
                    originals = {package / "standards" / Path(f).with_suffix(".md") for f in editions}
                direct = set()
                visited = set()
                pending = [entry]
                while pending:
                    document = pending.pop()
                    if document in visited:
                        continue
                    visited.add(document)
                    links = re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", document.read_text(encoding="utf-8"))
                    for link in links:
                        parts = urlsplit(link.strip("<>"))
                        if parts.scheme in {"https", "http", "mailto"} or not parts.path:
                            continue
                        target = (document.parent / unquote(parts.path)).resolve()
                        self.assertTrue(target.is_relative_to(package), (document.name, link))
                        if document == entry:
                            direct.add(target)
                        if target in originals:
                            continue
                        self.assertTrue(target.is_file(), (document.name, link))
                        if target.suffix == ".md":
                            pending.append(target)
                references = set((package / "references").glob("*.md"))
                self.assertTrue(references, name)
                missing = (references | originals) - direct
                self.assertFalse(missing, f"{name}: missing direct links in SKILL.md: {missing}")
