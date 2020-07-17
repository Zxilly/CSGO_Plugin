from fastapi import FastAPI,Response
from typing import Optional
import json
import requests
from datetime import datetime

api_key = "A41CB32704D5547F3F4C23905FFEDEAB"

def render(player, rankid):
    kd = format(player.total_kills / player.total_deaths, '.2f')
    win_rate = format(player.total_wins_round / player.total_round * 100, '.2f')
    # print(player.total_wins_round,player.total_round)
    hit_rate = format(player.hits / player.fired * 100, '.2f')
    headshot_rate = format(player.total_head_kills / player.total_kills * 100, '.2f')
    last_kd = format(player.last_kill / player.last_death, '.1f')
    fav_hit_rate = format(player.last_favweapon_hits / player.last_favweapon_shots * 100, '.2f')

    # print(player.last_favweapon_id)
    # print(player.last_favweapon_hits)

    output = template_html.format(player.avatar_url, player.player_name, rankid, player.total_kills, kd, win_rate,
                                  hit_rate, headshot_rate, last_kd, player.win_status, player.last_t, player.last_ct,
                                  fav_hit_rate, player.last_mvp, player.last_kill, player.last_death,
                                  weapon_url_dict[player.last_favweapon_id])

    # print(output)
    return output

weapon_url_dict = {
    1: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_deagle.29e8f0d7d0be5e737d4f663ee8b394b5c9e00bdd.png",
    2: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_elite.6563e9d274c6e799d71a7809021624f213d5e080.png",
    3: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_fiveseven.7c33b4a78ae94a3d14e7cd0f71b295cf61717d75.png",
    4: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_glock.8430afea5349054d0923cefa7d2e7bf3950ce3d7.png",
    7: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_ak47.a320f13fea4f21d1eb3b46678d6b12e97cbd1052.png",
    8: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_aug.6b97a75aa4c0dbb61d81efb6d5497b079b67d0da.png",
    9: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_awp.2899e1c6345ed05d62bdbe112db1b117d022e477.png",
    10: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_famas.c897878873beb9e9ca4c68ef3a666869c6e78031.png",
    11: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_g3sg1.986d0e07f58c81c99aa5a47d86340f4c3d400339.png",
    13: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_galilar.b84153658afdb7dc26a9854e566fde3fc42c22ef.png",
    14: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_m249.02d1cf8fa8c41af5a43749bf780c4c4a2e50ea8e.png",
    16: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_m4a1.39b3bd8d556e5cdebb79d60902442986eb9aedff.png",
    17: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_mac10.41e40474aa21a9ed90d9b21dd5adf0910f766426.png",
    19: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_p90.15fedd7fc90f003b8de0ded36245b438d54bc3d2.png",
    23: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_mp5sd.2e92234c951819f3ae44742e96c488ef97f26c7c.png",
    24: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_ump45.55669e2321f28efed775be27f7e3c7e71b501520.png",
    25: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_xm1014.7bd7f3985d680db2fcb7cad32b07c90b758c234b.png",
    26: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_bizon.58523d37ee43b9a4ef42a67b65a28e5967743a56.png",
    27: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_mag7.5480ba05c61153309163c46e7d646d6958af9bf7.png",
    28: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_negev.1cf512eb01bd62bcae5c54feec694f418ab71d30.png",
    29: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_sawedoff.4c4df9c84e1edc20488c45061ad88cfd2460c4a5.png",
    30: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_tec9.74538566492b4af122be9b996bdd7d08585db3c0.png",
    31: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_taser.3c80d155bf0547c377217920f2c7329c8b00d472.png",
    32: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_hkp2000.c2221f8c2ef3df6c2fcdafd1bea9faae01f64054.png",
    33: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_mp7.0afc09868c38a00fde50c3e4943637c714e8981e.png",
    34: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_mp9.c9103efde0845eb715cdcb67bf74bad646b1c5bc.png",
    35: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_nova.d9063351d4233101d02def18aa7e901d02f9b4c1.png",
    36: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_p250.0bc9109121fb318a3bb18f6fa92692c7aa433205.png",
    37: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_shield.b4b0ca3e42b2e043cbba823de27bc199ad650da4.png",
    38: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_scar20.1552c7b64dfe9e542a3b730edb80e21dcc6d243d.png",
    39: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_sg556.74040869391ea2ab25777f3670a6015191a73e6c.png",
    40: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_ssg08.271a856f50fd6ac1014334098b1a43d61bddb892.png",
    41: "https://steamcdn-a.akamaihd.net/apps/730/icons/econ/weapons/base_weapons/weapon_knife.a07b900d79ea768eae1a217a2839c5727f760396.png",
}

template_html = """<meta content="width=device-width,user-scalable=0" name="viewport">
<link rel="stylesheet" href="https://api.learningman.top/static/css/csgo.css" type="text/css">
<div class="csgo-stat-box">
    <div class="head"><a class="user-link"><img
            src="{}">{}</a><img
            class="level" src="https://api.learningman.top/static/img/skillgroup{}.png"></div>
    <ul class="num-box">
        <li><span>{}</span><b>杀敌数</b></li>
        <li><span>{}</span><b>K/D</b></li>
        <li><span>{}%</span><b>胜率</b></li>
        <li><span>{}%</span><b>命中率</b></li>
        <li><span>{}%</span><b>爆头率</b></li>
    </ul>
    <div class="last-round-box"><h2>最近一场比赛</h2>
        <p class="kd-value">{}</p>
        <p class="score-value">{} {} / {}</p>
        <p class="stat-value"><span>命中率 {}%</span><span>MVP {}</span><span>击杀 {}</span><span>死亡 {}</span></p><img
                src="{}">
    </div>
</div>
    """

class Player(object):
    def __init__(self, steamid):
        self.steamid = steamid
        # self.rankid = rankid
        # self.get_game_info()
        self.get_player_info()

    def get_game_info(self):
        api1_info = {"appid": 730, "key": api_key, "steamid": self.steamid}
        api1_object = requests.get("https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/",
                                   params=api1_info)
        data1 = json.loads(api1_object.content)
        self.total_kills = data1['playerstats']['stats'][0]['value']
        self.total_head_kills = data1['playerstats']['stats'][25]['value']
        self.total_deaths = data1['playerstats']['stats'][1]['value']
        self.total_wins_round = data1['playerstats']['stats'][5]['value']
        self.total_round = data1['playerstats']['stats'][46]['value']
        self.hits = data1['playerstats']['stats'][44]['value']
        self.fired = data1['playerstats']['stats'][45]['value']
        self.last_kill = data1['playerstats']['stats'][87]['value']
        self.last_death = data1['playerstats']['stats'][88]['value']
        self.last_mvp = data1['playerstats']['stats'][89]['value']
        self.last_ct = data1['playerstats']['stats'][84]['value']
        self.last_t = data1['playerstats']['stats'][83]['value']
        last_win = data1['playerstats']['stats'][85]['value']
        if (self.last_ct > self.last_t):
            self.win_status = 'ct'
        elif (self.last_ct < self.last_t):
            self.win_status = 't'
        else:
            self.win_status = '平'
        if (last_win == self.last_ct):
            player_role = 'ct'
        else:
            player_role = 't'
        if (self.win_status == player_role and self.win_status != '平'):
            self.win_status = '胜'
        else:
            self.win_status = '负'
        self.last_favweapon_id = data1['playerstats']['stats'][90]['value']
        self.last_favweapon_shots = data1['playerstats']['stats'][91]['value']
        self.last_favweapon_hits = data1['playerstats']['stats'][92]['value']

        # num = 0
        # for one in data1['playerstats']['stats']:
        #    print(str(num)+" "+one['name']+" "+str(one['value']))
        #    num += 1

    def get_player_info(self):
        api2_info = {"key": api_key, "steamids": self.steamid}
        api2_object = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/",
                                   params=api2_info)
        data2 = json.loads(api2_object.content)
        # print(data2)
        self.player_name = data2['response']['players'][0]['personaname']
        self.avatar_url = data2['response']['players'][0]['avatarfull']
        self.logoff_time = data2['response']['players'][0]['lastlogoff']


def cache(player, rankid):
    steamid = player.steamid
    cache_path = './cache/{}.{}.json'.format(steamid, rankid)
    try:
        with open(cache_path, 'r+') as f:
            player_info = json.loads(f.read())
            if player_info['generate_time'] > player.logoff_time:
                return player_info['page_content']
            else:
                raise Exception('CacheExpiredError')
    except:
        player.get_game_info()
        render_content = render(player, rankid)
        write_cache(cache_path, render_content)
        return render_content


def write_cache(path, content):
    time_now = datetime.timestamp(datetime.utcnow())
    cache_content = {'generate_time': time_now, 'page_content': content}
    with open(path, 'w+') as f:
        f.write(json.dumps(cache_content))


app = FastAPI()

@app.get("/")
async def entry(steamid:str,rankid:int):
    a = Player(steamid)
    output = cache(a,rankid)
    return Response(content=output,media_type='text/html')