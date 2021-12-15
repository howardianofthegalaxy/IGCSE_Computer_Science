#initalize a list (linkedlist)
student_names = ["mike", "amy", "charlie", "marco", "david", "leon", "rain"]

#add a name to our list
student_names.append("mars")
student_names.insert(0, "Mr.Amini") #insert at index (0) first position
print("first student", student_names[0])

#delete a name
student_names.remove("charlie")

#iterate over our list
for name in student_names:
    print(name)

#get the length of the list
length = len(student_names)
print(length)

#sort list using built in list method. sort
student_names.sort()
for name in student_names:
    print(name)

#create a list of booleam values tp represent
#students who have done their homework
has_done_homework = [True, False, True, False, True, False, False, True, True]
print(has_done_homework)
has_done_homework.sort()
print(has_done_homework)

#how many false values are in this data structure?
number_Falses = has_done_homework.count(False)
print(number_Falses)

#iterate (traverse the datastructure)
for student in has_done_homework:
    print(student)

#make a list that stores the 
#amount of money each student has in their pocket
money_in_student_pockets = [50,190, 4928, 587.7, 13]
print(money_in_student_pockets)