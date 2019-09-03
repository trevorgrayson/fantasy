import sys
from fantasy import depth


def print_chart(chart):
    for position, players in chart.items():
        print("{position}: {players}".format(
            position=position,
            players=", ".join(players)
        ))


if __name__ == '__main__':

    team = sys.argv[1]
    print('looking up %s' % team)
        
    chart = depth.team_depth_chart(team)
    print_chart(chart)
