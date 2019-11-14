#The input is the string to be reversed
#The output is the reverse string

x = ''
def reverse_string(string):
    global x
    for i in range(len(string)):
        x += string[-(i+1)]

    return x
        
        


print(reverse_string('hello I would like to reverse this string'))


