# game

#Beginning prompt
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of ... somewhere.
A sign is positioned right in front of you, covered with some dust. It says: "Welcome to the Bear Frachise"
There is a hallway to your right and to your left.
'''
print(start)

#Choices of left or right

#Choice of going left
print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left" or "Left":
    #Left
    print("You decide to go left")
    print("You keep on walking. The lights are flickering, the walls and floors are dirty. To your right, you can see an office. You move closer. There is a sign next to the wooden door that says: Operations Office. Go in or continue down the hall?")
    print("Type 'office' to go inside or 'hall' to continue")
    if user_input == "office" or "Office":
        #Left-> Office
        print("You chose the office")
        print("The room is messy, as if someone had not been there in decades. There are hundreds of files on the floor, which seem to have come from the main desk across the room.")
        print("When you step in the room, a light seems to come off from the main desk. You look towards it and see a desktop. Do you walk to the desktop or look at the files on the floor? ")
        print("Type 'files' to look at the files or 'desktop' to analyze the computer")
        if user_input == "files" or "Files":
            #Left->Office->Files
            print ("You chose to observe the files")
        elif user_input == "desktop" or "Desktop":
            #Left->Office->Desktop
            print ("You choose to analyze the desktop")
    elif user_input == "hall" or "Hall":
        #Left-> hall
        print("You chose the hall")
elif user_input == "right" or "Right":
    #Right
    print("You chose right")
    print("Down the hall, you can see that there are two rooms. To the right, there is a door with a sign that says: Party Room. To the left, there is a door with a sign that says: Store. You keep on walking, but there is nowhere else to go. A choice must be made.")
    print("Type 'party' to go in the Party Room or 'store' to go in the store")
    if user_input == "party" or "Party":
        #Right->Party Room
        print("You chose the Party Room")
    elif user_input == "store" or "Store":
        #Right-> Store
        print("You chose the store")



#SOMETHING WRONG HERE

else user_imput ==! "Left" or "left" or "Right" or "right":
    print ("This is not a valid response. You can't just run away from your choices. Sometimes, choosing is something that must be done. It's a part of life.")



#Choices of going right
elif user_input == "right" or "Right":
    print("You choose to go right")
