class BSTNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def make_tree(tree):
  if tree == []: return None

  value, left, right = tree
  root = BSTNode(value)
  root.left = make_tree(left)
  root.right = make_tree(right)
  return root

def print_bst(root, level=0):
  if root is None: return
  print("--" * level + str(root.value))
  print_bst(root.left, level + 1)
  print_bst(root.right, level + 1)
