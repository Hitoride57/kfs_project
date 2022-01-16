def set_gender(fighter_to_affect = ""):

    """
    - Gender prevail on set_age to determine competition type (feminin)
    - Optional argument as long as there's no fighter object
    """
    
    while True:
        gender_set = input("\nPlease set your gender (M)an or (W)oman : ")

        if gender_set != ("M") and gender_set != ("W"):
            print("\nPlease enter a valid answer")

        elif gender_set == "M":
            print("Gender set to Man")
            return "Man"
            break

        elif gender_set == "W":
            print("Gender set to Woman")
            return "Woman"
            break

gender = set_gender()

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
            
            elif age_set >= 12 and age_set < 18:
                print("\nAge set to " + str(age_set) + ".")
                return age_set
                break

            elif age_set >= 18:
                print("\nAge set to " + str(age_set) + ".")
                return age_set
                break

age = set_age()


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
                return "Kyusha"
                break

            elif grade_set <= 2:
                print("\nHonor's competition set")
                return (str(grade_set) + "dan")
                break

            elif grade_set <= 8:
                print("\nExcellence's competition set")
                return (str(grade_set) + "dan")
                break

grade = set_grade()


def choose_kamae(fighter_to_affect=""):

    """
    - Choose kamae function (ito, nito, jodan,...)
    - Optional argument as long as there's no fighter object
    """
        
        #Look forward to simplify input with a numbered list to select kamae
    
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

print("So the fighter is a " + gender + " of " + str(age) + " years old, whose grade is " + str(grade) + " and fight in " + kamae + ".")