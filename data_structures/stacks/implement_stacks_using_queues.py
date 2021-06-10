from queue import Queue

class Stack:
	
	def __init__(self):
		
		# Two inbuilt queues
		self.q1 = Queue()
		self.q2 = Queue()
			
		# To maintain current number
		# of elements
		self.curr_size = 0

	def push(self, x):
		self.curr_size += 1

		# Push x first in empty q2
		self.q2.put(x)

		# Push all the remaining
		# elements in q1 to q2.
		while (not self.q1.empty()):
			self.q2.put(self.q1.queue[0])
			self.q1.get()

		# swap the names of two queues
		self.q = self.q1
		self.q1 = self.q2
		self.q2 = self.q

	def pop(self):

		# if no elements are there in q1
		if (self.q1.empty()):
			return
		self.q1.get()
		self.curr_size -= 1

	def top(self):
		if (self.q1.empty()):
			return -1
		return self.q1.queue[0]

	def size(self):
		return self.curr_size

# Main Code
if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)

	print("current size: ", s.size())
	print(s.top())
	s.pop()
	print(s.top())
	s.pop()
	print(s.top())

	print("current size: ", s.size())
