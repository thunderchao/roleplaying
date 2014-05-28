#by @ghostlenin
import random

era = ['mythic ', 'ancient ', 'modern ', 'futuristic ']
nation = ['japanese ', 'chinese ', 'indian ', 'persian ', 'egyptian ',
          'russian ', 'scandanavian ', 'german ', 'latinate ', 'ethiopian ',
          'bantu ', 'anglo ', 'american ', 'mexican ', 'carribean ', 'pacific ']
style = ['utopia', 'dystopia', 'cyberpunk', 'steampunk', 'western', 'noir',
         'megacities', 'farmland', 'desert', 'tundra', 'rainforest',
         'mountains', 'underground', 'islands', 'underwater', 'wasteland',
         'industrial', 'resort', 'transport', 'slums', 'temple', 'clouds',
         'ruins', 'prison', 'beach']

print('5 randomly generated settings: ')
for x in range(0,5):
    e = random.choice(era)
    n = random.choice(nation)
    s = random.choice(style)
    if n in nation: nation.remove(n)
    if s in style: style.remove(s)
    print('\t' + e + n + s)
