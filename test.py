import numpy as np


def test_heap(n=100):
  from heap import make_max_heap, remove_max
  for _ in range(n):
    vals = np.random.uniform(size=1000)
    items = list(zip(vals, vals))
    heap = make_max_heap(items)
    heap_sorted = []
    sorted_vals = sorted(vals)[::-1]

    while len(heap) > 1:
      heap_sorted.append(remove_max(heap))
    assert(heap_sorted == sorted_vals)
  print("All tests for \'heap.py\' passed!")



if __name__ == "__main__":
  test_heap()