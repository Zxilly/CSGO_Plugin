import json
from datetime import datetime

from data import *


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


# @player_info
#   generate_time
#   page_content

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
