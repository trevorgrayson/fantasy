# https://yahoo-fantasy-api.readthedocs.io/en/latest/yahoo_fantasy_api.html?highlight=player_info#yahoo_fantasy_api.league.League.player_stats
from glob import glob
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa


sc = OAuth2(None, None, from_file='credentials.json')
gm = yfa.Game(sc, 'nfl')

last_league_id = gm.league_ids()[-1]
league = gm.to_league(last_league_id)

YAHOO_POSITIONS = ['QB', 'WR', 'RB', 'TE', 'K','DEF', 'BN'] # 'w/r' 'W/R/T',
# standings
# team_key()  is me.

def positions():
    # read all free-agent files 
    for filename in glob('data/free-agents/*'):
        print(filename)
        pos = filename.split("/")[-1]
        pids = []
        with open(filename, 'r') as fp:
            for line in fp:
                pids.append(
                    line.split('\t')[-1].strip()
                )

        yield (pos, pids)


def fetch_stats(pids):
    return league.player_stats(pids, 'season', season=2019)

keys = []
for (pos, pids) in positions():
    stats_list = fetch_stats(pids)
    with open(f"data/player_stats/{pos}.tsv", 'w') as fp:
        if len(stats_list) < 1:
            print(f"No {pos} found")
            continue
        headers = stats_list[0].keys()
        fp.write("\t".join(headers))
        fp.write("\n")

        for stats in stats_list:
            row = []
            for key in headers:
                row.append(str(stats.get(key, '')))
                
            fp.write("\t".join(row))
            fp.write("\n")
