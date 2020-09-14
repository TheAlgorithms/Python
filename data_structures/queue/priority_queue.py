"""
Pure Python implementation of Priority Queue using lists
"""


class FixedPriorityQueue:
	"""
	In a Priority Queue the elements are entred as an when the come
	But while removing or deleting an element the highest priority element is deleted in FIFO fashion
	Here the lowest integer has the highest priority. 
	Example:
	priority(0) > priority(5)
	priority(16) > priority(32)
	Here as an example I have taken only 3 priorities viz. 0, 1, 2 
	0 Being the highest priority and 2 being the lowest
	You can change the priorities as per your need 

	Examples
	>>>FPQ = FixedPriorityQueue()
	>>>FPQ.enqueue(0, 10)
	>>>FPQ.enqueue(1, 70)
	>>>FPQ.enqueue(0, 100)
	>>>FPQ.enqueue(2, 1)
	>>>FPQ.enqueue(2, 5)
	>>>FPQ.enqueue(1, 7)
	>>>FPQ.enqueue(2, 4)
	>>>FPQ.enqueue(1, 64)
	>>>FPQ.enqueue(0, 128)
	>>>FPQ.print_queue()
	Priority 0: [10, 100, 128]
	Priority 1: [70, 7, 64]
	Priority 2: [1, 5, 4]
	>>>print(FPQ.dequeue())
	10
	>>>print(FPQ.dequeue())
	100
	>>>print(FPQ.dequeue())
	128
	>>>print(FPQ.dequeue())
	70
	>>>print(FPQ.dequeue())
	7
	>>>FPQ.print_queue()
	Priority 0: []
	Priority 1: [64]
	Priority 2: [1, 5, 4]
	>>>print(FPQ.dequeue())
	64
	>>>print(FPQ.dequeue())
	1
	>>>print(FPQ.dequeue())
	5
	>>>print(FPQ.dequeue())
	4
	>>>print(FPQ.dequeue())
	Traceback (most recent call last):
	  File "Sample.py", line 117, in <module>
		print(FPQ.dequeue())
	  File "Sample.py", line 58, in dequeue
		raise Exception("Under Flow!")
	Exception: Under Flow!
	"""

	def __init__(self) -> None:
		self.queue = [
			[],
			[],
			[],
		]

	def enqueue(self, priority: int, data: int) -> None:
		"""
		This function enters the element into the FixedPriorityQueue based on its priority
		If the priority is invalid an Exception is raised saying Invalid Priority!
		If the FixedPriorityQueue is full an Exception is raised saying Over Flow!
		"""
		if priority > 2:
			raise Exception("Invalid Priority!")
		elif len(self.queue[priority]) == 100:
			raise Exception("Over Flow!")
		else:
			self.queue[priority].append(data)

	def dequeue(self) -> int:
		"""
		This function returns the highest priority element from the FixedPriorityQueue in FIFO fashion
		If the FixedPriorityQueue is empty and this function is called then an exception is raised saying Under Flow!
		"""
		if (
			len(self.queue[0]) == 0
			and len(self.queue[1]) == 0
			and len(self.queue[2]) == 0
		):
			raise Exception("Under Flow!")

		if len(self.queue[0]) != 0:
			return self.queue[0].pop(0)
		elif len(self.queue[1]) != 0:
			return self.queue[1].pop(0)
		else:
			return self.queue[2].pop(0)

	def print_queue(self) -> None:
		"""
		Prints each priority queue within the FixedPriorityQueue
		"""
		print("Priority 0:", self.queue[0])
		print("Priority 1:", self.queue[1])
		print("Priority 2:", self.queue[2])


class ElementPriorityQueue:
	"""
	Element Priority Queue is the same as Fixed Priority Queue
	The only difference being the value of the element itself is the priority
	The rule for priorities are the same
	The lowest integer has the highest priority. 
	Example:
	priority(0) > priority(5)
	priority(16) > priority(32)
	You can change the priorities as per your need

	>>>EPQ = ElementPriorityQueue()
	>>>EPQ.enqueue(10)
	>>>EPQ.enqueue(70)
	>>>EPQ.enqueue(100)
	>>>EPQ.enqueue(1)
	>>>EPQ.enqueue(5)
	>>>EPQ.enqueue(7)
	>>>EPQ.enqueue(4)
	>>>EPQ.enqueue(64)
	>>>EPQ.enqueue(128)
	>>>EPQ.print_queue()
	[10, 70, 100, 1, 5, 7, 4, 64, 128]
	>>>print(EPQ.dequeue())
	1
	>>>print(EPQ.dequeue())
	4
	>>>print(EPQ.dequeue())
	5
	>>>print(EPQ.dequeue())
	7
	>>>print(EPQ.dequeue())
	10
	>>>EPQ.print_queue()
	[70, 100, 64, 128]
	>>>print(EPQ.dequeue())
	64
	>>>print(EPQ.dequeue())
	70
	>>>print(EPQ.dequeue())
	100
	>>>print(EPQ.dequeue())
	128
	>>>print(EPQ.dequeue())
	Traceback (most recent call last):
    File "Sample.py", line 132, in <module>
    print(EPQ.dequeue())
    File "Sample.py", line 100, in dequeue
    raise Exception("Under Flow!")
	Exception: Under Flow!
	"""

	def __init__(self) -> None:
		self.queue = []

	def enqueue(self, data: int) -> None:
		'''
		This function enters the element into the ElementPriorityQueue based on its value
		If the ElementPriorityQueue is full an Exception is raised saying Over Flow!
		'''
		if len(self.queue) == 100:
			raise Exception("Over Flow!")
		else:
			self.queue.append(data)

	def dequeue(self) -> int:
		'''
		This function returns the highest priority element from the ElementPriorityQueue in FIFO fashion.
		If the ElementPriorityQueue is empty and this function is called then an exception is raised saying Under Flow!
		'''
		if len(self.queue) == 0:
			raise Exception("Under Flow!")
		else:
			data = min(self.queue)
			self.queue.remove(data)
			return data

	def print_queue(self) -> None:
		'''
		Prints all the elements within the Element Priority Queue
		'''
		print(self.queue)


def fixed_priority_queue() -> None:
	FPQ = FixedPriorityQueue()
	FPQ.enqueue(0, 10)
	FPQ.enqueue(1, 70)
	FPQ.enqueue(0, 100)
	FPQ.enqueue(2, 1)
	FPQ.enqueue(2, 5)
	FPQ.enqueue(1, 7)
	FPQ.enqueue(2, 4)
	FPQ.enqueue(1, 64)
	FPQ.enqueue(0, 128)
	FPQ.print_queue()
	print(FPQ.dequeue())
	print(FPQ.dequeue())
	print(FPQ.dequeue())
	print(FPQ.dequeue())
	print(FPQ.dequeue())
	FPQ.print_queue()
	print(FPQ.dequeue())
	print(FPQ.dequeue())
	print(FPQ.dequeue())
	print(FPQ.dequeue())
	print(FPQ.dequeue())


def element_priority_queue() -> None:
	EPQ = ElementPriorityQueue()
	EPQ.enqueue(10)
	EPQ.enqueue(70)
	EPQ.enqueue(100)
	EPQ.enqueue(1)
	EPQ.enqueue(5)
	EPQ.enqueue(7)
	EPQ.enqueue(4)
	EPQ.enqueue(64)
	EPQ.enqueue(128)
	EPQ.print_queue()
	print(EPQ.dequeue())
	print(EPQ.dequeue())
	print(EPQ.dequeue())
	print(EPQ.dequeue())
	print(EPQ.dequeue())
	EPQ.print_queue()
	print(EPQ.dequeue())
	print(EPQ.dequeue())
	print(EPQ.dequeue())
	print(EPQ.dequeue())
	print(EPQ.dequeue())



if __name__ == "__main__":
	fixed_priority_queue()
	element_priority_queue()
