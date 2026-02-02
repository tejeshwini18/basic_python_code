"""
SUMMARY:
  File:        multiprocessing_demo.py
  Purpose:    Demonstrates multiprocessing using the multiprocessing module.
  Action:     Spawns separate OS processes; work is distributed via a Process Pool.
              Each process has its own memory and can use a different CPU core.
  Best for:   CPU-bound work (heavy math, data crunching, parallel computation).
"""

import multiprocessing
import time


def cpu_task(n: int) -> int:
    """Simulate a CPU-bound task (e.g., number crunching)."""
    total = 0
    for i in range(n):
        total += i * i
    return total


def worker(process_id: int, value: int) -> tuple[int, int]:
    """Worker function each process runs."""
    result = cpu_task(value)
    return process_id, result


def main() -> None:
    # Use 4 processes; each does a chunk of work
    with multiprocessing.Pool(processes=4) as pool:
        start = time.perf_counter()
        # Map work across processes
        results = pool.starmap(worker, [(i, 1_000_000) for i in range(4)])
        elapsed = time.perf_counter() - start

    print("Results:", results)
    print(f"Completed in {elapsed:.2f}s using 4 processes")


if __name__ == "__main__":
    main()
