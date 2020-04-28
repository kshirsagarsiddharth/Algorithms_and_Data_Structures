# Python3 program to find number 
# of siblings of a given node 
from queue import Queue 

# Represents a node of an n-ary tree 
class newNode: 
	def __init__(self,data): 
		self.child = [] 
		self.key = data 

# Function to calculate number 
# of siblings of a given node 
def numberOfSiblings(root, x): 
	if (root == None): 
		return 0

	# Creating a queue and 
	# pushing the root 
	q = Queue() 
	q.put(root) 

	while (not q.empty()): 
		
		# Dequeue an item from queue and 
		# check if it is equal to x If YES, 
		# then return number of children 
		p = q.queue[0] 
		q.get() 

		# Enqueue all children of 
		# the dequeued item 
		for i in range(len(p.child)): 
			
			# If the value of children 
			# is equal to x, then return 
			# the number of siblings 
			if (p.child[i].key == x): 
				return len(p.child) - 1
			q.put(p.child[i]) 

# Driver Code 
if __name__ == '__main__': 

	# Creating a generic tree as 
	# shown in above figure 
	root = newNode(50) 
	(root.child).append(newNode(2)) 
	(root.child).append(newNode(30)) 
	(root.child).append(newNode(14)) 
	(root.child).append(newNode(60)) 
	(root.child[0].child).append(newNode(15)) 
	(root.child[0].child).append(newNode(25)) 
	(root.child[0].child[1].child).append(newNode(70)) 
	(root.child[0].child[1].child).append(newNode(100)) 
	(root.child[1].child).append(newNode(6)) 
	(root.child[1].child).append(newNode(1)) 
	(root.child[2].child).append(newNode(7)) 
	(root.child[2].child[0].child).append(newNode(17)) 
	(root.child[2].child[0].child).append(newNode(99)) 
	(root.child[2].child[0].child).append(newNode(27)) 
	(root.child[3].child).append(newNode(16)) 

	# Node whose number of 
	# siblings is to be calculated 
	x = 100

	# Function calling 
	print(numberOfSiblings(root, x)) 

# This code is contributed by PranchalK 
