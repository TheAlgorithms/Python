class CABAC:
    def __init__(self):
        self.low     = 0
        self.high    = (1 << 32) - 1
        self.context = [0.5] * 256 # probability model for 256 contexts

    def _update_context(self, ctx, bit):
        # Simple adaptation: move probability toward observed bit
        alpha = 0.05
        self.context[ctx] = (1 - alpha) * self.context[ctx] + alpha * bit

    def encode_bit(self, bit, ctx, output):
        prob   = self.context[ctx]
        range_ = self.high - self.low + 1
        split  = self.low  + int(range_ * prob)

        if bit == 0:
            self.high = split
        else:
            self.low  = split + 1

        while (self.high ^ self.low) < (1 << 24):
            output.append((self.high >> 24) & 0xFF)
            self.low  =  (self.low   << 8)  & 0xFFFFFFFF
            self.high =  ((self.high << 8)  & 0xFFFFFFFF) | 0xFF

        self._update_context(ctx, bit)

    def finish_encoding(self, output):
        for _ in range(4):
            output.append((self.low >> 24) & 0xFF)
            self.low =    (self.low << 8)  & 0xFFFFFFFF

    def decode_bit(self, ctx, input_bits):
        prob   = self.context[ctx]
        range_ = self.high - self.low + 1
        split  = self.low  + int(range_ * prob)

        if self.code <= split:
            self.high = split
            bit = 0
        else:
            self.low = split + 1
            bit = 1

        while (self.high ^ self.low) < (1 << 24):
            self.code = ((self.code << 8) & 0xFFFFFFFF) | next(input_bits)
            self.low  = (self.low   << 8) & 0xFFFFFFFF
            self.high = ((self.high << 8) & 0xFFFFFFFF) | 0xFF

        self._update_context(ctx, bit)
        return bit

    def start_decoding(self, encoded_bytes):
        self.low = 0
        self.high = (1 << 32) - 1
        self.code = 0
        input_bits = iter(encoded_bytes)
        for _ in range(4):
            self.code = (self.code << 8) | next(input_bits)
        return input_bits


def string_to_bits(s):
    return [(byte >> i) & 1 for byte in s.encode('utf-8') for i in range(7, -1, -1)]

def bits_to_string(bits):
    b = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        b.append(byte)
    return b.decode('utf-8')

def main(text: str):
    encoder = CABAC()
    output_bytes = []
    bits = string_to_bits(text)

    for i, bit in enumerate(bits):
        ctx = i % 256 # simple positional context
        encoder.encode_bit(bit, ctx, output_bytes)
    encoder.finish_encoding(output_bytes)

    # Decode
    decoder = CABAC()
    bitstream = decoder.start_decoding(iter(output_bytes))
    decoded_bits = [decoder.decode_bit(i % 256, bitstream) for i in range(len(bits))]
    decoded_text = bits_to_string(decoded_bits)

    print("Original:", text)
    print("Decoded :", decoded_text)
    print("Compressed size (bytes):", len(output_bytes))

if __name__ == "__main__":
    # Example usage
    main("Hello CABAC!")
