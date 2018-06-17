from binarytree import Node

class BinaryNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def make_print_tree(root):
  if root is None: return root
  print_root = Node(root.value)
  print_root.left = make_print_tree(root.left)
  print_root.right = make_print_tree(root.right)
  return print_root


if __name__ == "__main__":
  root = BinaryNode(5)
  root.left = BinaryNode(3)
  root.right = BinaryNode(7)
  root.right.right = BinaryNode(10)
  root.right.right.left = BinaryNode(9)
  root = make_print_tree(root)
  print(root)
