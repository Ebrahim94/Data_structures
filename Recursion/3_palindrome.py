def is_palindrome(input):
    if len(input) <= 1:
        return True
    elif len(input) == 2:
        return input[0] == input[1]
    else:
        output = (input[0] == input[-1]) & is_palindrome(input[1: -1])
    
    return output

test = ['wow', 'how', 'aa', 'b', 'this', 'dad', 'maam', 'madam']

for element in test:
    print('palindrome' if is_palindrome(element) else 'not palindrome')
