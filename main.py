numbers = [1, 2, 3]

new_numbers = [number+1 for number in numbers]

print(new_numbers)

name = "Anu"
new_name = [letter+"a" for letter in name]
print(new_name)

range_list = [2 * number for number in range(1, 5)]
print(range_list)

names = ["Anu", "Anamika", "Anju", "Manu", "Haritha", "Amayana", "rani"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) >=5]
print(long_names)