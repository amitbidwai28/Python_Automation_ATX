def digits_from_even_positions(input_string):
    result = []
    for index in range(0, len(input_string), 2):
        if input_string[index].isdigit():
            result.append(input_string[index])
    return ''.join(result)


# Example usage:
input_str = "1a2b3c4d5e6f"
result_digits = digits_from_even_positions(input_str)
print("Digits from even positions:", result_digits)

# ---------------------------------------------------------------

number = "8976549"
for index in range(0, len(number)):
    if index % 2 != 0 and index != 0:
        print("Value:", number[index], "at this location:", index)
