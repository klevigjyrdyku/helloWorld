command = ""
Started = False
while True:
    command = input("< "). lower()
    if command == "start":
        if Started:
            print("Car is alredy started!")
        else:
            Started = True
            print("car started...")
    elif command == "stop":
        if not Started:
            print("Car is alredy stopped!")
        else:
            print("Car stopped...")
    elif command == "help":
        print("""
        start - to start the car
        stop -  to stop the car
        quit - to quit
        """)
    elif command == "quit":
              break
    else:
        print("Sorry i don't andestand that!??")
