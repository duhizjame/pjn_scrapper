from nba_api.stats.endpoints import shotchartdetail, ShotChartDetail,commonplayerinfo, hustlestatsboxscore
from nba_api.stats.static import players, teams
import json
import pandas as pd
import nbashots
import matplotlib.pyplot as plt

# player = players.find_players_by_full_name("Kobe Bryant")
# tatum = player[0]
# boston = teams.find_teams_by_full_name("Los Angeles Lakers")[0]
# print(boston)
# print(tatum)
# x = ShotChartDetail(boston['id'], tatum['id'])
# # pand = pd.DataFrame.from_records(data = json)
# # print(pand)
# # for player in players:
# #     json = ShotChartDetail(teams.find_team_name_by_id(player['id']), player['id'])
# #     print(json)
# #     # json = nba_api.stats.endpoints.ShotChartDetail(nba_api.stats.static.teams.find_teams_by_city("Boston"),)
# #     # print(json)
# # 
# labels = ['GRID_TYPE','GAME_ID','GAME_EVENT_ID',"PLAYER_ID","TEAM_ID",'SHOT_ATTEMPTED_FLAG','SHOT_MADE_FLAG']
# x = x.get_data_frames()[0]
# x = x.drop(columns = labels)
# x = x[(x.MINUTES_REMAINING < 3) & (x.PERIOD == 4)]
# print(x)
# # print(y)
# # print(y.EVENT_TYPE.unique())
# # y.describe
# nbashots.shot_chart(x.LOC_X,x.LOC_Y,kind="scatter",color="y",court_color='b')
# plt.show()
# print(x)

jharden = players.find_players_by_full_name("James Harden")[0]
x = hustlestatsboxscore.HustleStatsBoxScore('0041900221').get_data_frames()[1]

columns = ['GAME_ID',"TEAM_ID","TEAM_ABBREVIATION","TEAM_CITY","PLAYER_ID","START_POSITION",
            "COMMENT","MINUTES"]
labels = ['PLAYER_NAME',"PTS", "CONTESTED_SHOTS", "CONTESTED_SHOTS_2PT",
        "CONTESTED_SHOTS_3PT","DEFLECTIONS","CHARGES_DRAWN",
        "SCREEN_ASSISTS","SCREEN_AST_PTS","OFF_LOOSE_BALLS_RECOVERED","DEF_LOOSE_BALLS_RECOVERED","LOOSE_BALLS_RECOVERED",
        "OFF_BOXOUTS","DEF_BOXOUTS","BOX_OUT_PLAYER_TEAM_REBS","BOX_OUT_PLAYER_REBS","BOX_OUTS"]
# y = x.drop(columns = columns)
y = x[labels].sort_values(by=['CONTESTED_SHOTS'])
f = open('tekst.txt','w')
# print(y)
f.write(y.to_string())