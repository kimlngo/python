print('========================================')
print('LEVEL 2 PROBLEMS')
print('Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.')
""" 
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
 """

def has_33(num_list):
    for idx in range(0, len(num_list) - 1):
        if num_list[idx] == 3 and num_list[idx + 1] == 3:
            return True
        
    return False

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))
print(has_33([2,1,5,3,3,1,3]))

print('========================================')
print('PAPER DOLL: Given a string, return a string where for every character in the original there are three characters')
""" 
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
 """

def paper_doll(str):
    output = ''
    for letter in str:
        output += letter * 3
    
    return output

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


print('========================================')
print("BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'")
""" 
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19 
"""
def blackjack(a,b,c):
    num_list = [a,b,c]
    total = sum(num_list)

    if total <= 21:
        return total
    else:
        if 11 in num_list:
            total -= 10

        if total <= 21:
            return total
        else:
            return 'BUST'

print(blackjack(5,6,7)) # 18
print(blackjack(9,9,9)) # 'BUST'
print(blackjack(9,9,11)) # 19 


print('========================================')
print("SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.")

def sum_69(arr):
    total = 0
    is_in_range = False

    for num in arr:
        if is_in_range and num != 9:
            continue

        if num == 6:
            is_in_range = True
            continue
        elif num == 9:
            is_in_range = False
            continue
        else:
            total += num
        
    return total

print(sum_69([1, 3, 5]))
print(sum_69([4, 5, 6, 6, 9, 8]))
print(sum_69([2, 1, 6, 9, 11]))