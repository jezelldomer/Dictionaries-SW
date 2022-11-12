
#Write a python program for contact tracing:

#Display a menu of options
print("‿︵‿︵  ୨˚̣̣̣͙୧ - M E N U - ୨˚̣̣̣͙୧   ‿︵‿︵")
print("\n ↡       1 ➭ Add an item           ↡\n ↡       2 ➭ Search                ↡ \n ↡       3 ➭ Exit (y/n)            ↡\n")
print ("‿︵‿︵  ୨˚̣̣̣͙୧ ୨˚̣̣̣͙୧ - - ୨˚̣̣̣͙୧ ୨˚̣̣̣͙୧   ‿︵‿︵ \n")

#Dictionary
dict = {
        "Full Name:" : {},
        "Age:" : {},
        "Address:" : {},
        "Contact Number:" : {},
        "Information:" : {}
}

def get_input():
    while True:
    #Ask the user for input
        print ("What do you want to do? Choose from the menu above: \n")
        user_input =input()
        menu = ('1', '2', '3')
        if user_input in menu:
            return user_input
        else:
            print()
            print("Not in the options! Please Try Again\n")
        
while True:   
    user_input = get_input()
    if user_input == "1":
        print("Please Type in your Personal Data for Contact Tracing")
        name  = input("Full Name: ")
        age = input("Age: ")
        address = input("Address: ")
        number = input("Contact Number: ")
        info = input("Activities(meeting, party, in home, etc.): ")
        print("Saved!")
            
            #Stored in Dictionary, dict
        dict ["Full Name:"] = name
        dict ["Age:"] = age
        dict ["Address:"] = address
        dict ["Contact Number:"] = number
        dict ["Information:"] = info
            
    elif user_input == "2":
            
            
    
        
    