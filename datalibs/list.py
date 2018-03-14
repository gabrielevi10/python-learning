class List_node:
	def __init__(self, value, next_node):
		self.value = value
		self.next = next_node

class List:
	def __init__(self, head, size):
		self.head = head
		self.size = size

	def insert(self, value):
		new_node = List_node(value, None)
		if(self.head == None):
			self.head = new_node
		else:
			current_node = head
			while(current_node.next != None):
				current_node = current_node.next
			current_node.next = new_node
		size = size + 1

	def print_list(self)
		current_node = self.head
		while(current_node.next != None)
			print(value)

