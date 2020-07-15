import json

import requests

from pri import *

from data import *

class Player(object):
    def __init__(self, steamid):
        self.steamid = steamid
        # self.rankid = rankid
        self.get_game_info()
        self.get_player_info()

    def get_game_info(self):
        api1_info = {"appid": 730, "key": api_key, "steamid": self.steamid}
        api1_object = requests.get("https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/",
                                   params=api1_info)
        data1 = json.loads(api1_object.content)
        self.total_kills = data1['playerstats']['stats'][0]['value']
        self.total_head_kills = data1['playerstats']['stats'][0]['value']
        self.total_deaths = data1['playerstats']['stats'][1]['value']
        self.total_wins_round = data1['playerstats']['stats'][6]['value']
        self.total_round = data1['playerstats']['stats'][46]['value']
        self.hits = data1['playerstats']['stats'][44]['value']
        self.fired = data1['playerstats']['stats'][45]['value']
        self.last_kill = data1['playerstats']['stats'][87]['value']
        self.last_death = data1['playerstats']['stats'][88]['value']
        self.last_mvp = data1['playerstats']['stats'][89]['value']
        last_ct = data1['playerstats']['stats'][85]['value']
        last_t = data1['playerstats']['stats'][84]['value']
        last_win = data1['playerstats']['stats'][86]['value']
        if (last_ct > last_t):
            win_status = 'ct'
        elif (last_ct < last_t):
            win_status = 't'
        else:
            self.win_status = '平'
        if (last_win == last_ct):
            player_role = 'ct'
        else:
            player_role = 't'
        if (self.win_status==player_role and self.win_status != '平'):
            self.win_status = '胜'
        else:
            self.win_status = '负'
        self.last_favweapon_id = data1['playerstats']['stats'][91]['value']
        self.last_favweapon_shots = data1['playerstats']['stats'][92]['value']
        self.last_favweapon_hits = data1['playerstats']['stats'][73]['value']

        #num = 0
        #for one in data1['playerstats']['stats']:
            # print(str(num)+" "+one['name']+" "+str(one['value']))
        #    num += 1
            # if(20000<one['value'] and one['value']<40000):
        #    print(str(num) + " " + one['name'] + " " + str(one['value']))

    def get_player_info(self):
        api2_info = {"key": api_key, "steamids": self.steamid}
        api2_object = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/",
                                   params=api2_info)
        data2 = json.loads(api2_object.content)
        #print(data2)
        self.player_name = data2['response']['players'][0]['personaname']
        self.avatar_url = data2['response']['players'][0]['avatarfull']
        self.logoff_time = data2['response']['players'][0]['lastlogoff']
        # print(self.player_name,self.avatar_url)
