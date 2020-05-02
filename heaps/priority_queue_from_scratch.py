# class node with data and priority queue

class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority


# class for priority queue

class PriorityQueue:
    def __init__(self):
        self.queue = list()

    def insert(self,node):
        if self.size() == 0:
            self.queue.append(node)
        else:
            # traverse the queue and find the right place for the element
            for i in range(0,self.size()):
                # if the priority of the new node is greater
                if node.priority > self.queue[i].priority:
                    # if we have traversed the complete queue

                    if i == self.size() - 1:
                        self.queue.insert(i + 1,node)
                    else:
                        continue
                else:
                    self.queue.insert(i,node)
                    return True

    
    def size(self):
        return len(self.queue)

    def delete(self):
        # remove first node from the queue
        return self.queue.pop(0)

    def show(self):
        for i in self.queue:
            print(str(i.data) + " " + str(i.priority))


"""
class Node:
	def __init__(self,data,priority):
		self.data = data
		self.priority = priority

class PriorityQueue:
	def __init__(self):
		self.queue = list()

	def size(self):
		return len(self.queue)

	def insert(self,node):
		if self.size() == 0:
			self.queue.append(node)

		else:
			for i in range(0,self.size()):
				if node.priority > self.queue[i].priority:
					if i == self.size() - 1:
						self.queue.insert(i + 1,node)
					else:
						self.queue.insert(i,node)
						return True

	def delete(self):
		return self.queue.pop(0)

	def show(self):
		for i in range(0,self.size()):
			print(str(i.data) + " " + str(i.priority))
"""