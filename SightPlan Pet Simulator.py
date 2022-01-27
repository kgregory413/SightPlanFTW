### Created by Kylie Gregory for Git/Python Training ###
### -- v1.0 -- January 27th, 2022 -- ##

### Welcome to the SightPlan Pet Simulator! ###
### Be a good pet parent and make your fur (or scale) baby happy! ###

# Pet dictionary
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

# pet toys data object
petToys = {"cat": ["scratching post", "nerf gun", "release a fake mouse into the SightPlan office"], "dog": ["frisbee", "Felipe's shoe", "mark territory in the Work conference room"], "fish": ["hide and seek in coral", "jump through hoop", "splash"]}

# Prompt for different options for pet type.
def initPet():
  # get input for what type of pet this is
  petType = ""

  petOptions = list(petToys.keys())
  # validate input
  while petType not in petOptions:
      print("Please choose a type of pet from the following options: ")
      for option in petOptions:
          print(option)
      petType = input("Please input one of the pets: ")
    # write pet type into database
  pet["type"] = petType

  # name your pet
  pet["name"] = input("What would you like to name your " + pet["type"] + "? ")


  # write to pet dictionary

# Print menu
def printMenu(menuOptions):
    optionKeys = list(menuOptions.keys())

    print("Here are your options:")
    print("-------")
    for key in optionKeys:
        print(key + ":\t" + menuOptions[key]["text"])

# Play with toys
def playToys():
  print(pet["name"] + " " + "had a wonderful time playing with you!")

# Get new toys
def getToys():
  print("Yay! Let's get some new toys!")
  toyOptions = petToys[pet["type"]]
  print(toyOptions)

  # specify toy number to select from list
  toyNum = -1

  while toyNum < 0 or toyNum > len(toyOptions) -1:
    for i in range(len(toyOptions)):
      print(str(i) + ": " + toyOptions[i])
    toyNum = int(input("Input the number of the toy you would like: "))

  #get the selected toy option from the list
  chosenToy = toyOptions[toyNum]
  pet["toys"].append(chosenToy)
  print("Nice! You selected the " + chosenToy + "!")

# Quit the game
def quitSimulator():
  print("Quit the simulator. Thanks for playing!")

# Feed your pet
def feedPet():
    newHunger = pet["hunger"] - 20
    if newHunger < 0:
      newHunger = 0
    pet["hunger"] = newHunger
    print("Your pet raided the breakroom fridge! Hunger decreased by 20!")

# print stats about current pet status
def printStats():
    print("Your pet " + pet["type"] + " " + pet["name"] + " is doing great!")
    print("Your pet currently has: " + str(len(pet["toys"])) + " toys, which are: ")
    for toy in pet["toys"]:
        print(toy)
    print("Your pet is currently at hunger of " + str(pet["hunger"]) + " " + "out of 100.")
    print("Your pet is currently " + str(pet["age"]) + " days old.")


# Main game loop
def main():

  # print welcome screen
  print("Welcome to the SightPlan Pet Simulator!")
  print("Adopt a pet to help you get sh*t done!")
  print()

  # initialize pet
  initPet()
  
  # menu options for printing and access
  menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game" }, 
    "F": { "function": feedPet, "text": "Feed" + " " + pet["name"] },
    "P": { "function": playToys, "text": "Play with" + " " + pet["name"] },
    "G": { "function": getToys, "text": "Get new toys for" + " " + pet["name"] + "!" }}

  keepPlaying = True
  while keepPlaying:
      # print the menu
      menuSelection = ""

      # validate the input
      while menuSelection not in menuOptions.keys():
        printMenu(menuOptions)
        menuSelection = input("Which of these menu options would you like to use? ").upper()
      
      # quit the game for "Q"
      if menuSelection == "Q":
          keepPlaying = False
      
      # invoke the function for selection
      menuOptions[menuSelection]["function"]()

      # increase pet hunger and age each turn
      pet["hunger"] += 10
      pet["age"] += 1
      print()
      printStats()

      # print out an extra line for space
      print()


main()
