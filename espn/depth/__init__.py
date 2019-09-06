DEPTH_URL = 'https://www.espn.com/nfl/team/depth/_/name/{team}'

from urllib.request import urlopen
from pyquery import PyQuery as pq
import fantasy
from fantasy import (
    cache_file
)

TEAMS = [
# AFC East
'buf', # Buffalo Bills
'mia', # Miami Dolphins
'ne', # New England Patriots
'ne', # New York Jets
# AFC North
'bal', # Baltimore Ravens
'cin', # Cincinnati Bengals
'cle', # Cleveland Browns
'pit', # Pittsburgh Steelers
# AFC South
'hou', # Houston Texans
'ind', # Indianapolis Colts
'jax', # Jacksonville Jaguars
'ten', # Tennessee Titans
# AFC West
'den', # Denver Broncos
'kc', # Kansas City Chiefs
'lac', # Los Angeles Chargers
'oak', # Oakland Raiders
# NFC East
'dal', # Dallas Cowboys
'nyg', # New York Giants
'phi', # Philadelphia Eagles
'wsh', # Washington Redskins
# NFC North
'chi', # Chicago Bears
'det', # Detroit Lions
'gb', # Green Bay Packers
'min', # Minnesota Vikings
# NFC South
'atl', # Atlanta Falcons
'car', # Carolina Panthers
'no', # New Orleans Saints
'tb', # Tampa Bay Buccaneers
# NFC West
'ari', # Arizona Cardinals
'lar', # Los Angeles Rams
'sf', # San Francisco 49ers
'sea' # Seattle Seahawks
]

POSITIONS = ['QB', 'RB', 'WR', 'WR', 'TE', 'FB', 'LT', 'LG', 'C', 'RG', 'RT' ,
    'LDE', 'LDT', 'RDT', 'RDE', 'WLB', 'MLB', 'SLB', 'SS', 'FS', 'RCB', 'LCB',
    'PK', 'P', 'H', 'PR', 'KR', 'LS'
]


def team_depth_chart(team):
    depth_chart = []

    resp = fantasy.fetch( DEPTH_URL.format(team=team) )
    d = pq(resp)

    positions = d('.nfl-depth-table .Table2__tr.Table2__tr--sm.Table2__even')

    rows = []
    for node in positions:
        node = pq(node)
        rows.append(node.find('a'))

    rows = filter(lambda x: len(x) > 0, rows)
    depth_chart = zip(POSITIONS, map(lambda row: [col.text for col in row], rows))
    
    return depth_chart

