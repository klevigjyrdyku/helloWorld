print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

a = name1.lower()
b = name2.lower()
T = a.count('t')
R = a.count('r')
U = a.count('u')
E = a.count('e')
TT = b.count('t')
RR = b.count('r')
UU = b.count('u')
EE = b.count('e')
L = a.count('l')
O = a.count('o')
V = a.count('v')
E = a.count('e')
LL = b.count('l')
OO = b.count('o')
VV = b.count('v')
EE = b.count('e')
true = int(T + R + U + E +TT + RR + UU + EE )
love = int(L + O + V + E + LL + OO + VV + EE )
total = int(str(true) + str(love))
if  10 > total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 <= total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")