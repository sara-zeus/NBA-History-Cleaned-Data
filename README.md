This repository contains the dataset used for the 'Complete History Of The NBA' interactive application. The data is periodically updated and sourced from Basketball-Reference.com. The main dataset, 'nbaallelo.csv,' includes the following variables:

gameorder: Play order of games in NBA history.
game_id: Unique ID for each game.
lg_id: The league in which the game was played.
_iscopy: Flags if this game ID has already occurred for the opposing team in the same matchup.
year_id: Season ID, named based on the year in which the season ended.
date_game: Game date.
is_playoffs: Flag for playoff games.
team_id: Three-letter code for team names (from Basketball Reference).
fran_id: Franchise ID (multiple team IDs can fall under the same fran_id due to name changes or moves; the interactive is grouped by fran_id).
pts: Points scored by the team.
elo_i: Team Elo rating entering the game.
elo_n: Team Elo rating following the game.
win_equiv: Equivalent number of wins in an 82-game season for a team of elo_n quality.
opp_id: Team ID of the opponent.
opp_fran: Franchise ID of the opponent.
opp_pts: Points scored by the opponent.
opp_elo_i: Opponent Elo rating entering the game.
opp_elo_n: Opponent Elo rating following the game.
game_location: Game location (Home, Away, or Neutral).
game_result: Win or loss for the team in the team_id column.
forecast: Elo-based chances of winning for the team in the team_id column, based on Elo ratings and game location.
notes: Additional information. 
