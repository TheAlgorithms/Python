import zlib

# Data to compress
data = b"Hello, DEFLATE! This is an example of data compression using the DEFLATE algorithm."

# Compress the data using DEFLATE
compressed_data = zlib.compress(data)

# Decompress the data
decompressed_data = zlib.decompress(compressed_data)

# Output results
print(f"Original Data: {data}")
print(f"Compressed Data: {compressed_data}")
print(f"Decompressed Data: {decompressed_data}")

# Verify the decompressed data matches the original
assert data == decompressed_data, "Decompressed data does not match the original data!"
