class Stack_node:
	def __init__(self, value, next_node):
		self.value = value
		self.next = next_node

class Stack:
	def __init__(self, first):
		self.first = first

	def push(self, value):
		if(self.first == None):
			self.first = Stack_node(value, None)
		else:
			aux = self.first
			self.first = Stack_node(value, aux)

	def pop(self):
		if(self.first == None):
			raise Exception("Stack is empty !!!")
		else:
			aux = self.first
			self.first = self.first.next
			return aux.value

	def search(self, value):
		if(self.first != None):
			current_node = self.first
			while(current_node.next != None):
				if(current_node.value == value):
					return True
				else:
					current_node = current_node.next
		return False

	def print_stack(self):
		current_node = self.first
		while(current_node.next != None)
			print(current_node.value)
			current_node = current_node.next
