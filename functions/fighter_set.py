    # fighter  argument optional in anticipation of a 2-player mode)

def set_gender(fighter = ""):

    """
    - Gender prevail on set_age to determine competition type (feminin)
    - 
    """
    
    while True:
        gender_set = input("\nPlease set your gender (M)an or (W)oman : ")

        gender_set = gender_set.lower()
        
        if gender_set != ("m") and gender_set != ("w"):
            print("\nPlease enter a valid answer")

        elif gender_set == "m":
            print("Gender set to Man")
            return "Man"
            break

        elif gender_set == "w":
            print("Gender set to Woman")
            return "Woman"
            break

gender = set_gender()

def set_age(fighter = ""):

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


def set_grade(fighter = ""):

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
                print("\nKyusha's grade set")
                return grade_set
                break

            elif grade_set <= 2:
                print(str(grade_set) + "dan set")
                return grade_set
                break

            elif grade_set <= 8:
                print(str(grade_set) + "dan set")
                return grade_set
                break

grade = set_grade()


def choose_kamae(fighter = ""):

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


# ↓↓↓ Bloc test à supprimer ↓↓↓

try:
    print("So the fighter is a " + gender + " of " + str(age) + " years old, whose grade is " + str(grade) + " and fight in " + kamae + " kamae.")
except:
    print("Informations is missing")

# ↑↑↑ Bloc test à supprimer ↑↑↑


def set_competition(fighter_gender,fighter_age,fighter_grade,fighter=""):
    if fighter_age < 18:
        if fighter_gender == "Woman":
            print("You can fight in Woman's and Junior's competition")
            return "Woman's and Junior's"
        else:
            print("You can fight in Junior's competition")
            return "Junior's"
    if fighter_age >= 18:
        if fighter_gender == "Woman":
            print("You can fight in Woman's competition")
            return "Woman's"
        else:
            if fighter_grade <= 1:
                print("You can fight in Kyusha's competition")
                return "Kyusha's"
            elif fighter_grade < 3:
                print("You can fight in Honor's competition")
                return "Honor's"
            else:
                print("You can fight in Excellence's competition")
                return "Excellence's"

competition = set_competition(gender,age,grade)

print("Fighter will go to " + competition + " competition.")