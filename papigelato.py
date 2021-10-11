def smaken():
    print("""De Smaken zijn
A = Aardbei
B = Vanille
C = Chocolade""")
    antwoordSmaken = input("Welke Smaak: ")
    if antwoordSmaken.lower() == "a":
        return "Aardbei"
    elif antwoordSmaken.lower() == "b": 
        return "vanille"
    elif antwoordSmaken.lower() == "c":
        return "chocolade" 
    


def nogmeer():
        nogmeerbestellen = input("wilt u nog meer bestellen?")
        if nogmeerbestellen == ("ja"):
            return bolletjes() 
        elif nogmeerbestellen == ("nee"):
            print("bedankt en tot ziens!!") 
        else:
            print("sorry, dat snap ik niet, kunt u de winkel verlaten alstublief?") 

def bolletjes():
    hoeveel = int(input("hoeveel bolletjes wil je?"))
    if hoeveel > 8:
        print("sorry zon grote bak hebben wij niet") 
        print(str(nogmeer()))
    
    elif hoeveel <= 4:
        allesmaken = ""
        for x in range(hoeveel):
            x += 1
            print(f"Geef de smaak voor bolletje {x} ")
            allesmaken = allesmaken + " " +  smaken()
        print(allesmaken)  
        bakofhoorntje = input("wilt u een bak of een hoorntje") 
        if bakofhoorntje == ("bakje"):
            print("oke, dan is hier uw bakje met", (hoeveel),"bolletjes")  
            print(str(nogmeer()))
        elif bakofhoorntje == ("hoorntje"): 
            print("oke, dan is hier uw hoorntje met", (hoeveel), "bollejtes") 
            print(str(nogmeer()))
        else:
            print("sorry dat snap ik niet")
            print(str(nogmeer()))
    elif hoeveel >= 3:
        allesmaken = ""
        for x in range(hoeveel):
            x += 1
            print(f"Geef de smaak voor bolletje {x} ")
            allesmaken = allesmaken + " " +  smaken()
        print(allesmaken)
        print ("oke, dan is hier uw bakje met",(hoeveel),"bollejes") 
        print(str(nogmeer())) 
    

print (str(bolletjes()))




