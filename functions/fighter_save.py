    # Saving fighter info for further fights

from os.path import exists

    # File will be name with fighter's name
fighter_name = "Hito"

savefile_choice = (fighter_name + ".sav")

if exists(savefile_choice):
    
    print(savefile_choice + " already exists.")
    

    while True:
        
        savefile_answer = input('(C)ontinu / (O)verwrite / (A)bort : ')
        savefile_answer = savefile_answer.lower()

        if savefile_answer == "c":
            savefile = open(savefile_choice, "a")

            """
                To be completed later
            """

            print(savefile_choice + " has been updated")

            savefile.close()
            break

        elif savefile_answer == "o":

            while True:

                confirm = input("Are you sure ? (Y)es or (N)o ")
                confirm = confirm.lower()

                if confirm == "y":

                    savefile = open(savefile_choice, "w")
                    
                    """
                        To be completed later
                    """

                    print(savefile_choice + " has been overwrote")

                    savefile.close()
                    break

                elif confirm == "n":
                    print("Save cancelled")
                    break
            break

        elif savefile_answer == "a":
            print("Save cancelled")
            break

else:
    savefile = open(savefile_choice, "w")

    """
        To be completed later
    """

    print(savefile_choice + " has been created")

    savefile.close()