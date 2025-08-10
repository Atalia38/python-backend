

# palindrome_io.py
from pathlib import Path

def is_palindrome(word: str) -> bool:
    """
    Case-insensitive palindrome check.
    Keeps only letters/digits so 'RaceCar' or "Madam" pass.
    """
    cleaned = "".join(ch for ch in word.casefold() if ch.isalnum())
    return cleaned != "" and cleaned == cleaned[::-1]

def find_and_write_palindromes(
    input_path: str | Path = "input_words.txt",
    output_path: str | Path = "palindromes.txt",
) -> int:
    """Reads words (one per line), writes palindromes in UPPERCASE, returns count."""
    inp, out = Path(input_path), Path(output_path)

    # --- Read input file ---
    try:
        with inp.open("r", encoding="utf-8") as fin:
            words = [line.strip() for line in fin if line.strip()]
    except FileNotFoundError:
        print(f"Error: input file not found → {inp}")
        return 0
    except PermissionError:
        print(f"Error: no permission to read → {inp}")
        return 0
    except UnicodeDecodeError:
        print(f"Error: could not decode {inp} as UTF-8")
        return 0

    # --- Filter palindromes ---
    pals = [w for w in words if is_palindrome(w)]

    # --- Write output file ---
    try:
        with out.open("w", encoding="utf-8", newline="\n") as fout:
            for w in pals:
                fout.write(w.upper() + "\n")
    except PermissionError:
        print(f"Error: no permission to write → {out}")
        return 0
    else:
        print(f"Wrote {len(pals)} palindromes to {out}")
        return len(pals)

if __name__ == "__main__":
    # Example quick test:
    # Path("input_words.txt").write_text("radar\nhello\nLevel\nNoon\npython\n", encoding="utf-8")
    find_and_write_palindromes()
