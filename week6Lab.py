"""Week 6 fix broken code"""

player_health = 100

def take_damage(current_health):
 player_health = current_health - 20
 print("Player took damage!")
 return player_health

player_health = take_damage(player_health)

print(f"Player health is: {player_health}")