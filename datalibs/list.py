class List_node:
	def __init__(self, value, next_node):
		self.value = value
		self.next = next_node

class List:
	def __init__(self, head, size):
		self.head = head
		self.size = size

	def insert(self, value, position = 0):
		if(self.head == None):
			self.head = List_node(value, None)
			self.last = List_node(value, None)
		elif(position != 0):
			current_node = self.head
			current_index = 1
			while(current_index != position and current_node.next != None):
				current_node = current_node.next
				current_index = current_index + 1
			current_node.next = List_node(value, current_node.next)
			self.size = self.size + 1
		
	def remove(self, position):
		if(position != None  and  self.head != None  and  self.size != 0):	
			if(position == "head"):
				current_node = self.head.next
				self.head = current_node
			if(position == "last"):
				current_node = self.head
				while(current_node.next != self.last):
					current_node = current_node.next
				last = current_node
			if(position <= self.size):
				current_node = self.head
				index = 1
				while(index != position - 1 and current_node.next != None):
					index = index + 1
					current_node = current_node.next
				current_node.next = current_node.next.next
		self.size = self.size - 1


	def search(self, value):
		if(self.head != None  and  self.size != 0):
			current_node = self.head
			flag = False
			position = 0
			while(current_node != None and not flag):
				if(current_node.value == value):
					flag = True
					break
				current_node = current_node.next
				position = position + 1
			if(not flag):
				position = -1
			return position

	def print_list(self):
		current_node = self.head
		while(current_node != None):
			print(current_node.value)
			current_node = current_node.next

