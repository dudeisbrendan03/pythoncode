#imports
from random import randint

#names
v,b,br,n,m,be,an,oo,s,ss,t,w,c,d = "veda","brandon","bret","nitya","maggie","beau","angelina","oscar","siya","samay","troy","william","conrad","dristi"

#print intro
print("WELCOME TO DA SHIP GENERATOR\nMADE WITH 100% TRUTH\n")

#start
num1,num2=input("Enter a name: ")input("\nEnter another name: ")

x = randint(0, 100)
num1.lower();num2.lower()
num1 = num1.replace(" ","" );num2 = num2.replace(" ","" )


#changes #FIX
if num1.lower() == v and num2.lower() == b: #VedaBrandon
	x = 100
elif num2.lower() == v and num1.lower() == b:
	x = 100
	
if num1.lower() == v and num2.lower() != b: #VedaOthers
	x = randint(0, 100)
elif num2.lower() == v and num1.lower() != b:
	x = randint(0, 100)
	
if num1.lower() == m and num2.lower() == w: #MaggieWilliam
	x = 100
elif num2.lower() == m and num1.lower() == w:
	x = 100
	
if num1.lower() == m and num2.lower() != w: #MaggieOthers
	x = randint(0, 100)
elif num2.lower() == m and num1.lower() != w:
	x = randint(0, 100)
	
if num1.lower() == n and num2.lower() == br: #NityaBret
	x = 100
elif num2.lower() == n and num1.lower() == br:
	x = 100
	
if num1.lower() == n and num2.lower() != br: #NityaOthers
	x = 0
elif num2.lower() == n and num1.lower() != br:
	x = 0
	
if num1.lower() == s and num2.lower() == be: #SiyaBeau
	x = 100
elif num2.lower() == s and num1.lower() == be:
	x = 100
	
if num1.lower() == s and num2.lower() != be: #SiyaOthers
	x = randint(0, 100)
elif num2.lower() == s and num1.lower() != be:
	x = randint(0, 100)
	
if num1.lower() == d and num2.lower() == c: #ConradDristi
	x = 100
elif num2.lower() == d and num1.lower() == c:
	x = 100
	
if num1.lower() == d and num2.lower() != c: #DristiOthers
	x = randint(0, 100)
elif num2.lower() == d and num1.lower() != c:
	x = randint(0, 100)
	
#print ship
print(num1 + ' and ' + num2 + ' have a ', x, '% chance of being together')
print("")

#repeat start
num1=input("Enter a name: ")
num2=input("Enter another name: ")
x = randint(0, 100)

num1 = num1.replace(" ","" )
num2 = num2.replace(" ","" )

#changes
if num1.lower() == v and num2.lower() == b: #VedaBrandon
	x = 100
elif num2.lower() == v and num1.lower() == b:
	x = 100
	
if num1.lower() == v and num2.lower() != b: #VedaOthers
	x = randint(0, 100)
elif num2.lower() == v and num1.lower() != b:
	x = randint(0, 100)
	
if num1.lower() == m and num2.lower() == w: #MaggieWilliam
	x = 100
elif num2.lower() == m and num1.lower() == w:
	x = 100
	
if num1.lower() == m and num2.lower() != w: #MaggieOthers
	x = randint(0, 100)
elif num2.lower() == m and num1.lower() != w:
	x = randint(0, 100)
	
if num1.lower() == n and num2.lower() == br: #NityaBret
	x = 100
elif num2.lower() == n and num1.lower() == br:
	x = 100
	
if num1.lower() == n and num2.lower() != br: #NityaOthers
	x = 0
elif num2.lower() == n and num1.lower() != br:
	x = 0
	
if num1.lower() == s and num2.lower() == be: #SiyaBeau
	x = 100
elif num2.lower() == s and num1.lower() == be:
	x = 100
	
if num1.lower() == s and num2.lower() != be: #SiyaOthers
	x = randint(0, 100)
elif num2.lower() == s and num1.lower() != be:
	x = randint(0, 100)
	
if num1.lower() == d and num2.lower() == c: #ConradDristi
	x = 100
elif num2.lower() == d and num1.lower() == c:
	x = 100
	
if num1.lower() == d and num2.lower() != c: #DristiOthers
	x = randint(0, 100)
elif num2.lower() == d and num1.lower() != c:
	x = randint(0, 100)

#print ship
print(num1 + ' and ' + num2 + ' have a ', x, '% chance of being together')
print("")

#repeat start
num1=input("Enter a name: ")
num2=input("Enter another name: ")
x = randint(0, 100)

num1 = num1.replace(" ","" )
num2 = num2.replace(" ","" )

#changes
if num1.lower() == v and num2.lower() == b: #VedaBrandon
	x = 100
elif num2.lower() == v and num1.lower() == b:
	x = 100
	
if num1.lower() == v and num2.lower() != b: #VedaOthers
	x = randint(0, 100)
elif num2.lower() == v and num1.lower() != b:
	x = randint(0, 100)
	
if num1.lower() == m and num2.lower() == w: #MaggieWilliam
	x = 100
elif num2.lower() == m and num1.lower() == w:
	x = 100
	
if num1.lower() == m and num2.lower() != w: #MaggieOthers
	x = randint(0, 100)
elif num2.lower() == m and num1.lower() != w:
	x = randint(0, 100)
	
if num1.lower() == n and num2.lower() == br: #NityaBret
	x = 100
elif num2.lower() == n and num1.lower() == br:
	x = 100
	
if num1.lower() == n and num2.lower() != br: #NityaOthers
	x = 0
elif num2.lower() == n and num1.lower() != br:
	x = 0
	
if num1.lower() == s and num2.lower() == be: #SiyaBeau
	x = 100
elif num2.lower() == s and num1.lower() == be:
	x = 100
	
if num1.lower() == s and num2.lower() != be: #SiyaOthers
	x = randint(0, 100)
elif num2.lower() == s and num1.lower() != be:
	x = randint(0, 100)
	
if num1.lower() == d and num2.lower() == c: #ConradDristi
	x = 100
elif num2.lower() == d and num1.lower() == c:
	x = 100
	
if num1.lower() == d and num2.lower() != c: #DristiOthers
	x = randint(0, 100)
elif num2.lower() == d and num1.lower() != c:
	x = randint(0, 100)
	
#print ship
print("{} and {} have a {}% chance of being together.".format(num1,num2,x))


#repeat start
num1=input("Enter a name: ");num2=input("Enter another name: ")
x = randint(0, 100)
num1 = num1.replace(" ","" );num2 = num2.replace(" ","" )

#changes
if num1.lower() == v and num2.lower() == b: #VedaBrandon
	x = 100
elif num2.lower() == v and num1.lower() == b:
	x = 100
	
if num1.lower() == v and num2.lower() != b: #VedaOthers
	x = randint(0, 100)
elif num2.lower() == v and num1.lower() != b:
	x = randint(0, 100)
	
if num1.lower() == m and num2.lower() == w: #MaggieWilliam
	x = 100
elif num2.lower() == m and num1.lower() == w:
	x = 100
	
if num1.lower() == m and num2.lower() != w: #MaggieOthers
	x = randint(0, 100)
elif num2.lower() == m and num1.lower() != w:
	x = randint(0, 100)
	
if num1.lower() == n and num2.lower() == br: #NityaBret
	x = 100
elif num2.lower() == n and num1.lower() == br:
	x = 100
	
if num1.lower() == n and num2.lower() != br: #NityaOthers
	x = 0
elif num2.lower() == n and num1.lower() != br:
	x = 0
	
if num1.lower() == s and num2.lower() == be: #SiyaBeau
	x = 100
elif num2.lower() == s and num1.lower() == be:
	x = 100
	
if num1.lower() == s and num2.lower() != be: #SiyaOthers
	x = randint(0, 100)
elif num2.lower() == s and num1.lower() != be:
	x = randint(0, 100)
	
if num1.lower() == d and num2.lower() == c: #ConradDristi
	x = 100
elif num2.lower() == d and num1.lower() == c:
	x = 100
	
if num1.lower() == d and num2.lower() != c: #DristiOthers
	x = randint(0, 100)
elif num2.lower() == d and num1.lower() != c:
	x = randint(0, 100)

#print ship
print(num1 + ' and ' + num2 + ' have a ', x, '% chance of being together')
print("")

#repeat start
num1=input("Enter a name: ")
num2=input("Enter another name: ")
x = randint(0, 100)

num1 = num1.replace(" ","" )
num2 = num2.replace(" ","" )

#changes
if num1.lower() == v and num2.lower() == b: #VedaBrandon
	x = 100
elif num2.lower() == v and num1.lower() == b:
	x = 100
	
if num1.lower() == v and num2.lower() != b: #VedaOthers
	x = randint(0, 100)
elif num2.lower() == v and num1.lower() != b:
	x = randint(0, 100)
	
if num1.lower() == m and num2.lower() == w: #MaggieWilliam
	x = 100
elif num2.lower() == m and num1.lower() == w:
	x = 100
	
if num1.lower() == m and num2.lower() != w: #MaggieOthers
	x = randint(0, 100)
elif num2.lower() == m and num1.lower() != w:
	x = randint(0, 100)
	
if num1.lower() == n and num2.lower() == br: #NityaBret
	x = 100
elif num2.lower() == n and num1.lower() == br:
	x = 100
	
if num1.lower() == n and num2.lower() != br: #NityaOthers
	x = 0
elif num2.lower() == n and num1.lower() != br:
	x = 0
	
if num1.lower() == s and num2.lower() == be: #SiyaBeau
	x = 100
elif num2.lower() == s and num1.lower() == be:
	x = 100
	
if num1.lower() == s and num2.lower() != be: #SiyaOthers
	x = randint(0, 100)
elif num2.lower() == s and num1.lower() != be:
	x = randint(0, 100)
	
if num1.lower() == d and num2.lower() == c: #ConradDristi
	x = 100
elif num2.lower() == d and num1.lower() == c:
	x = 100
	
if num1.lower() == d and num2.lower() != c: #DristiOthers
	x = randint(0, 100)
elif num2.lower() == d and num1.lower() != c:
	x = randint(0, 100)

#print ship
print(num1 + ' and ' + num2 + ' have a ', x, '% chance of being together')
print("")

