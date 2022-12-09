import json
from colors import my_color_list
#function to start the quiz questions 

def quiz():
    q1 = input("What color do you like for clothes? ")
    q2 = input("what color is the sky currently? ")
    q3 = input("What day is it? ")

    #question_1_list = my_color_dict
#TODO add all the variables do the other question
    q1_value = my_color_list[1]
    if q1 == q1_value:
        print("this worked finally")
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
