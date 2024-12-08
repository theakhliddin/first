class Fruits:
    name = "Fruits"
    season = "Season"

def main():
    fruit1 = Fruits()
    fruit1.name = "Mango"
    fruit1.season = "Summer"
    print("Name of furit: ",fruit1.name,"What's season: ",fruit1.season)
    
    fruit2 = Fruits()
    fruit2.name = "Orange"
    fruit2.season = "Winter"
    print("Name of furit: ",fruit2.name,"What's season: ",fruit2.season)


    fruit3 = Fruits()
    print("Fruit name:" ,fruit3.name,"Season: ",fruit3.season)

if __name__ == "__main__":
    main()