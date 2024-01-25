def calculate_parity_bit(message):
    # Count the number of set bits (1s) in the message
    parity = 0
    for bit in message:
        if bit == "1":
            parity ^= 1  # XOR operation to toggle the parity bit
    # Append the calculated parity bit to the message
    return message + str(parity)


def verify_parity_bit(message_with_parity):
    # Count the number of set bits (1s) in the message (excluding the parity bit)
    data_bits = message_with_parity[:-1]
    parity_bit = message_with_parity[-1]
    parity = 0
    for bit in data_bits:
        if bit == "1":
            parity ^= 1
    # Check if the calculated parity matches the received parity bit
    return parity == int(parity_bit)


# Example usage
message = "1101001"  # 7-bit message
message_with_parity = calculate_parity_bit(message)

print(f"Message with Parity: {message_with_parity}")

# Introduce an error by flipping one bit
corrupted_message = message_with_parity[:3] + "0" + message_with_parity[4:]
print(f"Corrupted Message: {corrupted_message}")

is_correct = verify_parity_bit(corrupted_message)
if is_correct:
    print("Message is correct.")
else:
    print("Message contains errors.")
