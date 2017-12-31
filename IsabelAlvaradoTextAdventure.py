
#Beginning prompt
start = "You wake up one morning and find that you aren't on your bed; you aren't even in your room. \nYou're in the middle of ... somewhere. \nA sign is positioned right in front of you, covered with some dust. \nIt says: 'Welcome to the Bear Frachise'"
choice= "There is a hallway to your right and to your left."

print(start)
print(choice)
#Choices of left or right

#Choice of going left
left_right= raw_input("\nType 'left' to go left or 'right' to go right\n")
#Left
if left_right == "left" or "Left":
    print("You decide to go left")

    print("You keep on walking. The lights are flickering, the walls and floors are dirty. To your right, you can see an office. \nYou move closer. \nThere is a sign next to the wooden door that says: Operations Office. \nGo in or continue down the hall?")
    office_hall= raw_input("\nType 'office' to go inside or 'hall' to continue\n")

    if office_hall == "office" or "Office":
        #Left-> Office
        print("You chose the office")
        print("The room is messy, as if someone had not been there in decades. There are hundreds of files on the floor, which seem to have come from the main desk across the room.")
        print("When you step in the room, a light seems to come off from the main desk. You look towards it and see a desktop. \nDo you walk to the desktop or look at the files on the floor? ")
        files_desktop= raw_input("Type 'files' to look at the files or 'desktop' to analyze the computer")
        if files_desktop == "files" or "Files":
            #Left->Office->Files
            print ("You chose to observe the files")
            print ("Some of them have the word 'Confidencial' on them. While looking through them, you wonder upon the fact that you probably should not have been in the room.")
            print ("Then, you stop. A file with the title 'DANGER' was staring right through your soul. You look through it.")
            print ("...")
            print ("...")
            print ("A chill goes through your spine. How could they do this to CHILDREN?. You look around. You don't want to be in this place anymore, not after reading the file.")
            print ("You look around and find an exit door in the office.")
            print ("You open it and run away")
        elif files_desktop == "desktop" or "Desktop":
            #Left->Office->Desktop
            print ("You chose to analyze the desktop. You tried to log in, in order to get information about this place")
        else:
            print ("This is not a valid response. You can't just run away from your choices. Sometimes, choosing is something that must be done. It's a part of life.")

    elif office_hall == "hall" or "Hall":
        #Left-> hall
        print("You chose the hall")
        print("You keep on walking for minutes. Then minutes become hours. And hours become days. You spend your last days on earth in the hall, only to be found by the next victim on the floor. ")
    else:
        print("This is not a valid response. You can't just run away from your choices. Sometimes, choosing is something that must be done. It's a part of life.")
#choices of going right
if left_right == "right" or "Right":
    #Right
    print("You chose right")
    print("Down the hall, you can see that there are two rooms. \nTo the right, there is a door with a sign that says: Party Room. \nTo the left, there is a door with a sign that says: Storage Room. \nYou keep on walking, but you meet a dead end. On the wall there is a sign that appears to be ripped in half. Chills run through your back. \nThere is no turning back. A choice must be made.")
    storage_party= raw_input("Type 'party' to go in the Party Room or 'storage' to go inside the Store")

    if storage_party == "party" or "Party":
        #Right->Party Room
        print("You chose the Party Room")
    elif storage_party == "store" or "Store":
        #Right-> Store
        print("You chose the store")
    else:
        print ("This is not a valid response. You can't just run away from your choices. Sometimes, choosing is something that must be done. It's a part of life.")


else:
    print ("This is not a valid response. You can't just run away from your choices. Sometimes, choosing is something that must be done. It's a part of life.")
