import random 


listPassword =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z","1","2","3","4","5","6","7","8","9","#"]

titleMotif = ""
mypassword  = " " 

print("Welcome, to the Passwords Generator");
print("====================================")


for cont in range(1,17):
    indice =  random.randrange(0,16)
    mypassword += listPassword[indice]

titleMotif = input("Title Motif: ")

if(mypassword !=  ""):
  file =  open("dataPassword.txt","a")
  file.write( "- " + titleMotif + " : " +mypassword +"\n" )

  print("Result")
  print("---------")
  print("Tile Motif: " + titleMotif)
  print("You password is: "+mypassword)
else : 
    print("error, intente nuevamente  por favor ")




