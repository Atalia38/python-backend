from pathlib import Path

def c_to_f(c: float) -> float:
    return c * 9/5 + 32

def convert_file(inp: str | Path = "celsius.txt",
                out: str | Path = "fahrenheit.txt",
                decimals: int = 2) -> int:
    """
    Convert Celsius values from `inp` to Fahrenheit and write formatted lines to `out`.
    Returns the count of successfully converted lines.
    """
    inp, out = Path(inp), Path(out)
    written = 0
    try:
        with inp.open("r", encoding="utf-8") as fin, \
            out.open("w", encoding="utf-8", newline="\n") as fout:
            for lineno, raw in enumerate(fin, 1):
                s = raw.strip()
                if not s:
                    continue  # skip empty lines
                try:
                    c = float(s)
                except ValueError:
                    print(f"Skipped line {lineno}: non-numeric value {s!r}")
                    continue
                f = c_to_f(c)
                # required format: {Celsius}C = {Fahrenheit}F
                fout.write(f"{c:.{decimals}f}C = {f:.{decimals}f}F\n")
                written += 1
    except FileNotFoundError:
        print(f"Error: input file not found → {inp}")
    except PermissionError:
        print(f"Error: permission issue reading/writing → {inp} / {out}")
    except UnicodeDecodeError:
        print("Error: decode failed (use UTF-8 input).")
    else:
        print(f"Done. Wrote {written} formatted lines to {out}")
    return written

if __name__ == "__main__":
    convert_file()