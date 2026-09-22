import random
from pycaw.pycaw import AudioUtilities
from playsound3 import playsound

vampire_hp = 200
x = random.randint(1, 5)


def set_volume_to_100():
    try:
        # 1. Get the default audio playback device
        device = AudioUtilities.GetSpeakers()

        # 2. Extract the advanced volume management tools
        volume = device.EndpointVolume

        # 3. Explicitly UNMUTE (0 means false / unmuted)
        volume.SetMute(0, None)

        # 4. Set the percentage slider to 100
        device.volume_percent = 100

    except Exception as e:
        print(f"Could not change volume: {e}")


# Automatically force volume to 100% if the big boss is rolled
if x == 2:
    set_volume_to_100()


def bigroundboss():
    print("you hear the roar")
    try:
        playsound("bigroundboss.wav")
    except Exception as e:
        print("Could not find bigroundboss.wav file.")


# --- ENCOUNTER CHAIN ---
if x == 1:
    print("you have encountered a vampire knight")
elif x == 2:
    print("you have encountered a big boss ")
elif x == 3:
    print("you have encountered zombie")
elif x == 4:
    print("you have encountered jacky ")
elif x == 5:
    print("you have encountered saber")

# --- COMBAT LOGIC ---
if x == 1:
    while vampire_hp > 0:
        print("\nvampire hp is " + str(vampire_hp))
        print("1. attack")
        print("2. skill")
        print("3. block")
        print("4. item")
        act = input("what will you do? ")

        if act == "1":
            vampire_hp = (vampire_hp - 30)
            print("you dealt 30 damage")
        elif act == "2":
            vampire_hp = (vampire_hp - 60)
            print("you used a skill and dealt 60 damage!")

        if vampire_hp <= 0:
            print("you have defeated the enemy")

if x == 2:
    print("you have entered the big bosses chambers.")
    bigroundboss()