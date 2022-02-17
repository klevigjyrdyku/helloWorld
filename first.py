print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
S = 15
M = 20
L = 25
if size == "S":
  bill += S
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
      bill += 1
elif size == "M":
  bill += M
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
      bill += 1
else :
  bill += L
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
      bill += 1

print(f"Your final bill is: ${bill}.")