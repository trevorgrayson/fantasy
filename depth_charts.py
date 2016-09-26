import json
from datetime import datetime

from fantasy import (
    depth, TEAMS,
    cache_file
)



for team in TEAMS:
    
    cache_f = cache_file('depth', team)
    
    try:
        fp = open(cache_f, 'r')
        last_line = fp.readlines()[-1]
        last_chart = json.loads(last_line)
        fp.close()
    except IOError:
        print "couldn't find %s" % cache_f
        

    fp = open(cache_f, 'a')

    chart = depth.team_depth_chart(team)
    chart['created'] = str(datetime.now())
    js = json.dumps(chart)
    fp.write(js)
    fp.write("\n")

    if last_chart is not None:
        for position, players in chart.iteritems():
            players2 = last_chart[position]

            if position != 'created' and players != players2:
                print '%s: %s - %s' % (
                    team, str(players), str(players2)
                )

    fp.close()
