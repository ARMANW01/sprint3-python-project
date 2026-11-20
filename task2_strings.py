#2a)
game_name = video_game_sales[4][NAME]
print(game_name[:7])

##########################################################

#2b) 
messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']
for name in messy_names:
    clean_name = name.strip().lower()
    print(clean_name)

##########################################################

#2c)
top_game = video_game_sales[0]
print(f'#{top_game[RANK]} Best Seller: {top_game[NAME]} ({top_game[YEAR]}) - ${top_game[GLOBAL_SALES]}M global sales')
