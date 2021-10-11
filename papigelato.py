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
        print ("oke, dan is hier uw bakje met",(hoeveel),"bollejes") 
        print(str(nogmeer())) 
    

print (str(bolletjes()))




