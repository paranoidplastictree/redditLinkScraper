import re

def findall(pattern, text):
    matches = re.findall(pattern, text)
    print(len(matches))
    print(matches[0])
    print(".............")
    print(matches[1])

def parseAll(pattern, text):
    matches = re.findall(pattern, text)
    for found in matches:
        print(found)
    
    
text = "Walk through a medieval village.  The market's busy with the day's sales, and occasionally you'll have to dodge a horse along the road.  Be sure to step to the side when a troop of soldiers comes by, and keep an eye open if a duel breaks out.\n\n[Medieval Village](htTp://mynoiSe.net/superGenerator.PHp?g1=grasslandSoundscapeGenerator.php%3Fc%3D3%26l%3D14000000000300220001%26a%3D1&amp;g2=cafeRestaurantNoiseGenerator.php%3Fc%3D3%26l%3D00080212040600000019%26a%3D1&amp;g3=battlefieldRPGSoundscapeGenerator.php%3Fc%3D3%26l%3D00002341401712151021%26a%3D1&amp;g4=springWalkSoundscapeGenerator.php%3Fc%3D3%26l%3D42370401082603230000%26a%3D1&amp;g5=&amp;yt=) A summer evening on a prairie, with a thunderstorm on the horizon. [Distant Prairie Storm](http://mynoise.net/superGenerator.php?g1=grasslandSoundscapeGenerator.php%3Fc%3D3%26l%3D11000000000000251105%26a%3D1&amp;g2=windNoiseGenerator.php%3Fc%3D3%26l%3D00000000010009020653%26a%3D1&amp;g3=thunderNoiseGenerator.php%3Fc%3D3%26l%3D43474841220000000000%26a%3D1&amp;g4=&amp;g5=&amp;yt=) xxx"
text2 = "aaaaaa 5bbbbb6 ccccc 5ddddd6 eeeee"
text2 = "aaaaaa [bbbbb] ccccc [ddddd] eeeee"

link_text_url_pattern = r"\[([^\[])+\]\(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=;]*)"
# p2 = r"\[[^\]]+\]\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\)"
p2 = r"(?i)\[[^\]]+\]\(http[s]?://mynoise.net/supergenerator\.php[^\)]+\)"
p2 = r"(?i)(?<=\[)[^\]]+\]\(http[s]?://mynoise.net/supergenerator\.php[^\)]+(?=\))"

findall(p2, text)
