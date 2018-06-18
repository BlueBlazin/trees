import numpy as np
from math import log2, ceil
from tree import make_print_tree


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
  print("All tests passed for \'heap.py\'!")


def test_avl():
  from avl import make_avl_tree
  # these tests trust root.height
  for _ in range(50):
    vals = np.random.uniform(size=500) * 50
    root = make_avl_tree(vals)
    assert(root.height <= 1 + ceil(log2(500)))

  for _ in range(25):
    vals = np.random.uniform(size=1000) * 100
    root = make_avl_tree(vals)
    assert(root.height <= 1 + ceil(log2(1000)))

  for _ in range(25):
    vals = np.random.randint(500, size=2000)
    root = make_avl_tree(vals)
    assert(root.height <= 1 + ceil(log2(2000)))
  
  # these tests don't trust root.height
  for _ in range(50):
    vals = np.random.uniform(size=500) * 50
    root = make_avl_tree(vals)
    assert(_test_avl_height(root) <= 1 + ceil(log2(500)))

  for _ in range(25):
    vals = np.random.uniform(size=1000) * 100
    root = make_avl_tree(vals)
    assert(_test_avl_height(root) <= 1 + ceil(log2(1000)))

  vals = range(5000)
  root = make_avl_tree(vals)
  assert(root.height <= 1 + ceil(log2(5000)))
  root = make_avl_tree(reversed(vals))
  assert(root.height <= 1 + ceil(log2(5000)))
  print("All tests passed for \'avl.py\'!")

def _test_avl_height(root):
  if root is None: return -1
  return 1 + max(_test_avl_height(root.left), _test_avl_height(root.right))


def test_redblack():
  from redblack import make_rb_tree
  for _ in range(50):
    vals = np.random.uniform(size=500) * 50
    root = make_rb_tree(vals)
    assert(_test_redblack_height(root) <= 2 * ceil(log2(500)))
  
  for _ in range(50):
    vals = np.random.uniform(size=1000) * 100
    root = make_rb_tree(vals)
    assert(_test_redblack_height(root) <= 2 * ceil(log2(1000)))
  
  for _ in range(25):
    vals = np.random.uniform(size=2000) * 500
    root = make_rb_tree(vals)
    assert(_test_redblack_height(root) <= 2 * ceil(log2(2000)))
  print("All tests passed for \'redblack.py\'!")

def _test_redblack_height(root):
  if root is None: return -1
  return 1 + max(_test_redblack_height(root.left), _test_redblack_height(root.right))



if __name__ == "__main__":
  test_heap()
  test_avl()
  test_redblack()
