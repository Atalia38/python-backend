

import re
from collections import Counter
from pathlib import Path

TOKEN = re.compile(r"[A-Za-z0-9']+")

class EmptyTextError(Exception): ...

def tokenize(text: str) -> list[str]:
    return TOKEN.findall(text.lower())

def word_counts(path: str | Path) -> Counter:
    path = Path(path)
    try:
        if not path.exists():
            raise FileNotFoundError(path)
        text = path.read_text(encoding="utf-8")
        words = tokenize(text)
        if not words:
            raise EmptyTextError("No words found.")
        return Counter(words)
    except FileNotFoundError as e:
        print(f"Error: file not found → {e}")
        return Counter()
    except UnicodeDecodeError:
        print("Error: wrong encoding (use UTF-8).")
        return Counter()
    except EmptyTextError as e:
        print(f"Error: {e}")
        return Counter()

def save_counts_csv(counts: Counter, out_path: str | Path, top: int | None = None):
    items = counts.most_common(top) if top else counts.most_common()
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        for w, n in items:
            f.write(f"{w},{n}\n")


