import constants

basketball_emoji = "\U0001F3C0"


print("""
{basketball} BASKETBALL TEAM STATS TOOL {basketball}

          --- Menu ---

Here are your choices:
1) Display Team Stats
2) Quit

""".format(basketball = basketball_emoji))

def return_bool(experience):
    """Returns a bool depending experience arg passed in"""
    if experience.upper() == "YES":
        return True
    return False


def format_players_list():
    player_list = []
    for player_index in constants.PLAYERS:
        player_dict = {}
        for key,value in player_index.items():
            if key == "height":
                height_int = int(value.split()[0:1][0])
                player_dict[key] = height_int
            elif key == "experience":
                player_dict[key] = return_bool(value)
            else:
                player_dict[key] = value
        player_list.append(player_dict)
    return player_list


def print_teams():
    for index, team in enumerate(constants.TEAMS):
        print(f"{index + 1}) {team}")


def format_teams():
    player_list = format_players_list()
    return [player_list[:6], player_list[6:12], player_list[12:]]

def print_team_stats(index,team):
    team_selected = team[index - 1]
    team_name = constants.TEAMS[index - 1]
    print("""
Team: {} Stats
--------------------
Total Players: {}

    """.format(team_name, len(team_selected)))


def get_team_stats():
    while True:
        try:
            select_team_index = int(input("Please enter a number 1-3 > "))
            if select_team_index in range(1,4):
                team_list = format_teams()
                print_team_stats(select_team_index, team_list)
            else:
                print("Sorry but needs to be either 1,2 or 3")
        except:
            print("Sorry but it must be a number...")


while True:
    try:
        response = int(input("Enter an option > "))
        if response == 1:
            print_teams()
            get_team_stats()
        else:
            print("Thanks for checking out the teams.")
            break
    except ValueError:
        print("Letters are invalid. Please enter a number.")


if __name__ == "__main__":
    pass
