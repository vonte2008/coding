def voter(age):
    if age >= 18:
      print("user may vote")
    else:
        print("user is not old enough to vote")

voter(18)


def maxnumber():
   numb1 = int(input("please type in a number:"))
   numb2 = int(input("please type in another number:"))
   numb3 = int(input("please type in another number:"))
   hiNumber = max(numb1, numb2, numb3)
   print(hiNumber)