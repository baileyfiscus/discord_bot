import os
import json

# TODO Fix this?
JSON_FILE = "games/games.json"

# Should be a file that looks like this:
#
# [
#   {"name": ""Game 1", "players": $PLAYER_SYNTAX_1, ...},
#   ...
# ]

def player_comparator(game_def, player_count):
    """Returns true if the player_count requested matches the defined range (e.g. we want
    a game that supports 1-3 people and the number of current players is 2.)

    All of these are valid syntaxes:

    1-3
    1,2,3
    1-5,10

    Good example of the last one is smite, CSGO, etc.

    """
    def expand_range_syntax(s):
        try:
            if "-" in s:
                return list(map(int, s.split("-")[:2]))

            return int(s)
        except ValueError:
            # TODO report parsing errors
            pass

    try:
        rng_syntax = game_def.get("players")
    except KeyError:
        # TODO report parsing error
        return False
    ranges = map(expand_range_syntax, rng_syntax.split(","))

    # Implements OR, basically.
    for rng in ranges:
        if rng is None:
            continue
        if type(rng) is list and rng[0] <= player_count <= rng[1]:
            return True
        if type(rng) is int and rng == player_count:
            return True

    return False

def get_list(player_count: int):
    jsn = None
    with open(JSON_FILE, 'r') as fobj:
        jsn = json.load(fobj)

    filteredList = filter(lambda x: player_comparator(x, player_count), jsn)
    return [x['name'] for x in filteredList]

def _old_getList(playerCount):
    #creates a list of games with the given player count
    gamesList = []
    gameDir = "/home/pi/discord_bot/games"

