import random 



listPassword =  ["a","b","c","d","e","f","g","h","i","j","k","l","1","2","3","4""#"]
mypassword  = " " 

print("Welcome, to the Passwords Generator");
print("====================================")

for cont in range(1,17):
    indice =  random.randrange(0,16)
    mypassword += listPassword[indice]

print("You password is: "+mypassword)


