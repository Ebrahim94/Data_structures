def reverse_string(input):
    if len(input) <= 1:
        return input
    return reverse_string(input[1:]) + input[0]

print(reverse_string('bed'))