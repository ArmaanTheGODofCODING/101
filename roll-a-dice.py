import random
response = "y"

if response == "y":
    while response == "y":
        no  = random.randint(1,6)
        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")

            input("Please enter y to roll dice or n to exit")
        if no == 2:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")

            input("Please enter y to roll dice or n to exit")
        if no == 3:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")

            input("Please enter y to roll dice or n to exit")
        if no == 4:
            print("[-----]")
            print("[0 0 0]")
            print("[  0  ]")
            print("[0 0 0]")
            print("[-----]")

            input("Please enter y to roll dice or n to exit")
        if no == 5:
            print("[-----]")
            print("[  0  ]")
            print("[  0  ]")
            print("[  0  ]")
            print("[-----]")

            input("Please enter y to roll dice or n to exit")
        if no == 6:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[  0  ]")
            print("[-----]")

            input("Please enter y to roll dice or n to exit")
else:
    print("The game has been exited! To start again, press y!")