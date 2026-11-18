######################################################################
#3a)
game_names = []
for game in video_game_sales[:20]:
    game_names.append(game[1])
print(game_names)

######################################################################
#3b)

video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

######################################################################
#3c)

dataset_info = (len(video_game_sales), len(video_game_sales[0]), 'Video Game Sales')
print(dataset_info)
#A tuple is more appropiate in this case because tuples are NOT mutable. This allows our dataset to be more protected.
