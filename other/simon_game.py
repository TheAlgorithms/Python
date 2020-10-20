#this is code for the arduino circuit.


import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import random

#GPIO's
b0 = "P8_7"
b1 = "P8_8"
b2 = "P8_9"
b3 = "P8_10"
l0 = "P8_13"
l1 = "P8_14"
l2 = "P8_15"
l3 = "P8_16"

#LED VECTOR
LEDS = [l0,l1,l2,l3]

game_sequence = []
player_sequence = []

GPIO.setup(b0, GPIO.IN)
GPIO.setup(b1, GPIO.IN)
GPIO.setup(b2, GPIO.IN)
GPIO.setup(b3, GPIO.IN)
GPIO.setup(l0, GPIO.OUT)
GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2, GPIO.OUT)
GPIO.setup(l3, GPIO.OUT)

GPIO.add_event_detect(b0, GPIO.FALLING)
GPIO.add_event_detect(b1, GPIO.FALLING)
GPIO.add_event_detect(b2, GPIO.FALLING)
GPIO.add_event_detect(b3, GPIO.FALLING)

current_round = 1
game_started = False

def blink(led,tempo):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(tempo)
    GPIO.output(led, GPIO.LOW)
    time.sleep(tempo)

def flag():
    blink(l0,0.5)
    blink(l1,0.5)
    blink(l2,0.5)
    blink(l3,0.5)

def generate_current_round():
    #Start with 1 led e add more one every round
    #for cont in range(0,current_round):
    current_led = random.randint(0,3)
    game_sequence.append(current_led)
    for count in range(0,current_round):
        blink(LEDS[game_sequence[count]],0.5)
        #add leds in the sequence    

def get_play():
    if(current_round > 1):
        del player_sequence[:]
    
    number_of_plays = 0
    play_time_begin = time.time() #Return the number of seconds since epoch
    play_time_end = time.time()
    # Player got 3 seconds for every led in the sequence on every round 
    while((play_time_end - play_time_begin) < current_round + 3):

        if(GPIO.input(b0)):
            player_sequence.append(0)
            number_of_plays += 1
            print("B0")
            time.sleep(0.25)

        if(GPIO.input(b1)):
            player_sequence.append(1)
            number_of_plays += 1
            print("B1")
            time.sleep(0.25)

        if(GPIO.input(b2)):
            player_sequence.append(2)
            number_of_plays += 1
            print("B2")
            time.sleep(0.25)

        if(GPIO.input(b3)):
            player_sequence.append(3)
            number_of_plays += 1
            print("B3")
            time.sleep(0.25)

        play_time_end = time.time()
        if(number_of_plays == current_round):
            break
    if(number_of_plays < current_round):
        while True:
            blink(l0,0.1)
        
def validate_current_round():
    for i in range(0,current_round):
        if(player_sequence[i] != game_sequence[i]):
            return(False)
    return(True)

while True:
    #Press any button to start
    while(GPIO.input(b0) or GPIO.input(b1) or GPIO.input(b2) or GPIO.input(b3)):
        #Show some standart sequence
        flag()
        #flag game_started
        game_started = True
        #Game loop
        while game_started:
            
            generate_current_round()    
            
            #Detect player's play
            get_play()

            #TO DEBUG
            #print(game_sequence)
            #print(player_sequence)

            if(not(validate_current_round())):
                while True:
                    blink(l0,0.1)

            flag()
            current_round += 1