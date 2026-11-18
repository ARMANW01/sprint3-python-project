##################################################################################
#6a)
def calculate_total_sales(game):
    total = game[NA_SALES] + game[EU_SALES] + game[JP_SALES]
    return total
print(calculate_total_sales(video_game_sales[0]))

#################################################################################
#6b)
def filter_by_genre(data,genre = 'Platform'):
    filtered_games = []
    for game in data:
        if game[GENRE] == genre:
            filtered_games.append(game)
    return filtered_games
print(f'Platform games: {len(filter_by_genre(video_game_sales))}')
print(f'Sports games: {len(filter_by_genre(video_game_sales,"Sports"))}')

##################################################################################
#6c)
def get_summary(game):
    return f'{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]:.2f}M'
for game in video_game_sales:
    print(get_summary(game))
