prijsbolletjes = 1.10
prijsbakje = 0.75
prijshoorntje = 1.25
totaalbolletjes = 0
totaalbakje = 0 
totaalhoorntje = 0 
hoeveel = 0



def yesOrno(vraag): 
    while True:
        antwoord = input(vraag) 
        if antwoord == "ja":
            return True
        elif antwoord == "nee":
            return False
        else:
            print("invalid Option")
def bonnetje():  
    totaal = (totaalbolletjes * prijsbolletjes) + (totaalbakje * prijsbakje) + ( totaalhoorntje * prijshoorntje) 
    print("dat is dan",(totaalbolletjes), "x",(prijsbolletjes), "+" ,(totaalbakje), "x", (prijsbakje), "+", (totaalhoorntje), "x", (prijshoorntje), "end dat is" ,(totaal))

def smaken():
    while True:
        print("""De Smaken zijn
A = Aardbei
B = Vanille
C = Chocolade""")
        antwoordSmaken = input("Welke Smaak: ").lower()
        if antwoordSmaken == "a":
            return "Aardbei"
        elif antwoordSmaken== "b": 
            return "vanille"
        elif antwoordSmaken == "c":
            return "chocolade" 
        else: 
            print("invalid option") 
    




print("welkom bij papigelato")
def bolletjes():
    while True:
        hoeveel = int(input("hoeveel bolletjes wil je?"))
        if hoeveel > 8:
            print("sorry zon grote bak hebben wij niet") 
        else:
            return hoeveel
while True:
    hoeveel = bolletjes()
    totaalbolletjes += hoeveel
    if hoeveel <= 4:
        allesmaken = ""
        for x in range(hoeveel):
            x += 1
            print(f"Geef de smaak voor bolletje {x} ")
            allesmaken = allesmaken + " " +  smaken()
        print(allesmaken)  
        bakofhoorntje = input("wilt u een bak of een hoorntje") 
        if bakofhoorntje == ("bakje"):
            print("oke, dan is hier uw bakje met", (hoeveel),"bolletjes")  
            totaalbakje += 1 
        elif bakofhoorntje == ("hoorntje"): 
            totaalhoorntje += 1 
            print("oke, dan is hier uw hoorntje met", (hoeveel), "bolletjes") 
            
        else:
            print("sorry dat snap ik niet")
            
    elif hoeveel >= 3:
        allesmaken = ""
        for x in range(hoeveel):
            x += 1
            print(f"Geef de smaak voor bolletje {x} ")
            allesmaken = allesmaken + " " +  smaken()
        print(allesmaken)
        print ("oke, dan is hier uw bakje met",(hoeveel),"bollejes") 
        totaalbakje += 1 
 
    

    inputYesNo = input("Wil je nog meer bestellen?")
    if inputYesNo == "ja":
        print("Oke meer ijs")
    elif inputYesNo == 'nee':
        print (bonnetje()) 
        break
    
 


     

    





