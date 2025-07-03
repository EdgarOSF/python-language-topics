import csv

name =  input("What's your name? ")
home =  input("What's your home? ")

with open('students_home.csv', 'a') as file:
    reader = csv.DictWriter(file, fieldnames=['name', 'home'])
    reader.writerow({'name': name, 'home': home})
