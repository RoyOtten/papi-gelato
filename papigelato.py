prijsbolletjes = 0.95
prijsbakje = 0.75
prijshoorntje = 1.25
totaalbolletjes = 0
totaalbakje = 0 
totaalhoorntje = 0 
hoeveel = 0
prijsslagroom = 0.50
totaalslagroom = 0 
prijssprinkels = 0.30
totaalsprinkels = 0 
prijscaramel = 0.90
totaalcaramel = 0 
totaaltoppings = (totaalslagroom + totaalsprinkels + totaalcaramel)
hoeveelliter = 0 
liter = 9.80
percent = 6/100 
percentage = percent * 100 
btw = (hoeveelliter + liter + percent) 
import sys

def zakelijk():
    hoeveelliter = int(input("hoeveel liter wil je?"))
    if hoeveelliter >= 0: 
        print ("de prijs is dan", hoeveelliter, "x", liter, "+", btw, "en dat is", (hoeveelliter * liter + btw)) 
        sys.exit(0) 
    else:
        print ("dat snap ik niet")

def zakelijke_markt():
    z_or_p = input("bent u particulier of zakelijk?")
    if z_or_p == "particulier":
        return hoeveel 
    elif z_or_p == "zakelijk":
        return zakelijk() 
    else:
        print("dat snap ik niet")
print("welkom bij papigelato")  
zakelijke_markt() 

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
    totaal = (totaalbolletjes * prijsbolletjes) + (totaalbakje * prijsbakje) + ( totaalhoorntje * prijshoorntje) + (totaalslagroom) + (totaalcaramel) + (totaalsprinkels) 
    print("dat is dan",(totaalbolletjes), "x",(prijsbolletjes), "+" ,(totaalbakje), "x", (prijsbakje), "+", (totaalhoorntje), "x", (prijshoorntje), "+" , (totaaltoppings), "end dat is" ,(totaal))

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
            print("isorry , dat verkopen wij niet in deze salon") 

          
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
        toppings = input("welke topping wil je?")
        if toppings == "slagroom":
            totaalslagroom += 1
        elif toppings == "sprinkels":
            totaalsprinkels += 1
        elif toppings == "caramel":
            totaalcaramel += 1
            print("oke, dan is hier uw hoorntje met", (hoeveel), "bolletjes") 
            
        else:
            print("sorry dat verkopen wij niet in deze salon")
            
    elif hoeveel >= 3:
        allesmaken = ""
        for x in range(hoeveel):
            x += 1
            print(f"Geef de smaak voor bolletje {x} ")
            allesmaken = allesmaken + " " +  smaken()
        print(allesmaken)
        toppings = input("welke topping wil je?") 
        if toppings == "slagroom":
             totaalslagroom += 1
        elif toppings == "sprinkels":
             totaalsprinkels += 1
        elif toppings == "caramel":
             totaalcaramel += 1

        print ("oke, dan is hier uw bakje met",(hoeveel),"bollejes") 
        totaalbakje += 1 
 
    

    inputYesNo = input("Wil je nog meer bestellen?")
    if inputYesNo == "ja":
        print("Oke meer ijs")
    elif inputYesNo == 'nee':
        print (bonnetje()) 
        break 
    else: 
        print('Sorry dat is niet iets wat wij in deze salon aanbieden') 
    
 


     

    





