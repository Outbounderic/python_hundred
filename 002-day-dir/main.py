cond_start = input("Welcome to the tavern... \nWould you like a room? (Y)es or (N)o ")

if (cond_start == 'y') :
  print("Oh good, that will be five sheckles.")
  meal = input("Would you like a meal with your room? (Y)es or (N)o ")
  if (meal == 'y') :
    print("Right away, that will be two sheckles.")
    drink = input("Now, how about a drink? (Y)es or (N)o ")
    if (drink == 'y') :
      print("Oh goodie, that will be another sheckle... have a fantastic night.")
    
  else :
    print("Here's your key, have a good night.")
  
else :
  print("No room, no service... best get out of here.")
