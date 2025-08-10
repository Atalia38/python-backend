from pathlib import Path

p = Path("demo.txt")


with p.open("w", encoding="utf-8", newline="\n") as f:
    f.write(" first line \nsecond   line\n\nthird line  ")


with p.open("r", encoding="utf-8") as f:
    content = f.read()
print("RAW:", content)


cleaned = []
with p.open("r", encoding="utf-8") as f:
    for line in f:
        line = " ".join(line.strip().split())  
        if line:
            cleaned.append(line)
print("CLEAN:", cleaned)


with p.open("a", encoding="utf-8", newline="\n") as f:
    f.write("\nappended line")

print("SIZE (bytes):", p.stat().st_size)
