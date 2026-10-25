# Question 2: Logical Shift Operations on 8-bit Binary Numbers

def logical_left_shift(binary, positions):
    print("\nLogical Left Shift")
    print("Original 8-bit number:", binary)

    for step in range(1, positions + 1):
        # Discard the leftmost bit and add 0 at the right.
        binary = binary[1:] + "0"
        print("After shift", step, ":", binary)

    print("Final 8-bit result:", binary)


def logical_right_shift(binary, positions):
    print("\nLogical Right Shift")
    print("Original 8-bit number:", binary)

    for step in range(1, positions + 1):
        # Add 0 at the left and discard the rightmost bit.
        binary = "0" + binary[:-1]
        print("After shift", step, ":", binary)

    print("Final 8-bit result:", binary)


print("LOGICAL SHIFT OPERATIONS ON 8-BIT BINARY NUMBERS")

print("\n(a) Logical left shift of 10110110 by 2 positions")
logical_left_shift("10110110", 2)

print("\n(b) Logical right shift of 11010100 by 2 positions")
logical_right_shift("11010100", 2)
