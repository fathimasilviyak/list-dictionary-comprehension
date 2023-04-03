student_dict = {
    "student": ["Anu", "Manu", "Anju"],
    "score": [50, 60, 70]
}

# Loop through dictionary
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through dataframe
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Anu":
        print(row.score)
