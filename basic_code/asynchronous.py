"""
SUMMARY:
  File:        asynchronous.py
  Purpose:    Demonstrates asynchronous (async/await) programming using asyncio.
  Action:     Runs multiple I/O-bound coroutines concurrently in a single thread.
              While one coroutine is waiting (e.g., sleep, network), others run.
  Best for:   I/O-bound tasks (APIs, DB calls, file I/O) without spawning threads.
"""

import asyncio
import time


async def async_task(task_id: int, duration: float) -> None:
    """Simulate an async I/O-bound operation (e.g., HTTP request, DB query)."""
    print(f"Task {task_id} started")
    await asyncio.sleep(duration)
    print(f"Task {task_id} finished after {duration}s")


async def main() -> None:
    # Create and run all tasks concurrently
    start = time.perf_counter()
    await asyncio.gather(
        async_task(1, 1.0),
        async_task(2, 1.5),
        async_task(3, 2.0),
        async_task(4, 2.5),
    )
    elapsed = time.perf_counter() - start
    print(f"\nAll tasks done in {elapsed:.2f}s (would be ~7s if sequential)")


if __name__ == "__main__":
    asyncio.run(main())
