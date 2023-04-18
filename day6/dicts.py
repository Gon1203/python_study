player = {
    "name": "gon",
    "age": 10,
    "alive": False,
    'favorite': ['🍕','🍔']
    }



print(player["age"])
print(player["name"])
print(player["alive"])


print(player)
player.pop('age')
player['xp'] = 1500
print(player)


player["favorite"].append('🎂')

print(player)