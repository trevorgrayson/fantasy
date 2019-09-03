from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa


sc = OAuth2(None, None, from_file='credentials.json')
gm = yfa.Game(sc, 'nfl')

last_league_id = gm.league_ids()[-1]
league = gm.to_league(last_league_id)

YAHOO_POSITIONS = ['QB', 'WR', 'RB', 'TE','W/R/T','K','DEF', 'BN'] # 'w/r'
# standings
# team_key()  is me.


print('get team rosters')
for team in league.teams():
    team_name = team['name']
    print('#' + team_name)
    with open(f"data/rosters/{team_name}", "w") as fp:
        team = league.to_team(team['team_key'])
        roster = team.roster(league.current_week())

        try:
            for player in roster:
                fp.write(player['name'] + "\n")
        except StopIteration as err:
            pass


print('get free-agents list')
for pos in YAHOO_POSITIONS:

    pos_filename = pos.replace('/', '_')
    with open(f"data/free-agents/{pos_filename}", "w") as fp:
        try:
            for agent in league.free_agents(pos):
                name = agent['name']
                positions = ",".join(agent['eligible_positions'])
                print(f">>{name}	{positions}")
                fp.write(f"{name}	{positions}\n")
        except StopIteration as err:
            pass
