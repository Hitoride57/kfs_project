def set_age(fighter_to_affect=""):
    """
    - Age prevail on set_grade to determine competition type
    - Optional argument as long as there's no fighter object
    """

    while True:
        try:
            age_set = int(input("\nPlease set you age here (minimum 12 y.o.) : "))
        
        except:
            print("\nPlease enter a valid age")
        
        else:
            if age_set < 12:
                print("\nCompetition is not open to child under 12 years old")
            
            elif age_set >= 12 & age_set < 18:
                print("\nAge set to " + str(age_set) + ".")
                return age_set
                break

            elif age_set >= 18:
                print("\nAge set to " + str(age_set) + ".")
                return age_set
                break

set_age()


def set_grade(fighter_to_affect=""):
    """
    - Grade might be useful later to set a difficulty level
    - Optional argument as long as there's no fighter object
    """

    while True:
        try:
            grade_set = int(input("\nPlease set your grade here (0 for kyusha) : "))

        except:
            print("\nPlease enter a number between 0 and 8")

        else:     
            if grade_set == 0:
                print("\nKyusha's competition set")
                return grade_set
                break

            elif grade_set <= 2:
                print("\nHonor's competition set")
                return grade_set
                break

            elif grade_set <= 8:
                print("\nExcellence's competition set")
                return grade_set
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
            print("\nChudan kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Hidari-Jodan":
            print("\nHidari-Jodan kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Migi-Jodan":
            print("\nMigi-Jodan kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Sai-Nito":
            print("\nSai-Nito kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Gyaku-Nito":
            print("\nGyaku-Nito kamae choosed")
            return kamae_set
            break

        elif kamae_set == "Waki":
            print("\nWaki kamae choosed (why not, it can be efficient against nito)")
            return kamae_set
            break

        else:
            print("\nIncorrect input, please set a correct kamae please")

kamae = choose_kamae()

if not kamae:
    print("No kamae set")
else:
    print("The kamae set is : " + kamae)