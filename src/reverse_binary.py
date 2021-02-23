def csReverseIntegerBits(n):
    input_bin = bin(n)
    original_bin = str(input_bin)
    original_bin_length = len(original_bin)  # calculate length of the list
    sliced_bin = original_bin[original_bin_length:1:-1]  # slicing

    decimal = 0
    for digit in sliced_bin:
        decimal = decimal * 2 + int(digit)
    return decimal
n = 417

print(csReverseIntegerBits(n))