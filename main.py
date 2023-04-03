numbers = [1, 2, 3]

new_numbers = [number+1 for number in numbers]

print(new_numbers)

name = "Anu"
new_name = [letter+"a" for letter in name]
print(new_name)

range_list = [2 * number for number in range(1, 5)]
print(range_list)