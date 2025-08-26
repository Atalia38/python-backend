# multithreaded_tasks.py
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading, time, random

def work(task_id: int) -> str:
    """Simulate I/O-like work with a random delay."""
    delay = random.uniform(0.3, 1.5)
    time.sleep(delay)
    return f"Task {task_id} finished on {threading.current_thread().name} in {delay:.2f}s"

def main() -> None:
    print("Submitting 8 tasks to a thread pool with 4 workers...\n")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="worker") as pool:
        futures = [pool.submit(work, i) for i in range(1, 9)]
        for fut in as_completed(futures):
            print(fut.result())
    print(f"\nAll done in {time.perf_counter() - start:.2f}s (concurrent).")

if __name__ == "__main__":
    main()
