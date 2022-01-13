def set_grade(fighter_to_affect=""):
    """
    - Grade might beu useful later to set a difficulty level
    - Optional argument as long as there's no fighter object
    """

    while True:
        try:
            grade_set = int(input("\nPlease set your grade here (0 for kyusha) : "))

        except:
            print("Please enter a number between 0 and 8\n")

        else:     
            if grade_set == 0:
                print("Kyusha's competition set\n")
                break

            elif grade_set <= 2:
                print("Honor's competition set\n")
                break

            elif grade_set <= 8:
                print("Excellence's competition set\n")
                break

set_grade()


def choose_kamae(fighter_to_affect=""):
    """
    - Choose kamae function (ito, nito, jodan,...)
    - Optional argument as long as there's no fighter object
    """
    
    while True:

        kamae_set = input("\nSet your kamae (h for help) : ")

        if kamae_set == "h":
            print("""
    Kamae's list :

        - Chudan
        - Hidari-Jodan
        - Migi-Jodan
        - Sai-Nito
        - Gyaku-Nito

    (Enter \"q\" at any moment to leave the simulator)
                """)

        elif kamae_set == "q":
            print("\nLeaving the simulator\n")
            break

        elif kamae_set == "Chudan":
            print("Chudan kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Hidari-Jodan":
            print("Hidari-Jodan kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Migi-Jodan":
            print("Migi-Jodan kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Sai-Nito":
            print("Sai-Nito kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Gyaku-Nito":
            print("Gyaku-Nito kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Waki":
            print("Waki kamae choosed (why not)")
            return kamae_set
            break

        else:
            print("Incorrect input, please set a correct kamae please")

kamae = choose_kamae()

if not kamae:
    print("No kamae set")
else:
    print("The kamae set is : " + kamae)