
from pathlib import Path

def transform_file(src: str | Path, dst: str | Path) -> int:
    """
    Read src, trim + collapse spaces, number the lines, and write to dst.
    Returns number of lines written.
    """
    src, dst = Path(src), Path(dst)
    written = 0
    try:
        with src.open("r", encoding="utf-8") as fin, dst.open("w", encoding="utf-8", newline="\n") as fout:
            for i, raw in enumerate(fin, 1):
                line = " ".join(raw.strip().split())
                if not line:
                    continue
                fout.write(f"{i:04d}: {line}\n")
                written += 1
    except FileNotFoundError:
        print(f"Error: input not found → {src}")
    except PermissionError:
        print(f"Error: permission problem with {src} or {dst}")
    except UnicodeDecodeError:
        print("Error: decode as UTF-8 or set correct encoding.")
    else:
        print(f"OK: wrote {written} lines to {dst}")
    return written

