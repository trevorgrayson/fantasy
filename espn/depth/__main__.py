import datetime
from . import TEAMS, team_depth_chart


if __name__ == '__main__':
    for team in TEAMS:
        depth = team_depth_chart(team)
        print(team)
        now = datetime.datetime.now().isoformat()

        with open(f"data/depth/{team}", 'w') as fp:
            for pos, vals in depth:

                players = "	".join(vals)
                fp.write(f"{pos}	{players}\n")
