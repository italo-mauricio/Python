import random

def trigger_random():
    speed = ["fast", "slow"]
    triggers = ["hand sounds", "tapping", "mouth sounds", "stop sound", "fabric scratching", 
    "head massage", "gloves"]
    speed_choice = random.choice(speed)
    triggers_choice = random.choice(triggers)
    
    return speed_choice, triggers_choice

trigger_random()
print(trigger_random())