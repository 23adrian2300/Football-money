from fastapi import HTTPException


def verify_api_key(api_key: str):
    file = open('api_keys.txt', 'r')
    for line in file:
        if api_key in line:
            return True
    return False


def string_to_int(string):
    return int(string.replace('€', '').replace('m', '0000').replace('k', '0').replace('.', '').replace(' ', ''))


def get_most_valuable_player_by_club_id(parsed):
    try:
        players = parsed['players']
        players_with_market_value = [player for player in players if player.get('marketValue')]
        players_with_market_value = sorted(players_with_market_value,
                                           key=lambda x: string_to_int(x.get('marketValue', '0')), reverse=True)
        most_valuable_player = players_with_market_value[0]
        value = most_valuable_player.get('marketValue')

        return most_valuable_player, value
    except Exception as e:
        return e

def parse_info_about_player(parsed, value):
    try:
        name = parsed['name']
        age = parsed['age']
        position = parsed['position']
        dateofbirth = parsed['dateOfBirth']
        nationality = parsed["nationality"][0]
        height = parsed['height']
        foot = parsed['foot']
        valueofplayer = value

        return name, age, position, dateofbirth, nationality, height, foot, valueofplayer
    except Exception:
        raise HTTPException(status_code=404, detail="Failed to parse info about player")