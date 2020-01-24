#permutations
def permutations(l):
    if len(l) <= 1:
        return [l]
    
    elif len(l) == 2:
        return [l, l[::-1]]
    
    else:
        output = []
        current = l[0]
        prev = permutations(l[1:])

        for element in prev:
            for pos in range(len(element) + 1):
                temp_list = []
                temp_element = element.copy()
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list.append(current)
                    else:
                        temp_list.append(temp_element.pop())
                output.append(temp_list)
        
        return output

print(permutations([7,8,9,10,11]))