class Node:
	def __init__(self, data ):
		self.left = None
		self.right = None
		self.data = data



root = Node(10)

root.left = Node(34)

root.right = Node(89)

# left root right
# left child visited first, followed by parent node, then right child
def inorder(node):
	if node:
		inorder(node.left)
		print(node.data)
		inorder(node.right)

#root left right
# root node is visited fisrt, followed by left right
def preorder(node):
	if node:
		print(node.data)
		inorder(node.left)
		inorder(node.right)
# left right root
def postorder(node):
	if node:
		postorder(node.left)
		postorder(node.right)
		print(node.data)


def find_sum(root):
	if (root ==None):
		return 0
	return root.data + find_sum(root.left) + find_sum(root.right)

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print("Sum of all values of this tree is (should print 20):")
print(find_sum(node2))