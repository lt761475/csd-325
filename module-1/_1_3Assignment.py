# Leon Truong, 1.3 Assignment, 10/25/2026
#= beers on the wall program. 

#bottle song function
def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        bottles = bottles - 1

    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, no more bottles of beer on the wall.")


def main():
    yesNo = True
    #validation loop
    while yesNo == True:
        try:
            #get number
            bottles = int(input("Enter number of bottles: "))

            #validation
            if bottles <= 0:
                print("Please enter a number greater than 0.")
            else:
                #if validation was sucessful
                yesNo = False
        #validation pt2
        except ValueError:
            print("Invalid input. Please enter a whole number.")


    #function call
    countdown(bottles)

    print("Time to buy more bottles of beer.")


main()