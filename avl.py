from bst import find
# from tree import make_print_tree
from random import randint


class Node:
  def __init__(self, value, height):
    self.value = value
    self.height = height
    self.left = None
    self.right = None
  
  def __str__(self):
    return str(self.value)


########################################################################
# BST functions
########################################################################

def find(root, value):
  if root is None: return None
  
  if root.value > value:
    return find(root.left, value)
  if root.value < value:
    return find(root.right, value)
  return root

########################################################################
# AVL tree functions
########################################################################

def make_avl_tree(vals):
  root = None
  for value in vals:
    root = avl_insert(root, value)
  return root

def avl_insert(root, value):
  if root is None: return Node(value, 0)
  
  if value < root.value:
    root.left = avl_insert(root.left, value)
    # we just inserted something in left so check if unbalanced
    if height(root.left) > height(root.right) + 1:
      root = _rebalance_right(root)
  elif value > root.value:
    root.right = avl_insert(root.right, value)
    # we just inserted something in right so check if unbalanced
    if height(root.right) > height(root.left) + 1:
      root = _rebalance_left(root)
  
  root.height = 1 + max(height(root.left), height(root.right))
  return root


def height(node):
  return node.height if node else -1


def _rebalance_left(node):
  root, right = node, node.right
  if height(right.left) > height(right.right):
    root.right = _rotate_right(right)
  root = _rotate_left(node)
  return root

def _rebalance_right(node):
  root, left = node, node.left
  if height(left.right) > height(left.left):
    root.left = _rotate_left(left)
  root = _rotate_right(node)
  return root

def _rotate_left(node):
  root = node.right
  node.right = root.left
  root.left = node
  root.left.height = 1 + max(height(root.left.left), height(root.left.right))
  root.height = 1 + max(height(root.left), height(root.right))
  return root

def _rotate_right(node):
  root = node.left
  node.left = root.right
  root.right = node
  root.right.height = 1 + max(height(root.right.left), height(root.right.right))
  root.height = 1 + max(height(root.left), height(root.right))
  return root


if __name__ == "__main__":
  root = None
  vals = [randint(0, 100) for _ in range(50)]
  for value in vals:
    root = avl_insert(root, value)
    print(make_print_tree(root))