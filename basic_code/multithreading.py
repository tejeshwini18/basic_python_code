"""
SUMMARY:
  File:        multithreading.py
  Purpose:    Demonstrates multithreading using the threading module.
  Action:     Spawns multiple threads in one process; each runs a task in parallel.
              Threads share memory. Good when tasks spend time waiting on I/O.
  Best for:   I/O-bound work (network, disk, waiting on responses).
"""
import time
from threading import Thread
num= 0

# The bottleneck of the code which is CPU-bound
def upgrade(n):
while num<400000000:
num=num+1

# Creation of multiple threads
t1 = Thread(target=upgrade, args=(num//2,))
t2 = Thread(target=upgrade, args=(num//2,))

# multi thread architecture, recording time
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

