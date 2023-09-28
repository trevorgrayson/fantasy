# encapsulate all these things in models

# bullshit file
with open("data/myteam") as fp:
    for line in fp:
        player, team, pos = line.split("\t")
        # print(player, team)

        with open(f"data/depth/{team.lower()}") as teamp:
            for line in teamp:
                line = line.strip()
                if player in line:
                    pos, *lineup = line.split("\t")
                    try:
                        print(pos, player, lineup.index(player), line)
                    except ValueError:
                        print(pos, player, "No")