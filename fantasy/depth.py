DEPTH_URL = 'http://in.sports.yahoo.com/nfl/teams/{team}/depthchart'

import urllib2
from pyquery import PyQuery as pq
from lxml import etree

def team_depth_chart(team):
    depth_chart = {}

    resp = urllib2.urlopen( DEPTH_URL.format(team=team) ).read()
    d = pq(resp)

    positions = d('.chart li dl')

    for node in positions:
        node = pq(node)

        position = node('dt')[0].text

        player_rows = node('dd')

        depth_chart[position] = map(lambda n: 
            pq(n)('a em').text() or pq(n)('a').text()
        , player_rows)

    return depth_chart
