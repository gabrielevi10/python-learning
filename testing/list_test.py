import unittest, sys
sys.path.append('../datalibs')
from list import List

class ListTestCase(unittest.TestCase):
	def test_insert_head(self):
		test_list = List(None, 0)
		test_list.insert(0)
		self.assertEqual(test_list.head.value, 0)

	def test_insert(self):
		test_list = List(None, 0)
		test_list.insert(0, 0)
		test_list.insert(1, 1)
		test_list.insert(2, 2)
		test_list.insert(3, 3)
		current_node = test_list.head
		index_test = 0
		while(current_node != None):
			self.assertEqual(current_node.value, index_test)
			index_test = index_test + 1
			current_node = current_node.next

	def test_insert_any_and_search(self):
		test_list = List(None, 0)
		test_list.insert(0, 0)
		test_list.insert(1, 1)
		test_list.insert(2, 2)
		test_list.insert(3, 3)
		test_list.insert(4, 2)
		self.assertEqual(test_list.search(4), 2)

	def test_remove(self):
		test_list = List(None, 0)
		test_list.insert(0, 0)
		test_list.insert(1, 1)
		test_list.insert(2, 2)
		test_list.insert(3, 3)
		test_list.remove(3)
		self.assertEqual(test_list.search(2), -1)

if __name__ == '__main__':
	unittest.main()