import json
from colors import my_color_list
#function to start the quiz questions 

def quiz():
    q1 = input("What is your favorite color? ")
    q2 = input("What is the first letter if your name? ")
    q3 = input("What day is it? ")

    american_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
   
    #question_1_list = my_color_dict
#todo add all the variables do the other question
#question 1 if statements
    if q1 == my_color_list[1]:
        print("this worked finally")
    if q1 == my_color_list[0]:
        print("you have selected blue as your favorite color")
    if q1 == my_color_list[2]:
        print("you have selected black as your favorite color")   
    if q1 == my_color_list[3]:
        print("you have selected red as your favorite color")
#question 2 if statements 
    if q2 == american_alphabet[0]:
        print("the first letter of your name is in the range")          
    else:
        print("try again")
    


#question_1_list = my_color_list
#make a fucntion for all the variables of the color names so that the if statement can 
#be based on the color names instead of the values from the dictionary
#def value_color_names():


print("Which Avenger do YOU think you are?")
#TODO add a sleep time in between this question 
print("Would you like to continue?")

answer = input("Y/N:")
if answer == "Y".casefold():
    quiz()
else:
    print("Come back later!")




#def stop(): to stop the function if errors or input change occurs 
