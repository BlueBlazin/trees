
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def make_bst(vals):
  root = None
  for val in vals:
    root = insert(root, val)
  return root

########################################################################
# Insert & Find
########################################################################

def insert(root, value):
  if root is None: return Node(value)
  
  if root.value > value:
    root.left = insert(root.left, value)
  elif root.value < value:
    root.right = insert(root.right, value)
  return root


def find(root, value):
  if root is None: return None
  
  if root.value > value:
    return find(root.left, value)
  if root.value < value:
    return find(root.right, value)
  return root.value


########################################################################
# Delete
########################################################################

def delete(root, value):
  if root is None: return None
  
  if   value < root.value: root.left = delete(root.left, value)
  elif value > root.value: root.right = delete(root.right, value)
  else:
    if root.left is None: return root.right
    tmp = root
    root = get_max(root.left)
    root.left = del_max(tmp.left)
    root.right = tmp.right
  return root

def get_max(root):
  if root.right is None: return root
  return get_max(root.right)

def del_max(root):
  if root.right is None: return root.left
  root.right = del_max(root.right)
  return root



if __name__ == "__main__":
  root = make_bst([1, 4, 2, 3, 5, 7])
  print(find(root, 5))
  delete(root, 5)
  print(find(root, 5))