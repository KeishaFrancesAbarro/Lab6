age = int(input("Enter your age: "))
mem = input("Are you a member?")
choice1 = "yes"
choice2 = "no"

if age <=18 :
    if mem == choice1 :
        print("Your fee is 450.00 pesos")
    if mem ==choice2 : 
        print("Your fee is 650.00 pesos")
        
elif age >=18 and age <=65 :
    if mem == choice1 :
        print("Your fee is 550.00 pesos")
    if mem == choice2 :
        print("Your fee is 750.00 pesos")
        
elif age >=66 and age <=120 :
    if mem == choice1 :
        print("Your fee is 400.00 pesos")
    if mem == choice2 :
        print("Your fee is 600.00 peos")

else:
    print("invalid age")