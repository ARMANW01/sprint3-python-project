#1a)
total_games = len(video_game_sales)
print(total_games)

##################################################################

#1b)
total_sales = 0
for game in video_game_sales:
    total_sales = total_sales + game[9]
avg_global_sales = total_sales / len(video_game_sales)
print("Average Global Sales:", avg_global_sales)

####################################################################

#1c)
top_game_sales = video_game_sales[0][9]
top_game_share = (top_game_sales/total_sales)*100
print('Wii Sports Percentage:', top_game_share)
