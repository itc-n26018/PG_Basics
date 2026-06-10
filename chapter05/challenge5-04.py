About_me = {"Height": "165cm",
            "Favorite Color": "Purple-Blue",
            "Favorite Author" : "Souseki",
            "Favorite K-POP Member": "Hitomi"}

answer = input("Search about me! (Type the categories): ")
if answer in About_me:
    result = About_me[answer]
    print(result)
else:
    print("Oops! Can't find it")
