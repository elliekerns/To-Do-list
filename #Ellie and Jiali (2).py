#Ellie and Jiali
#01/12
#To Do List

myGroceryList = ["Eggs","Tomatoes", "Bread", "Milk", "Cookies"]

#Functions

#Takes user input and adds an item to the end of the list
def add_item():
    newitem=input("Which item would you like to add?: ")
    myGroceryList.append(newitem)
    print (myGroceryList)
    
#Takes user input and removes that item from the list
def remove_item():
    removeditem=input("Which item would you like to remove?: ")
    myGroceryList.remove(removeditem)
    print (myGroceryList)
    
#Marks an X next to the item the user has bought
def complete_item():
    ans=input("Which item have you bought?: ")
    i= myGroceryList.index(ans)
    myGroceryList[i]= ans + " [X]"
    print (myGroceryList)
    
#Main

#User interaction loop / This while loop will keep running until you use the break command to end loop

while True:
    print("Choose an option: \n1. Add an item to the grocery list \n2. View the current grocery list \n3. Mark an item as bought \n4. Remove an item from the grocery list \n5. Exit the program")
    option=int(input("Option:"))
    
    if option==1:
        add_item()
        
    if option==2:
        print (myGroceryList)
        
    if option==3:
        complete_item()
        
    if option==4:
        remove_item()
        
    if option==5:
        print("You have exited your grocery list.")
        break