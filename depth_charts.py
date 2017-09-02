#!/usr/bin/env python

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
        last_chart = None
        

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
                new_lead = ""

                if players[0] != players2[0]:
                    new_lead = players[0]

                print '%s:%s: %s <= %s' % (
                    team, new_lead, ", ".join(players), ", ".join(players2)
                )

    fp.close()
