import json
from colors import my_color_list
import time
from avengers_list1 import avenger_list
#function to start the quiz questions 

def quiz():
    q1 = input("What color are your eyes? ")
    q2 = input("What is the first letter of your name? ")
    q3 = input("What is your favorite vegtable? ")

    vegtable_list = ['Cucumber', 'Carrot', 'Tomato', ]
    american_alphabet = ['a','b','c','d','e','f','g','h',"i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    list1 = [] #this is to allow the range of first name characters to be assigend to a value
    list2 = [] #this is for the colors list to assign an avenger to it 
    list3 = []
#todo add more colors to be including 
#question 1 if statements using list 2
    if q1 in my_color_list[1]:
        first_color = 1
        list2.append(first_color)
    if q1 in my_color_list[0]:
        second_color = 2 
        list2.append(second_color)
    if q1 in my_color_list[2]:
        third_color = 3 
        list2.append(third_color)
    if q1 in my_color_list[3]:
        fourth_color = 4 
        list2.append(fourth_color)
#question 2 if statements using list 1
    if q2 in american_alphabet[0:6]:
        first_range = 1
        list1.append(first_range)  
    if q2 in american_alphabet[7:13]:
        second_range = 2
        list1.append(second_range)
    if q2 in american_alphabet[14:20]:
        third_range = 3
        list1.append(third_range)      
    if q2 in american_alphabet[21:26]:
        fourth_range = 4
        list1.append(fourth_range)             
    else:
        print("try again")
#question 3 if statements using list 3 
    if q3 in vegtable_list:
        first_vegtable = 1 
        list3.append(first_vegtable)
    print(list1)
#question 3 if statments 


#question_1_list = my_color_list
#make a fucntion for all the variables of the color names so that the if statement can 
#be based on the color names instead of the values from the dictionary
#def value_color_names():


print("Which Avenger do YOU think you are?")
time.sleep(2)
print("Would you like to find out?")

answer = input("Y/N:")
if answer == "Y".casefold():
    quiz()
else:
    print("Come back later!")




#def stop(): to stop the function if errors or input change occurs 
