# https://www.fantasyfootballdatapros.com/blog/ml/1

RUSH_COLS = ['Cmp']
RECEIV_COLS = ['Yds']
PASS_COLS = []

def features(data):
    data.rename({
        'Player': 'name',
        'Pts*': 'points',
        'Att': 'Attempts', 
        # Cmp = Completions, 
        # Yds = Yards Gained, 
        # TD = Touchdowns, 
        # Int = Interceptions, 
        # 2Pt = 2-Point Conversions, 
        # Rec = Receptions, 
        # FL = Fumbles Lost, 
        # Pts = Fantasy Football Points
    }, axis=1, inplace=True)
    # drop unused

    # filter position
    # df[df['FantPos'] == 'RB']
    return data

def train(rows, target):
    pass


def predict(features):
    pass


