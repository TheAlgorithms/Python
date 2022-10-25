class Program():
    def __init__(self, value):
        self.value = value
 
    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Program):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Program")
 
    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Program):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Program")
 
    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Program):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Program")
 
    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Program):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Program")
 
    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Program):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Program")
 
    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value
 
 
# Driver's code
if __name__ == "__main__":
    a = Program(10)
    b = Program(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)
