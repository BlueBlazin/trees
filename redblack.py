from bst import find
from tree import make_print_tree
from random import randint

class Node:
  def __init__(self, value, color):
    self.value = value
    self.left = None
    self.right = None
    self.color = color

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
# Red-Black functions
########################################################################

def make_rb_tree(vals):
  root = None
  for value in vals:
    root = rb_insert(root, value)
    root.color = "BLACK"
  return root


def rb_insert(root, value):
  if root is None: return Node(value, "RED")
  
  if value < root.value: 
    root.left = rb_insert(root.left, value)
  elif value > root.value:
    root.right = rb_insert(root.right, value)
  
  if is_red(root.right) and not is_red(root.left): root = _rotate_left(root)
  if is_red(root.left) and is_red(root.left.left): root = _rotate_right(root)
  if is_red(root.left) and is_red(root.right): _flip_colors(root)

  return root


def is_red(node):
  return node.color == "RED" if node else False


def _flip_colors(node):
  node.left.color = node.right.color = "BLACK"
  node.color = "RED"

def _rotate_left(node):
  root = node.right
  node.right = root.left
  root.left = node
  root.color = node.color
  node.color = "RED"
  return root

def _rotate_right(node):
  root = node.left
  node.left = root.right
  root.right = node
  root.color = node.color
  node.color = "RED"
  return root


if __name__ == "__main__":
  vals = [randint(0, 99) for _ in range(15)]
  root = make_rb_tree(vals)
  print(make_print_tree(root))