#variables
#int

import math
import random
import re

age = 25

print(f"your age is {age} years old")
#float

distance =4.55
print(f"your distance is {distance} km")


#string
name = "tesfaye"
email = "tesfaye@gmail.com"

print(f"your name  is {name} and your email is {email}")

#boolean

is_online = True
game_running = False
is_logged_in = True

print(f"is online: {is_online}")
print(f"game running: {game_running}")
print(f"is logged in: {is_logged_in}")


if not is_online:
    print(f"{name} is offline")
else:
    print(f"{name} is online but your age is {age} not good for your health")



a=10
b=20
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")



#lsts
iceicrems =["vanilla","chocolate","strawberry","mango","banana"]
print(iceicrems[0])
print(iceicrems[1])
print(iceicrems[2])
print(iceicrems[3])
print(iceicrems[4])


iceicrems.append("nothing")
print(iceicrems)

iceicrems[3]="kiwi"
print(iceicrems)




#dictionaries
#keys/values

dictuser = {
    "name":"tesfaye",
    "age":25,
    "email":"tesfaye@gmail"
}
print(dictuser)
print(dictuser["name"])
dictuser["age"]=26
print(dictuser["age"])


x=10.4567843
print(f"{x:.2f}")

print(math.floor(x)) #rounds down to the nearest integer
print(math.ceil(x)) #rounds up to the nearest integer
print(math.trunc(x)) #removes the decimal part
print(round(x))  #rounds to the nearest integer
print(str(x)) #converts to string


y=78
print(math.sqrt(y)) #returns the square root of y
print(math.pow(y,2)) #returns y to the power of 2
print(f"{math.log(y):.2f}") #returns the natural logarithm of y
print(f"{math.cos(y):.2f}") #returns the cosine of y
print(f"{math.sin(y):.2f}") #returns the sine of y
print(f"{math.tan(y):.2f}") #returns the tangent of y


z=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(z)) #returns a random element from the list
print(random.randint(1,100)) #returns a random integer between 1 and 100

v = int(input("enter a number between 1 and 100: "))
output = random.randint(1,100)
print(f"the random number is {output}") #prints the random number (output)

if output > v:
    print("you won")
elif output == v:
    print("double your money")
else:
    print("you lost")

#strings
phone = input("enter your phone number: ")
print(f"your phone number is {phone}")

phone_number = "+251/00/987/87/87" #phone number
print(phone_number.replace("/","-"))


phone_n = "+49 (176) 123-4567"
print(phone_n.replace("+","").replace("(","").replace(")","").replace("-","").replace(" ",""))


#using REGEX
phone_x = "+49 (176) 123-4567"

cleaned =re.sub(r"[+\s()\-]","",phone_x)
result =(f"00{cleaned}")
print(result)

csv_file = "Tesfaye,25,tesfaye@gmail.com"
print(csv_file.split(","))
name,age,email = csv_file.split(",")
print(name)
print(age)
print(email)


#transformation
print("=" * 30)



#indexing and slicing

luck = "Tesfaye Dejene"
print (luck[0])
print (luck[1])
print (luck[2])
print(luck[0:4])
print(luck[:4])
print(luck[4:])
print(luck[::2])#prints every other character
print(luck[::-1])#reverses the string

print(luck.upper())
print(luck.lower())
print(luck.split(" "))

print(luck[0:8:2])

#whitespace cleaning
message = "   hello world!   "
print(message.strip())
print(message.lstrip())
print(message.rstrip())


import re

pack = "968-Maria, ( D@t@ Engineer );; 27y..".strip()

# Extract parts
name = re.search(r"-(\w+)", pack).group(1).lower()          # Maria → maria
role = re.search(r"\(\s*(.*?)\s*\)", pack).group(1)          # D@t@ Engineer
role = re.sub(r"[^a-zA-Z\s]", "", role).lower().strip()      # data engineer
age  = re.search(r"(\d+)y", pack).group(1)                   # 27

# Final format
result = f"name: {name} | role: {role} | age:{age}"
print(result)



