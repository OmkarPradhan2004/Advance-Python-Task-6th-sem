rooms={
    101:None,
    102:None,
    103:None,
    104:None,
    105:None
}
occupied=set()
#To Do:
#allot room
#vacate room
#room info
#exit
while True:
    print("1.Allot Room")
    print("2.Vacate Room")
    print("3.Room Info")
    print("4.Exit")
    c=int(input("Enter Your Choice:"))

    if c==1:
        print("Available rooms:")
        for key in rooms:
            if rooms[key]==None:
                print(key)      

        a=int(input("Select Room to Allot:"))
        n=input("Enter Guest Name:")
        rooms[a]=n
        print("Room Alotted SUCCESSFULLY!")
        occupied.add(a)

    elif c==2:
        print("Alloted rooms:")
        print(occupied)
        v=int(input("Select Room to Vacate:"))
        rooms[v]=None
        print("Room Vacated SUCCESSFULLY!")
        occupied.remove(v)

    elif c==3:
        print("Room info:")
        print("Available rooms:")
        for key in rooms:
            print(key,"-",rooms[key])

    elif c==4:
        print("THANK YOU!")
        break

    else:
        print("Invalid Choice!")