# Choose kamae function (ito, nito, jodan,...)


def choose_kamae(fighter_to_affect=""):                     # Optional argument as long as there's no fighter object

    while True:

        kamae_set = input("Set your kamae (h for help) : ")

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