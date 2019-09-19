import os


class PlayerNews:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.summary = kwargs.get("summary")
        self.body = kwargs.get("body")

    def __str__(self):
        return f"{self.name}: {self.summary}\n{self.body}\n"


def news():
    """ summary of other event outlets """
    return []


def roster(team="Team Taco"):
    """what's going on with team"""
    roster = []
    text = os.popen("./bin/team_news").read().split("\n")

    players = []
    with open(f"data/rosters/{team}", "r") as team:
        for player in team:
            players.append( player.strip())

    for line in text:
        fields = line.split("</p>")
        summary = fields.pop(0)
        body = "".join(fields).replace("</p","") # hack

        roster.append(PlayerNews(
            name=players.pop(0),
            summary=summary,
            body=body
        ))


    return roster


def first_strings():
    """new first strings, by position"""
    pass


if __name__ == '__main__':
    # testing
    for news in roster():
        print(news)
