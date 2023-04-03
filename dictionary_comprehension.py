import random
names = ["Anu", "Anamika", "Anju", "Manu", "Haritha", "Amayana", "rani"]
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)