import json
from colors import my_color_list
import time
#function to start the quiz questions 

def quiz():
    q1 = input("What is your favorite color? ")
    q2 = input("What is the first letter if your name? ")
    q3 = input("What day is it? ")

    american_alphabet = ['a','b','c','d','e','f','g','h',"i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    avenger_list1 = []
    #question_1_list = my_color_dict
#todo add all the variables do the other question
#question 1 if statements
    if q1 == my_color_list[1]:
        print("this worked finally")
    if q1 == my_color_list[0]:
        print("you have selected blue as your favorite color")
        print("\n")
    if q1 == my_color_list[2]:
        print("you have selected black as your favorite color")
        print("\n")   
    if q1 == my_color_list[3]:
        print("you have selected red as your favorite color")
        print("\n")
#question 2 if statements 
    if q2 == american_alphabet[0]:
        first_letter = 0   
    if q2 == american_alphabet[1]:
        second_letter = 1 
    if q2 == american_alphabet[2]:
        third_letter = 2
    if q2 in american_alphabet[3:6]:
        first_range = 1
        avenger_list1.append(first_range)      
    else:
        print("try again")
    
    print(avenger_list1)



#question_1_list = my_color_list
#make a fucntion for all the variables of the color names so that the if statement can 
#be based on the color names instead of the values from the dictionary
#def value_color_names():


print("Which Avenger do YOU think you are?")
time.sleep(3)
print("Would you like to find out?")

answer = input("Y/N:")
if answer == "Y".casefold():
    quiz()
else:
    print("Come back later!")




#def stop(): to stop the function if errors or input change occurs 
