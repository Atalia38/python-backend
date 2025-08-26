# async_fetch_urls.py
from __future__ import annotations
import asyncio, sys
from typing import Sequence
import aiohttp

async def fetch(session: aiohttp.ClientSession, url: str, timeout: float = 8.0) -> tuple[str, int]:
    """Return (url, size) or (url, -1) on error."""
    try:
        async with session.get(url, timeout=timeout) as resp:
            text = await resp.text()
            return url, len(text)
    except Exception:
        return url, -1

async def gather_all(urls: Sequence[str]) -> None:
    connector = aiohttp.TCPConnector(limit=20)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [asyncio.create_task(fetch(session, u)) for u in urls]
        for done in asyncio.as_completed(tasks):
            url, size = await done
            print(f"[OK] {url} -> {size} bytes" if size >= 0 else f"[ERROR] {url}")

def main(argv: Sequence[str]) -> None:
    if len(argv) < 2:
        print("Usage: python async_fetch_urls.py <url1> <url2> ...")
        return
    asyncio.run(gather_all(argv[1:]))

if __name__ == "__main__":
    main(sys.argv)
