from fastapi import FastAPI
import random
import json
from pydantic import BaseModel

file = open("history.json", "r")
text = file.read()
data = json.loads(text)
file.close()

data["history"] += {"hello": "world"}

print(data)

app = FastAPI()

class SimulatedGame(BaseModel):
    choice1: str
    choice2: str

@app.get("/")
async def root():
    return {"message": "Hello, World"}

option = [
    "Rock",
    "Fire",
    "Scissors",
    "Sponge",
    "Paper",
    "Air",
    "Water",
]

"""
Rock = 0
Fire = 1
Scissors = 2
Sponge = 3
Paper = 4
Air = 5
Water = 6
"""

def rps(playerPick, computerPick=None):
    if computerPick == None:
        computerPick = random.randint(0, 6)

    playerWin = False

    if computerPick == playerPick:
        return {"TIE!!!": ""}
    
    elif (computerPick == 0) and (playerPick == 1 or playerPick == 2 or playerPick == 3):
        playerWin = False

    elif (computerPick == 0) and (playerPick == 4 or playerPick == 5 or playerPick == 6):
        playerWin = True

    elif (computerPick == 1) and (playerPick == 2 or playerPick == 3 or playerPick == 4):
        playerWin = False

    elif (computerPick == 1) and (playerPick == 5 or playerPick == 6 or playerPick == 0):
        playerWin = True

    elif (computerPick == 2) and (playerPick == 3 or playerPick == 4 or playerPick == 5):
        playerWin = False

    elif (computerPick == 2) and (playerPick == 6 or playerPick == 0 or playerPick == 1):
        playerWin = True

    elif (computerPick == 3) and (playerPick == 4 or playerPick == 5 or playerPick == 6):
        playerWin = False

    elif (computerPick == 3) and (playerPick == 0 or playerPick == 1 or playerPick == 2):
        playerWin = True

    elif (computerPick == 4) and (playerPick == 5 or playerPick == 6 or playerPick == 0):
        playerWin = False

    elif (computerPick == 4) and (playerPick == 1 or playerPick == 2 or playerPick == 3):
        playerWin = True
    
    elif (computerPick == 5) and (playerPick == 6 or playerPick == 0 or playerPick == 1):
        playerWin = False

    elif (computerPick == 5) and (playerPick == 2 or playerPick == 3 or playerPick == 4):
        playerWin = True

    elif (computerPick == 6) and (playerPick == 0 or playerPick == 1 or playerPick == 2):
        playerWin = False

    elif (computerPick == 6) and (playerPick == 3 or playerPick == 4 or playerPick == 5):
        playerWin = True


    return {"playerPick": option[playerPick], "cpuPick": option[computerPick], "playerWin": playerWin}

@app.get("/play/rock")
def rock():
    return rps(0)
    
@app.get("/play/fire")
def fire():
    return rps(1)

@app.get("/play/scissors")
def scissors():
    return rps(2)

@app.get("/play/sponge")
def sponge():
    return rps(3)

@app.get("/play/paper")
def paper():
    return rps(4)

@app.get("/play/air")
def air():
    return rps(5)

@app.get("/play/water")
def water():
    return rps(6)

@app.post("/simulate")
def simulate(simulatedGame: SimulatedGame):
    return rps(options.index(simulatedGame.choice1), options.index(simulatedGame.choice2))