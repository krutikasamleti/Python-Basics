#Problem 1
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

# problem 2 
import pyttsx3
engine = pyttsx3.init()
engine.say("Hey how are you?")
engine.runAndWait()

# problem 3
import os
dir_path = '/'
contents = os.listdir(dir_path)
print(contents)



# Chapter 2 Problems

a = 12
b = 5

print("Remainder is:",a%b)\

a = int(input("Enter the no:"))
print(type(a))

a = 80
b = 43

c= a > b
print("is a is greater than b:",c)

# Average no
a = float(input("Enter the 1 no: "))
b = float(input("Enter the 2 no: "))

avg = (a+b)/2
print("Average number:",avg)

# Square of number
a = int(input("Enter the no: "))
sq = a*a
print("Square of a number",(a**2))  # a^2 invalid to find square


#Problem 3
name = input("Enter your name: ")
print(f"How are you? {name}")

name = input("name: ")
date = int(input("date: "))
print(f"Dear {name},\nYou are Selected!\n{date}")


# Problem 4
letter ="""Dear <Name>,
    You are Selected!
    <Date>"""

print(letter.replace("<Name>","Krutika").replace("<Date>","8 January 2027"))


# Problem 5  detect double spaces
spaces = "Hello how  are you  doing?  "
print(spaces.find("  "))


# problem 6 replace the double apce with single space
str = "hi im  a proffesor  in your  university  !"
print(str.replace("  "," "))


# problem 7 wap to format text using escape sequence characters
text = "Dear Krutika,\nyou are Selected,\nfor the role\t\"AI Engineer Intern\",\nGlad to Welcome you to the Team.\nBest Wishes."
print(text)