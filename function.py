from data import *


def render(player, rankid):
    kd = format(player.total_kills / player.total_deaths, '.2f')
    win_rate = format(player.total_wins_round / player.total_round, '.2f')
    hit_rate = format(player.hits / player.fired, '.2f')
    headshot_rate = format(player.total_head_kills / player.total_kills, '.2f')
    last_kd = format(player.last_kill / player.last_death, '.1f')
    fav_hit_rate = format(player.last_favweapon_hits / player.last_favweapon_shots, '.2f')

    # print(player.last_favweapon_id)
    # print(player.last_favweapon_hits)

    output = template_html.format(player.avatar_url, player.player_name, rankid, player.total_kills, kd, win_rate,
                                  hit_rate, headshot_rate, last_kd, player.win_status, player.last_t, player.last_ct,
                                  fav_hit_rate, player.last_mvp, player.last_kill, player.last_death,
                                  weapon_url_dict[player.last_favweapon_id])

    # print(output)
    return output
