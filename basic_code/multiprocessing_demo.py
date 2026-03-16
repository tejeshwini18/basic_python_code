"""
SUMMARY:
  File:        multiprocessing_demo.py
  Purpose:    Demonstrates multiprocessing using the multiprocessing module.
  Action:     Spawns separate OS processes; work is distributed via a Process Pool.
              Each process has its own memory and can use a different CPU core.
  Best for:   CPU-bound work (heavy math, data crunching, parallel computation).
"""

import multiprocessing

def print_cube(num):
	print("Cube: {}".format(num * num * num))

def print_square(num):
	print("Square: {}".format(num * num))

if __name__ == "__main__":
	# creating processes
	p1 = multiprocessing.Process(target=print_square, args=(10, ))
	p2 = multiprocessing.Process(target=print_cube, args=(10, ))
	p1.start()
	p2.start()
	# wait until process 1 is finished
	p1.join()
	p2.join()

	# both processes finished
	print("Done!")

