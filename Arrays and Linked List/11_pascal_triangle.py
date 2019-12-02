def factorial(num: int) ->int:
    product = 1

    for i in range(1,num+1):
        product = product * i
        
    return product

def combinations(total_num:int, choosen_num:int) -> int:
    return int(factorial(total_num)/ (factorial(choosen_num) *  factorial(total_num - choosen_num)))

def nth_row_pascal(num_row:int) ->list:
    row_result = []
    for i in range(num_row+1):
        row_result.append(combinations(num_row, i))
    return row_result

print(nth_row_pascal(5))