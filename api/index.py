import base64
import json
from datetime import datetime

import requests
import uvicorn
from fastapi import FastAPI, Response

rand = "A41CB32704D5547F3F4C23905FFEDEAB"


def img2base64(inputInfo, rank=False, weapon=False):
    if rank:
        with open('./page/img/skillgroup' + str(inputInfo) + '.png', 'rb') as f:
            b64data = base64.b64encode(f.read())
            return b64data.decode()
    elif weapon:
        with open(f'./page/base64/{inputInfo}', 'rb') as f:
            a = f.read()
        return a.decode()
    else:
        return base64.b64encode(requests.get(inputInfo).content).decode()


def render(player, rankid, svg=False):
    kd = format(player.total_kills / player.total_deaths, '.2f')
    win_rate = format(player.total_wins_round / player.total_round * 100, '.2f')
    # print(player.total_wins_round,player.total_round)
    hit_rate = format(player.hits / player.fired * 100, '.2f')
    headshot_rate = format(player.total_head_kills / player.total_kills * 100, '.2f')
    last_kd = format(player.last_kill / player.last_death, '.1f')
    fav_hit_rate = format(player.last_favweapon_hits / player.last_favweapon_shots * 100, '.2f')

    # print(player.last_favweapon_id)
    # print(player.last_favweapon_hits)

    if not svg:
        output = template_html.format(player.avatar_url, player.player_name, rankid, player.total_kills, kd, win_rate,
                                      hit_rate, headshot_rate, last_kd, player.win_status, player.last_t,
                                      player.last_ct,
                                      fav_hit_rate, player.last_mvp, player.last_kill, player.last_death,
                                      weapon_url_dict[player.last_favweapon_id])

    else:
        output = template_html_svg.format(img2base64(player.avatar_url),
                                          player.player_name,
                                          img2base64(rankid, rank=True),
                                          player.total_kills,
                                          kd,
                                          win_rate,
                                          hit_rate,
                                          headshot_rate,
                                          last_kd,
                                          player.win_status,
                                          player.last_t,
                                          player.last_ct,
                                          fav_hit_rate,
                                          player.last_mvp,
                                          player.last_kill,
                                          player.last_death,
                                          img2base64(player.last_favweapon_id, weapon=True))
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

template_html = """<meta content="width=device-width,user-scalable=0" name="viewport"/>
<link rel="stylesheet" href="https://api.learningman.top/static/css/csgo.css" type="text/css"/>
<div class="csgo-stat-box">
    <div class="head"><a class="user-link"><img
            src="{}"/>{}</a><img
            class="level" src="https://api.learningman.top/static/img/skillgroup{}.png"/></div>
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
                src="{}"/>
    </div>
</div>
    """

template_html_svg = """<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="500px" height="220px">
    <title>CSGO Plugin</title>
    <foreignObject width="500" height="220">
        <div xmlns="http://www.w3.org/1999/xhtml" style="margin:0;height:100%;width:100%">
            <meta content="width=device-width,user-scalable=0" name="viewport"/>
            <style>
                div {{
                background: #2F3545;
                color: #FFF;
                font: 12px sans-serif;
                }}

                body,
                div,
                h2,
                p {{
                margin: 0;
                }}

                .csgo-stat-box {{
                overflow: hidden;
                }}

                .csgo-stat-box .head {{
                padding: 10px;
                }}

                .csgo-stat-box .head .user-link {{
                font-size: 24px;
                line-height: 36px;
                }}

                .csgo-stat-box .head .user-link img {{
                width: 36px;
                height: 36px;
                border-radius: 2px;
                vertical-align: top;
                margin-right: 10px;
                }}

                .csgo-stat-box .head .level {{
                float: right;
                height: 36px;
                }}

                .csgo-stat-box .num-box {{
                margin: 0 -30px 0 0;
                list-style-type: none;
                padding: 5px 0 5px 5px;
                overflow: hidden;
                background: #111;
                text-shadow: 0 1px 0 #000;
                }}

                .csgo-stat-box .num-box li {{
                float: left;
                padding: 5px 10px;
                margin-right: 10px;
                }}

                .csgo-stat-box .num-box li:last-child {{
                margin-right: 0;
                padding-right: 0;
                }}

                .csgo-stat-box .num-box li span {{
                display: block;
                font-size: 24px;
                line-height: 28px;
                font-weight: 100;
                }}

                .csgo-stat-box .num-box li b {{
                display: block;
                font-style: 12px;
                line-height: 18px;
                font-weight: 200;
                color: #8A9EA7;
                }}

                .csgo-stat-box .last-round-box {{
                position: relative;
                text-align: right;
                padding: 10px 17px;
                }}

                .csgo-stat-box .last-round-box h2 {{
                font-size: 12px;
                line-height: 22px;
                font-weight: 200;
                color: #8A9EA7;
                background: #111;
                position: absolute;
                top: 15px;
                left: 50%;
                padding: 0 7px;
                border-radius: 2px;
                margin-left: -43px;
                }}

                .csgo-stat-box .last-round-box p.kd-value {{
                font-size: 21px;
                line-height: 34px;
                font-weight: 200;
                }}

                .csgo-stat-box .last-round-box p.kd-value:before {{
                content: 'KD ';
                }}

                .csgo-stat-box .last-round-box p.score-value,
                .csgo-stat-box .last-round-box p.stat-value {{
                line-height: 14px;
                padding: 4px 0;
                color: #8A9EA7;
                }}

                .csgo-stat-box .last-round-box p.score-value span,
                .csgo-stat-box .last-round-box p.stat-value span {{
                display: inline-block;
                }}

                .csgo-stat-box .last-round-box p.score-value span:after,
                .csgo-stat-box .last-round-box p.stat-value span:after {{
                content: '|';
                display: inline-block;
                padding: 0 10px;
                opacity: .5;
                }}

                .csgo-stat-box .last-round-box p.score-value span:last-child:after,
                .csgo-stat-box .last-round-box p.stat-value span:last-child:after {{
                content: none;
                }}

                .csgo-stat-box .last-round-box img {{
                height: 86px;
                position: absolute;
                top: 0;
                left: 10px;
                }}

                .csgo-stat-box .cp {{
                position: absolute;
                left: 0;
                bottom: 0;
                margin: 4px;
                font-size: 12px;
                line-height: 12px;
                color: #8A9EA7;
                transform: scale(.8);
                opacity: .5;
                }}

                @media (max-width: 400px) {{
                .csgo-stat-box .num-box li {{
                padding: 5px;
                margin-right: 10px;
                }}
                }}

                @media (max-width: 320px) {{
                .csgo-stat-box .num-box {{
                zoom: .95;
                }}
                }}
            </style>
            <div class="csgo-stat-box">
                <div class="head">
                    <a class="user-link"><img
                            src="data:image/jpeg;base64,{}"/>{}
                    </a>
                    <img
                            class="level" src="data:image/png;base64,{}"/>
                </div>
                <ul class="num-box">
                    <li>
                        <span>{}</span>
                        <b>杀敌数</b>
                    </li>
                    <li>
                        <span>{}</span>
                        <b>K/D</b>
                    </li>
                    <li>
                        <span>{}%</span>
                        <b>胜率</b>
                    </li>
                    <li>
                        <span>{}%</span>
                        <b>命中率</b>
                    </li>
                    <li>
                        <span>{}%</span>
                        <b>爆头率</b>
                    </li>
                </ul>
                <div class="last-round-box">
                    <h2>最近一场比赛</h2>
                    <p class="kd-value">{}</p>
                    <p class="score-value">{} {} / {}</p>
                    <p class="stat-value">
                        <span>命中率 {}%</span>
                        <span>MVP {}</span>
                        <span>击杀 {}</span>
                        <span>死亡 {}</span>
                    </p>
                    <img
                            src="data:image/png;base64,{}"/>
                </div>
            </div>
        </div>
    </foreignObject>
</svg>
    """


class Player(object):
    def __init__(self, steamid):
        self.steamid = steamid
        # self.rankid = rankid
        self.get_game_info()
        self.get_player_info()

    def get_game_info(self):
        api1_info = {"appid": 730, "key": rand, "steamid": self.steamid}
        api1_object = requests.get("https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/",
                                   params=api1_info)
        data1 = json.loads(api1_object.content)
        alist = data1['playerstats']['stats']
        self.total_kills = deepTraverse(alist, 'total_kills')
        self.total_head_kills = deepTraverse(alist, 'total_kills_headshot')
        self.total_deaths = deepTraverse(alist, 'total_deaths')
        self.total_wins_round = deepTraverse(alist, 'total_wins')
        self.total_round = deepTraverse(alist, 'total_rounds_played')
        self.hits = deepTraverse(alist, 'last_match_favweapon_hits')
        self.fired = deepTraverse(alist, 'last_match_favweapon_shots')
        self.last_kill = deepTraverse(alist, 'last_match_kills')
        self.last_death = deepTraverse(alist, 'last_match_deaths')
        self.last_mvp = deepTraverse(alist, 'last_match_mvps')
        self.last_ct = deepTraverse(alist, 'last_match_ct_wins')
        self.last_t = deepTraverse(alist, 'last_match_t_wins')
        last_win = deepTraverse(alist, 'last_match_wins')
        if last_win == 15:
            self.win_status = '平'
            self.last_t = 15
            self.last_ct = 15
        else:
            if (self.last_ct > self.last_t):
                self.win_status = 'ct'
            elif (self.last_ct < self.last_t):
                self.win_status = 't'
            if (last_win == self.last_ct):
                player_role = 'ct'
            else:
                player_role = 't'
            if (self.win_status == player_role):
                self.win_status = '胜'
            else:
                self.win_status = '负'
        self.last_favweapon_id = deepTraverse(alist, 'last_match_favweapon_id')
        self.last_favweapon_shots = deepTraverse(alist, 'last_match_favweapon_shots')
        self.last_favweapon_hits = deepTraverse(alist, 'last_match_favweapon_hits')

        # num = 0
        # for one in data1['playerstats']['stats']:
        #    print(str(num)+" "+one['name']+" "+str(one['value']))
        #    num += 1

    def get_player_info(self):
        api2_info = {"key": rand, "steamids": self.steamid}
        api2_object = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/",
                                   params=api2_info)
        data2 = json.loads(api2_object.content)
        ## print(data2)
        self.player_name = data2['response']['players'][0]['personaname']
        self.avatar_url = data2['response']['players'][0]['avatarfull']
        # self.logoff_time = data2['response']['players'][0]['lastlogoff']


def deepTraverse(alist, key):
    for one in alist:
        if one['name'] == key:
            return one['value']
    raise Exception("Not Found")


app = FastAPI()


@app.get("/api")
async def entry(steamid: str, rankid: int, svg: bool = False):
    a = Player(steamid)
    if not svg:
        output = render(player=a, rankid=rankid)
        return Response(content=output, media_type='text/html')
    else:
        rep = render(player=a, rankid=rankid, svg=True)
        return Response(content=rep, media_type='image/svg+xml')
