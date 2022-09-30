# declaring byte value
byte_val = b'\x00\x01'
# converting to int
# byteorder is big where MSB is at start
int_val = int.from_bytes(byte_val, "big")
# printing int equivalent
print(int_val)
