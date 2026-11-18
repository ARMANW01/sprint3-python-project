##################################################################
#4a)
for game in video_game_sales:
    if game[GLOBAL_SALES] > 25.00:
        print(game[NAME], game[GLOBAL_SALES])

###################################################################
#4b)
pre_2000_count = 0
for game in video_game_sales:
    if game[YEAR] < 2000:
        pre_2000_count = pre_2000_count + 1
print(pre_2000_count)

###################################################################
#4c)
NA_total = 0
JP_total = 0
for game in video_game_sales:
    NA_total = NA_total + game[NA_SALES]
    JP_total = JP_total + game[JP_SALES]
print(f'NA Total: {NA_total}')
print(f'JP Total: {JP_total}')

if NA_total > JP_total:
    print('NA had higher sales.')
elif JP_total > NA_total:
    print('JP had higher sales.')
else:
    print('NA and JP had equal sales.')
###################################################################
#4d)
nintendo_games = []
for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])
print(nintendo_games)
print(len(nintendo_games))
