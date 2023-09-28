DEPTH_URL = 'http://in.sports.yahoo.com/nfl/teams/{team}/depthchart'

from urllib.request import urlopen
import fantasy
from pyquery import PyQuery as pq

# ESPN Depth 
# https://www.espn.com/nfl/team/depth/_/name/buf
# .nfl-depth-table .Table2__table__wrapper td .Table2__table-scroller td

def team_depth_chart(team):
    depth_chart = {}

    resp = fantasy.fetch( DEPTH_URL.format(team=team) )
    d = pq(resp)

    positions = d('.bd table tr')

    for node in positions:
        node = pq(node)

        position = node('th')[0].text

        player_rows = node('td')

        depth_chart[position] = map(lambda n: 
            pq(n)('a').text()
        , player_rows)

    return depth_chart


FANTASY_PROS = 'https://www.fantasypros.com/nfl/start/{names}.php'

def fantasy_pros_who_starts(a, b=None):
    names = a.split(' ')

    if b is not None:
        names += b.split(' ')

    url = FANTASY_PROS.format(names="-".join(names))
    resp = fantasy.fetch( url )
    d = pq(resp)

    left  = d('.wsis-summary .player-left span')[0].text
    right = d('.wsis-summary .player-right span')[0].text

    return (left, right)
