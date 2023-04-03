import random
names = ["Anu", "Anamika", "Anju", "Manu", "Haritha", "Amayana", "rani"]
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_dictionary = {word: len(word) for word in sentence.split()}
print(words_dictionary)
