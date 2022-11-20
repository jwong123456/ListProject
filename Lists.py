
#Project is for student to practice WHY we use while loops and how
#to use a specific data structure. such as lists

#First ask them what type of loop we need to use to create a main menu.
#Answer "While loops"
#why?

#Answer: "because they need to add/remove/delete multiple times and we do not know
#but we do know if they press the exit button it should stop and that is our condition
#for the while loop"

#They should create a main menu with 4 options and 1 challenge portion

#Main Menu:
#1. Add Guest
#2. Remove Guest
#3. Change Guest Name
#4. Swap Guest (challenge)
#0. Exit

#Each function try to get a feel for how the student is asking it
#How would you approach this?
#What functions/concepts would we use for this?
#Do you think we need ____?
#Why do you think we need ____ for this project/part?

#ex: Swap function
#T: "Before we start on this what do you think we need?"
#S: "Perhaps we need for loops?"
#T: "Why do you think we need for loops?"
#S: "To go through the list?"
#T: "For what reason?" (specifically asking for WHY he thinks he needs it)
#S: "To check if it is valid"
#T: ...

#Goal is not to show them the code but to make them
#Think of how to use their current knowledge/resources to help them

#REFERENCE FOR STUDENT:
#https://www.w3schools.com/python/python_ref_list.asp
#Allow them to use previous projects as well


def add(Guests):

    #simple append operation
    print("What is the name of the guest you want to add?")
    userInput = input()
    Guests.append(userInput)

    #can add challenge of making it so it HAS to be unique
    #can also add in while loop till user enters 0 to keep adding inputs
    #until 0 is entered to stop adding in multiple users

def remove(Guests):

    #simple delete
    print("What is the name of the guest you want to remove?")
    userInput = input()
    Guests.remove(userInput)

    # can add challenge of making it so it HAS to be unique
    # can also add in while loop till user enters 0 to keep adding inputs
    # until 0 is entered to stop adding in multiple users


def changeGuest(Guests):


    #EASY: Ask the user for the INDEX

    #MEDIUM: Ask the user for the NAME to change to

    #CHALLENGE: Check the user's validity before changing the name

    print("What is the name of the guest you want to change?")
    userInput = input()

    print("What is the name to change to?")
    userInput2 = input()

    #Validity
    if(Guests.count(userInput) == 0):
        return  #This name does not exist


    Guests[Guests.index(userInput)] = userInput2

def display(Guests):
    #simple display
    for x in Guests:
        print("Name=\t"+x)



def swapGuest(Guests):

    #PRACTICE
    #let the student verify that the person exists first before swapping

    #extra challenge: Use the NAME instead of the INDEX of the person

    #Student may use another way
    print("What is the INDEX of the FIRST person you want to replace?")
    index = int(input())

    print("What is the INDEX of the SECOND person you want to replace?")
    index2 = int(input())

    if index >= len(Guests) or index2 >= len(Guests) or index < 0 or index2 < 0:
        print("INVALID INPUT")
        return

    #SHOW THEM THIS WAY
    temp = Guests[index]
    Guests[index] = Guests[index2]
    Guests[index2] = temp

    return

    #note there is also another way SPECIFIC to python u can use
    #If you see this they must be reallly good or looking stuff up
    Guests[index], Guests[index2] = Guests[index2], Guests[index]



def run():

    #Context:
    #you are organizing a hotel guest check in program
    #The hotel(user) should be able to add, remove, change, and swap guests in the hotel
    #assume these hotel rooms are all the same and the the hotel needs to do these functions

    #note:
    #Swap and change guest name is weird in this context but i can't come up with a better scenario

    #Var to hold Guests
    Guests =  []

    #As long as while loop stops when they type in 0 it doesn't matter
    while(True):
        print("1. Add Guest")
        print("2. Remove Guest")
        print("3. Change Guest Name")
        print("4. Display All Guests")
        print("5. Swap Guest (Challenge)")
        print("0. Exit")
        userInput = input()

        #for purposes of organizing this document the answers will be above
        #student SHOULD NOT USE FUNCTIONS HERE UNLESS THEY KNOW HOW TO!
        if(userInput == "1"):
            add(Guests)
        elif (userInput == "2"):
            remove(Guests)
        elif (userInput == "3"):
            changeGuest(Guests)
        elif (userInput == "4"):
            display(Guests)
        elif (userInput == "5"):
            swapGuest(Guests)
        elif (userInput == "0"):
            return #you can also use break, or just use condition for while loop
        else:
            print("Invalid value Entered")







if __name__ == '__main__':
    run()
