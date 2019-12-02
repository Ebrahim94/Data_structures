# sum all the values in a given list
def sum_list(input_list: list) -> int:
    result = 0
    for i in input_list:
        result += i
    
    return result


#given a list generate all possible combinations
def sublist_generator(input_list: list) -> list:
    list_of_lists = []
    list_max_pos = len(input_list)+1

    for initial_pos in range(list_max_pos):
        for final_pos in range (initial_pos+1, list_max_pos):
            list_of_lists.append(input_list[initial_pos: final_pos])
    return list_of_lists



for i in range(4,4):
    print(i)


#The maximum sum of an array
def max_sum(input_list: list) -> int:
    max_val = -float('inf')
    list_of_lists = sublist_generator(input_list)

    for l in list_of_lists:
        list_added = sum_list(l)
        if list_added > max_val:
            max_val = list_added

    return max_val


print(max_sum([1,2,-5,-4,1,6]))