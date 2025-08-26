# async_simulated_downloads.py
from __future__ import annotations
import asyncio, random, sys
from typing import Sequence

async def download(name: str, size_mb: int | None = None) -> None:
    """Simulate downloading `size_mb` MB in 1 MB chunks with variable network speed."""
    if size_mb is None:
        size_mb = random.randint(5, 20)  # fake total size
    chunks = size_mb
    for i in range(1, chunks + 1):
        await asyncio.sleep(random.uniform(0.05, 0.2))  # "network" delay
        pct = int(i / chunks * 100)
        bar = "#" * (pct // 5)
        print(f"[{name:<12}] {pct:3d}% |{bar:<20}| ({i}/{chunks} MB)")
    print(f"[{name:<12}] DONE ({size_mb} MB)")

async def main(argv: Sequence[str]) -> None:
    if len(argv) < 2:
        print("Usage: python async_simulated_downloads.py <file1> <file2> ...")
        return
    names = argv[1:]
    tasks = [asyncio.create_task(download(n)) for n in names]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main(sys.argv))
