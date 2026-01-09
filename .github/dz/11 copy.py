
# №1
# def add_two_numbers():
#     num1= 90
#     num2= 1087
#     total= num1+num2
#     print(total)
# print(add_two_numbers())
# №2
# def add_all_nums (*nums):
#     total = 0 
#     for num in  nums :
#         total += num
#     return total
# print(add_all_nums(90,67,23,78,3423,46,))

# №3
# def add_all_nums (*nums):
#     total = 0 
#     if not nums:
#         return "Помилка"
#     for num in  nums :
#         total += num
#     return total
    
# print(add_all_nums(90,67,23,78,3423,46,))

# №4
# def covert_celcuis_to_far(cel):
#     far=(cel*9/5)+32
#     return far
# print(covert_celcuis_to_far(67))

# №5
# def check_season(month):
#     if month in [1,2,1]:
#         return "winter"
#     elif month  in [3,4,5]:
#         return "spring"
#     elif month in [6,7,8]:
#         return "summer"
#     elif month in [9,10,11]:
#         return "autem"
# print(check_season(8))
# print(check_season(3))    
     
# №6
# def calculate_slope(x1,x_2,y_1,y_2):
#     delta_y = y_1-y_2
#     delta_x = x_1-x_2
#     slope= delta_y/delta_x
#     return slope
# print(calculate_slope(7,2,8,10))

# №7
# import math

# def solve_quadratic_eqn(a,b,c):
#     solve= b**2-4*a*c
#     if solve>0:
#        x1 = (-b + math.sqrt(solve))/(2*a),
#        x2 = (-b - math.sqrt(solve))/(2*a)
#        return {x1,x2}
#     elif solve == 0:
#         x = -b/(2*a)
#         return {x}
#     else:
#         return set()
# print(solve_quadratic_eqn(1,3,60))

# №8
# def  reverse_list(my_list):
#     reverse_list = []
#     for i in range(len(my_list)-1,-1,-1):
#         reverse_list.append(my_list[i])
#     return reverse_list
# print(reverse_list([1, 2, 3, 4, 5]))

# №9
# def reverse_list(my_list):
#     reversed_list = []
#     for i in range(len(my_list)-1, -1, -1):
#         reversed_list.append(my_list[i])

#     return reversed_list
       
# №10
# def  capitalize_list_items(my_list):
#     my_captalize = []
#     for item in my_list:
#         # Додай елемент з великої літери (використай .capitalize())
#         my_captalize.append(item.capitalize())
#     return my_captalize
# print(capitalize_list_items(['apple', 'banana']))

# def capitalize_list_items(my_list):
#     return [item.capitalize() for item in my_list]

# print(capitalize_list_items(['яблуко', 'банан', 'вишня']))

# # №11
# def  add_item(food_staff):
#     food_staff.append('Meat')
#     return food_staff
# print(add_item(['Potato', 'Tomato', 'Mango', 'Milk']))

# def add_item_num(number):
#     number.append(5)
#     return number
# print(add_item_num([2, 3, 7, 9]))
    
    
# №12
# def  remove_item(food_staff):
#     food_staff.remove('Mango')
#     return food_staff
# print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk']))

# №13
# def sum_of_numbers(sum):
#     total=0
#     for i in range (sum+1):
#         total += i
#     return total
# print(sum_of_numbers(5))
# print(sum_of_numbers(10))
# print(sum_of_numbers(100))

# №14
# def  sum_of_odds(odds):
#     total = 0
#     for i in range(odds+1):
#         if i & 1:
#             total += i
#     return total
# print(sum_of_odds(100))


# def sum_of_even(even):
#     total = 0
#     for i in range (even+1):
#         if i % 2 == 0:
#             total += i
#     return total
# print(sum_of_even(100))
    
# def  evens_and_odds(n):
#     evens = 0
#     odds = 0
#     for i in range(n+1):
#         if i & 1:
#             odds +=1
#         else:
#             if i % 2 == 0:
#                 evens +=1
#     print(f"The number of odds are {odds}.")
#     print(f"The number of evens are {evens}.")
# evens_and_odds(100)   
    
# def factor(n):
#     total = 1
#     for i in range(1,n+1):
#         total*=i
#     return total
# print(factor(3))



# def is_empty(parametr):
#     if parametr:
#         return False
#     return True

# def is_empty(parametr):
#     return not parametr
# print(is_empty(()))
# print(is_empty([1, 2]))


# def calculate_mean(n):
#     total =sum(n)
#     coount = len(n)
#     return coount/total
# print(calculate_mean([1,2,4,6,4,3,]))

# def calculate_median(numbers):
#     sorted_nums = sorted(numbers)  # Сортуємо список
#     n = len(sorted_nums)
#     if n % 2 == 0:  # Якщо парна кількість
#         # Беремо два центральні числа і ділимо на 2
#         middle1 = sorted_nums[n//2 - 1]
#         middle2 = sorted_nums[n//2]
#         return (middle1 + middle2) / 2
#     else:  # Якщо непарна
#         return sorted_nums[n//2]  # Беремо центральне число

# # Тест:
# print(calculate_median([1, 2, 3, 4, 5]))     # 3
# print(calculate_median([1, 2, 3, 4, 5, 6]))
        
        

import statistics

def calculate_mode_easy(numbers):
    return statistics.mode(numbers)

print(calculate_mode_easy([1, 2, 2, 3, 4])) # Виведе: 2

def calculate_range(numbers):
    return max(numbers) - min(numbers)

# Тест:
print(calculate_range([1, 2, 3, 4, 5]))  # 5 - 1 = 4