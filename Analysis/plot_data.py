import pandas as pd
import matplotlib.pyplot as plt

file_path = "../Data/pokemon.csv"

#Relevant columns
battle_stats = ['hp','attack','defense','sp_attack','sp_defense','speed']
misc_stats = ['base_egg_steps','base_happiness','base_total','capture_rate','experience_growth','height_m','percentage_male','weight_kg']
classification = ['abilities','classfication','type1','type2','generation','is_legendary']

#All pokemon types, 18 total
pokemon_types = ['dark', 'psychic', 'electric', 'ghost', 'rock', 'ice', 'poison', 'normal', 'steel', 'fighting', 'fairy', 'fire', 'grass', 'water', 'ground', 'flying', 'bug', 'dragon']


df = pd.read_csv(file_path, index_col = "pokedex_number")


#Test for normal pokemon
plt.hist(df[(df.type1 == 'normal') | (df.type2 == 'normal')]['hp'])
plt.show()
