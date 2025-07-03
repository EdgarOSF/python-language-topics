import csv 


name = input("what's your name? ")
home = input("Where's your home? ")

with open('students_home.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name, home], )