"""
Python program for operator overloading

"""


class Vikash():
	def __init__(self, value):
		self.value = value

	def __and__(self, obj):
		print("And operator overloaded")
		if isinstance(obj, Vikash):
			return self.value & obj.value
		else:
			raise ValueError("Must be a object of class Vikash")

	def __or__(self, obj):
		print("Or operator overloaded")
		if isinstance(obj, Vikash):
			return self.value | obj.value
		else:
			raise ValueError("Must be a object of class Vikash")

	def __xor__(self, obj):
		print("Xor operator overloaded")
		if isinstance(obj, Vikash):
			return self.value ^ obj.value
		else:
			raise ValueError("Must be a object of class Vikash")

	def __lshift__(self, obj):
		print("lshift operator overloaded")
		if isinstance(obj, Vikash):
			return self.value << obj.value
		else:
			raise ValueError("Must be a object of class Vikash")

	def __rshift__(self, obj):
		print("rshift operator overloaded")
		if isinstance(obj, Vikash):
			return self.value & obj.value
		else:
			raise ValueError("Must be a object of class Vikash")

	def __invert__(self):
		print("Invert operator overloaded")
		return ~self.value


# Driver's code
if __name__ == "__main__":
	a = Vikash(int(input("Enter A")))
	b = Vikash(int(input("Enter B")))
	print(a & b)
	print(a | b)
	print(a ^ b)
	print(a << b)
	print(a >> b)
	print(~a)
