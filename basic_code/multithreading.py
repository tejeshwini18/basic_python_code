"""
SUMMARY:
  File:        multithreading.py
  Purpose:    Demonstrates multithreading using the threading module.
  Action:     Spawns multiple threads in one process; each runs a task in parallel.
              Threads share memory. Good when tasks spend time waiting on I/O.
  Best for:   I/O-bound work (network, disk, waiting on responses).
"""

import threading
import time


def task(thread_id: int, duration: float) -> None:
    """Simulate an I/O-bound task (e.g., waiting for response, reading file)."""
    print(f"Thread {thread_id} started")
    time.sleep(duration)
    print(f"Thread {thread_id} finished after {duration}s")


def main() -> None:
    # Create threads
    threads = [
        threading.Thread(target=task, args=(i, 1.0 + i * 0.5))
        for i in range(1, 5)
    ]

    start = time.perf_counter()

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    print(f"\nAll threads done in {elapsed:.2f}s (would be ~3.5s if sequential)")


if __name__ == "__main__":
    main()
