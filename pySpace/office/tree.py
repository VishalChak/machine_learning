# https://www.onlinegdb.com/ editer
class node:
  def __init__(self):
    self.left = None
    self.right = None
    self.data = None
def insert(root, temp):
  if root.data <= temp.data:
    if root.right ==None:
      root.right = temp
    else:
      insert(root.right, temp)
  else:
    if root.left == None:
      root.left = temp
    else:
      insert(root.left, temp)

def print_tree(root):
  if root != None:
    print_tree(root.left)
    print(root.data)
    print(root.right)


choice = 0 
root = None
while choice < 3 :
  print("1 for insertion\n2 for print")
  choice = int(input())
  if choice ==1:
    temp = node()
    temp.data = int(input())
    if root == None:
      root = temp
    else:
      insert(root, temp)
  elif choice ==2:
    print_tree(root)