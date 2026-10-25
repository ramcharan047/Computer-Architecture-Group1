# Question 1: Signed Binary Arithmetic using 8-bit 2's Complement

def to_8bit_binary(number):
    """Return the 8-bit two's complement representation of a number."""
    return format(number & 0xFF, "08b")


def binary_addition(first, second):
    """Add two 8-bit binary strings and return result and carry-out."""
    carry = 0
    result = ""

    for index in range(7, -1, -1):
        total = int(first[index]) + int(second[index]) + carry
        result = str(total % 2) + result
        carry = total // 2

    return result, carry


def binary_to_signed_decimal(binary):
    """Convert an 8-bit two's complement string to signed decimal."""
    value = int(binary, 2)
    if binary[0] == "1":
        value -= 256
    return value


def perform_addition(number1, number2):
    binary1 = to_8bit_binary(number1)
    binary2 = to_8bit_binary(number2)

    result, carry_out = binary_addition(binary1, binary2)
    decimal_result = binary_to_signed_decimal(result)

    # Signed overflow: same-sign operands produce an opposite-sign result.
    overflow = (
        (number1 >= 0) == (number2 >= 0)
        and (decimal_result >= 0) != (number1 >= 0)
    )

    print("Operand 1:", number1, "=", binary1)
    print("Operand 2:", number2, "=", binary2)
    print("\nBinary addition:")
    print(" ", binary1)
    print("+", binary2)
    print("-----------")
    print(" ", result)
    print("Carry out:", carry_out)
    print("Final result (binary):", result)
    print("Final result (decimal):", decimal_result)
    print("Arithmetic overflow:", "Yes" if overflow else "No")


print("SIGNED BINARY ARITHMETIC USING 8-BIT 2'S COMPLEMENT")

print("\n(a) 25 + (+18)")
perform_addition(25, 18)

print("\n(b) (-25) + (-18)")
perform_addition(-25, -18)
