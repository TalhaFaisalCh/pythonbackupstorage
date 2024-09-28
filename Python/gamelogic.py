from FunctionsONLYasModules import calculate_distance
x1, y1, h1 = 10, 20, 50
x2, y2, h2 = 15, 25, 55

player_position = [x1, y1]      
enemy_position = [x2, y2]       


               
nust = (330, 720)           
comsats = (200, 500)        
talha = [336, 721]          
ayesha = [360, 321]        

print(int(calculate_distance(player_position, enemy_position)))
