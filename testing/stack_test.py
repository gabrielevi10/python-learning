import unittest, sys
sys.path.append('../datalibs')
from stack import Stack

class StackTestCase(unittest.TestCase):
	def test_push_first(self):
		test_stack = Stack(None)
		test_stack.push(2)
		assert(test_stack.first, 2)

	def test_push(self):
		test_stack = Stack(None)
		test_stack.push(3)
		test_stack.push(2)
		test_stack.push(1)
		test_stack.push(0)
		current_node = test_stack.first
		index_test = 3
		while(current_node != None):
			self.assertEqual(current_node.value, index_test)
			index_test = index_test -1
			current_node = current_node.next

	def test_pop(self):

if __name__ == '__main__':
	unittest.main()