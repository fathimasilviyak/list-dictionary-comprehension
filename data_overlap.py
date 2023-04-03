with open("file1.txt") as file1:
    file1_list = file1.readlines()

with open("file2.txt") as file2:
    file2_list = file2.readlines()

overlapped_data = [int(number) for number in file1_list if number in file2_list]
print(overlapped_data)