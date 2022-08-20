import random

players = {0:{"Round Total":0,"Game Total":0,"Name":""},
         1:{"Round Total":0,"Game Total":0,"Name":""},
         2:{"Round Total":0,"Game Total":0,"Name":""},
        }

for i in range(0,3):
    players[i]["Round Total"] = 0
    init_player = random.choice(list(players.keys()))

print(init_player)

for i in range(0,3):
    print(players[i]["Round Total"])


# 11,Lose a turn
# 19,Bankrupt