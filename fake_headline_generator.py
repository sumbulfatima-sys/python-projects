# 1- impport the random module 
import random 


# 2- create subjects
subjects = [
    "shahrukh khan",
    "virat kholi",
    "A mumbai cat",
    "A group of monkey",
    "prime minister modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "lanchues",
    "cancels",
    "dances with",
    "eats",
    "order",
    "celebrates",
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plote of samosa",
    "inside parliament",
    "during IPL match",
    "at INdia gate"
]

# 3 start the headline generation loop 
while True:
    subject = random.choice(subjects) 
    action = random.choice(actions)  
    place_or_things = random.choice(places_or_things)
      
      
    headline = f" BREKING NEWS: {subject} {action} {place_or_things}"
    print("\n"+ headline)
    user_input = input("\nDO you want another headline? (yes/no)").strip()
    if user_input =="no":
        break



#print goodbye message
print("\nthanks for using the fake news headline generator .have a fun day")
    
                                