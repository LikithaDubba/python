class TreeNode:
   def __init__(self,data):
      self.data=data
      self.left=None
      self.right=None

def createbst(root,val):
    if root is None:
      return TreeNode(val)
    if val<root.data:
      root.left=createbst(root.left,val)
    elif val>root.data:
       root.right=createbst(root.right,val)
    return root
def preorder(root):
   if root:
      print(root.data,end="")
      preorder(root.left)
      preorder(root.right)

def inorder(root):
   if root:
      inorder(root.left)
      print(root.data,end="")
      inorder(root.right)

def postorder(root):
   if root:
      postorder(root.left)
      postorder(root.right)
      print(root.data,end="")

def search (root,ele):
   if root is None:
      return False
   if root.data==ele:
      return True
   elif ele>root.data:
      return search(root.left,ele)
   else:
      return search(root.right,ele)
   
def find_max(root):
   if root is None:
      return None
   while root.right:
      root=root.right
   return root.data

def find_min(root):
   if root is None:
      return None

def delete_node(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left=delete_node(root.left,key)
    elif key>root.data:
        root.right=delete_node(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp=find_min(root.right)
        root.data=temp.data
        root.right=delete_node(root.right,temp.data)

        return root
      
arr=[8,3,10,1,6,14,4,7]
root=TreeNode(arr[0])
for val in arr:
   root=createbst(root,val)

print("preorder traversal:",end="")
preorder(root)
print("\nInorder traversal:",end="")
inorder(root)
print("\npostorder traversal:",end="")
postorder(root)

print(f"\n\nsearch 10:{search(root,10)}")
