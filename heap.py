

def make_max_heap(vals):
  """ vals must be an array of (key, value) pairs where the key is used in comparisons """
  heap = [(-1, -1)] + vals
  N = len(heap) - 1
  for i in reversed(range(1, N//2 + 1)):
    _sink(heap, i)
  return heap


def insert(heap, item):
  """ item must be a (key, value) tuple """
  heap.append(item)
  _swim(heap, len(heap)-1)


def remove_max(heap):
  heap[1], heap[len(heap)-1] = heap[len(heap)-1], heap[1]
  _, max_value = heap.pop()
  _sink(heap, 1)
  return max_value


def _sink(heap, i):
  N = len(heap) - 1
  while 2*i <= N:
    larger = 2 * i
    if larger < N and heap[larger] < heap[larger+1]: larger += 1
    if heap[i] >= heap[larger]: break
    heap[i], heap[larger] = heap[larger], heap[i]
    i = larger

def _swim(heap, i):
  while i > 0 and heap[i] > heap[i//2]:
    heap[i], heap[i//2] = heap[i//2], heap[i]
    i = i // 2



if __name__ == "__main__":
  heap = make_max_heap([(2, 2), (5, 5), (3, 3), (1, 1), (7, 7), (4, 4)])
  print(heap)