import requests
import json
from datetime import datetime

def all_guild_players(guild):
    r = requests.get('https://api.wynncraft.com/v3/guild/prefix/' + guild)
    print(r.status_code)
    t = r.json()
    t = t['members']
    return t['chief'], t['strategist'], t['captain'], t['recruiter'], t['recruit']
def last_time_online(username):
    try: 
        r = requests.get('https://api.wynncraft.com/v3/player/' + username)
    except:
        print(r.status_code)
    
    t = r.json()
       
    return t['username'], t['lastJoin']

a, b, c, d, e = all_guild_players(input('guild prefix: '))
 
print('--------chiefs--------')
for f in a.keys():
    try: 
        t, y = last_time_online(f)
        print(t)
        print(y[:10])
    except:
        print('something went wrong for: ' + f)

print('--------strategist--------')
for f in b.keys():
    try: 
        t, y = last_time_online(f)
        print(t)
        print(y[:10])
    except:
        print('something went wrong for: ' + f)
        
print('--------captain--------')
for f in c.keys():
    try:
        t, y = last_time_online(f)
        print(t)
        print(y[:10])
    except:
        print('something went wrong for: ' + f)

print('--------recruiters--------')
for f in d.keys():
    try:
        t, y = last_time_online(f)
        print(t)
        print(y[:10])
    except:
        print('something went wrong for: ' + f)

print('--------recruits--------')
for f in e.keys():
    try:
        t, y = last_time_online(f)
        print(t)
        print(y[:10])
    except:
        print('something went wrong for: ' + f)
