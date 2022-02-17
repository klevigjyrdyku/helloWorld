print("Welcome to the rollercoaster")
height = int(input("What is your height in cm: "))
bill = 0
if height >= 120:
  print("Yoy can ride the rollercoaster")
  age = int(input("What is your age? "))

  if age < 12:
    bill = 5
    print("Your tricket are 5$.")
  elif age <= 18:
    bill = 7
    print("Your tricket are 7$.")
  elif 45<= age <= 55:
    print("Your tricket are free")
  else:
    bill = 12
    print("Your tricket are 12$.")

  photo = input("Do you wont to take a photo? Y or N.")
  if photo == "Y":