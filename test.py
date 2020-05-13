class DoubleLinkedNode:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None

class lru_cache:
	def __init__(self,capacity):
		self.capacity = capacity
		self.head_node = DoubleLinkedNode(0,0)
		self.tail_node = DoubleLinkedNode(0,0)
		self.head_node.next = self.tail_node
		self.tail_node.prev = self.head_node
		self.hashmap = {}

	def remove_node(self,node):
		n=node.prev
		m=node.next
		n.next = m
		m.prev = n
		
	def insert_node(self,node):
		node.prev = self.head_node
		node.next = self.head_node.next
		node.prev.next = node
		  

	def move_head(self,node):
		self.remove_node(node)
		self.insert_node(node)


	def get(self,key):
		if key not in self.hashmap:
			return None
		else:
			result = self.hashmap[key].value	
			self.move_head(self.hashmap[key])
			return result


	def put(self, key, value):
			if key in self.hashmap:
				self.move_head(self.hashmap[key])
				value =  self.hashmap[key].value
			else:
				node = DoubleLinkedNode(key,value)
				self.hashmap[key] = node
				self.insert_node(self.hashmap[key])

				if len(self.hashmap)>self.capacity:
					del self.hashmap[self.tail_node.prev.key]
					self.remove_node(self.tail_node.prev)

			


    






