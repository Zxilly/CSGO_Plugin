from cla import *
from pri import *
from function import *
from PIL import Image,ImageDraw,ImageFont
import sys

#a = Player(user_code)
#render(player=a,rankid=6)

#with open('a','r+') as f:
#    print(f.read())
def getfont(fontsize:int):
    font = ImageFont.truetype(r'assets/fonts/NotoSansCJKsc-hinted/NotoSansCJKsc-Regular.otf',size=fontsize)
    return font

def pic_render(rankid):
    """
    kd = format(player.total_kills / player.total_deaths, '.2f')
    win_rate = format(player.total_wins_round / player.total_round * 100, '.2f')
    # print(player.total_wins_round,player.total_round)
    hit_rate = format(player.hits / player.fired * 100, '.2f')
    headshot_rate = format(player.total_head_kills / player.total_kills * 100, '.2f')
    last_kd = format(player.last_kill / player.last_death, '.1f')
    fav_hit_rate = format(player.last_favweapon_hits / player.last_favweapon_shots * 100, '.2f')
    """


    base_pic = Image.new('RGB',(500,220),'#2F3545')
    draw_object = ImageDraw.Draw(base_pic)
    draw_object.rectangle([(0,57),(500,123)],fill='#111',width=0)
    #57 123
    draw_object.text((15,96),'杀敌数',fill='#8A9EA7',font=getfont(12))
    # draw_object.line((0, 0) + base_pic.size, fill=128)
    # draw_object.line((0, base_pic.size[1], base_pic.size[0], 0), fill=128)
    base_pic.show()


if __name__ == '__main__':
    pic_render(6)

