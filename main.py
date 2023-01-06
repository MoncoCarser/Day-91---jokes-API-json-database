import requests, json, os, time



while True:
    os.system("clear")
    new_or_old = input("Would you like to see a joke? (y) \n Or load old jokes (o )> ").lower()
    
    if new_or_old[0] == "y":
        result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
        joke = result.json()
        print()
        print(joke["joke"])
        joke_id = joke["id"]
        
        choice_to_save = input("\nWould you like to save that joke? y/n \n>").lower()
        
        if choice_to_save[0] == "y":
            with open("database.txt", newline="\n", mode="a+") as f:
                f.write(joke_id)
                f.write("\n")

        else:
            continue

    if new_or_old[0] == "o":
        with open("database.txt", mode="r") as data:
            for item in data:
                item = item[:-1]
                result = requests.get(f"https://icanhazdadjoke.com/j/{item}", headers={"Accept":"application/json"})
                joke = result.json()
                print()
                print(joke["joke"])
                time.sleep(2)
    time.sleep(2)
               
                
            