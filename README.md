## Getting Credentials

1. Navigate to [your app's creds](https://developer.yahoo.com/apps/ulaYgd7a/)
2. Make a credentials.json file in the root of the project with those values.

```
{
    "consumer_key": "...",
    "consumer_secret": "...",
}
```

# depth_charts.py

fetches depth charts for every team, compares against the last result and sees if anything changed.
if the primary changes, it will print that between the colons.
will cache page results once a day.


# TODO

- newer data? 2018??

check wire for pick ups
- injuries imply new good candidates?
- who is better than i will be playing?


optimizing team
