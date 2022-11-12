
#Write a python program for contact tracing:

#Display a menu of options
menu_options = ("\033[0;36;40m\n‿︵‿︵  ୨˚̣̣̣͙୧ - M E N U - ୨˚̣̣̣͙୧   ‿︵‿︵\n\n ↡\033[1;33;40m       1 ➭ Add an item         \033[0;36;40m  ↡\n ↡  \033[1;32;40m     2 ➭ Search              \033[0;36;40m  ↡ \033[0;36;40m\n ↡     \033[1;31;40m  3 ➭ Exit (y/n)            \033[0;36;40m↡\n\n‿︵‿︵  ୨˚̣̣̣͙୧ ୨˚̣̣̣͙୧ - - ୨˚̣̣̣͙୧ ୨˚̣̣̣͙୧   ‿︵‿︵ \n")

#Dictionary
dict = {
        "Full Name" : {},
        "Age" : {},
        "Address" : {},
        "Contact Number" : {},
        "Information" : {}
}

def get_input():
    while True:
    #Ask the user for input
        print(menu_options)
        print ("\033[1;37;40mWhat do you want to do? Choose from the menu above: \n")
        user_input =input()
        menu = ('1', '2', '3')
        if user_input in menu:
            return user_input
        else:
            print()
            print("Not in the options! Please Try Again\n")
            print("\n°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。\n ")
        
while True:   
    user_input = get_input()
    if user_input == "1":
        print("\n°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。\n ")
        print("\033[1;33;40m    ⇝   C O N T A C T  T R A C I N G   ⇜    \033[1;33;40m\n")
        print(" \033[1;37;40mPlease Type in your Personal Data for Contact Tracing \n\033[0;33;40m")
        name  = input("Full Name: ")
        age = input("Age: ")
        address = input("Address: ")
        number = input("Contact Number: ")
        info = input("Activities(meeting, party, in home, etc.): ")
        print("\033[1;32;40m\n    Saved!")
        print("\033[1;37;40m\n°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。\n ")
            
            #Stored in Dictionary, dict
        dict ["Full Name"] = name
        dict ["Age"] = age
        dict ["Address"] = address
        dict ["Contact Number"] = number
        dict ["Information"] = info
     
     #Option 2       
    elif user_input == "2":
        key = input("\033[0;33;40m\nWhat key do you want to search?: ")     
        if key in dict:
            print (dict[key])
        else:
            print ("\033[1;31;40m\nNot Available\n")
            print("\033[1;37;40m\n°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。\n ")
            
     #Option 3
     
    elif user_input == "3":
        yesno = input("\033[1;31;40mAre you sure? (y/n): ")
      
        if yesno == "y":    
            print ("\033[1;32;40m\nExit - Thank You!")
            print("\033[1;37;40m\n°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。\n ")
            break
      
        