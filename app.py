import constants
from utilities import return_bool, return_integer
from print_functions import prints_intro_message, print_teams


def print_team_stats(index,team):
    """Takes two arguments and prints team stats"""

    player_names_dict = get_player_info(team[index - 1])
    team_name = constants.TEAMS[index - 1]
    print("""
Team: {} Stats
--------------------
Total Players: {}
Players on Team:
  {}

 Player Guardians:
  {}

 Experienced Players: {}

 Inexperienced Players: {}

 Average Height: {}
    """.format(
    team_name, len(player_names_dict["names"]),
    ' , '.join(player_names_dict["names"]),
    ' , '.join(player_names_dict["guardians"]),
    len(player_names_dict["experienced_players"]),
    len(player_names_dict["inexperienced_players"]),
    player_names_dict["heights"]))


def format_players_dict():
    """Creates new dictionary with imported constant.PLAYERS file"""

    inexperienced_players = []
    experienced_players = []
    for player_index in constants.PLAYERS:
        player_dict = {}
        for key,value in player_index.items():
            if key == "height":
                player_dict[key] = return_integer(value)
            elif key == "experience":
                player_dict[key] = return_bool(value)
            elif key == "guardians":
                 splitted_guardians = ','.join(value.split("and"))
                 player_dict[key] = splitted_guardians.rstrip()
            else:
                player_dict[key] = value
        if player_dict["experience"] == False:
            inexperienced_players.append(player_dict)
        else:
            experienced_players.append(player_dict)
    return experienced_players + inexperienced_players


def format_teams():
    """Creates list of experienced and inexperienced players"""

    player_list = format_players_dict()
    experienced_players = player_list[:9]
    inexperienced_players = player_list[9:]
    return [experienced_players[:3] + inexperienced_players[:3], experienced_players[3:6] + inexperienced_players[3:6], experienced_players[6:] + inexperienced_players[6:]]


def get_player_info(team):
    """Returns player dictionary for print team stats"""

    player_dict = {
    "names":[],
    "inexperienced_players": [],
    "experienced_players":[],
    "heights": 0,
    "guardians":[]
    }
    for index in team:
        for key,value in index.items():
            if key == "name":
                player_dict["names"].append(value)
            if key == "experience" and value == True:
                player_dict["experienced_players"].append(index)
            elif key == "experience" and value == False:
                player_dict["inexperienced_players"].append(index)
            if key == "guardians":
                player_dict["guardians"].append(value)
            if key == "height":
                player_dict["heights"] += value
    player_dict["heights"] = get_average_height(player_dict, team)
    return player_dict


def get_average_height(player_dict, team):
    """takes two args and returns int"""

    return player_dict["heights"] // len(team)


def get_team_stats():
    """Prompts user for team selection"""

    while True:
        try:
            print("\n")
            select_team_index = int(input("Please enter a number 1-3 > "))
            if select_team_index in range(1,4):
                team_list = format_teams()
                print_team_stats(select_team_index, team_list)
                break
            else:
                print("Sorry but needs to be either 1,2 or 3")
        except:
            print("Sorry but it must be a number...")


def quit_or_continue():
    """Continously runs until user selects option"""

    while True:
        prints_intro_message()
        response = int(input("Enter an option > "))
        if response == 1:
            print_teams()
            get_team_stats()
        elif response == 2:
            print("Thanks for checking out the teams.")
            break
        else:
            print("\n **** Please select 1 or 2 ****")


def run_app():
    """Contains all functionality"""

    while True:
        try:
            quit_or_continue()
            break
        except ValueError:
            print("Letters are invalid. Please enter a number.")


if __name__ == "__main__":
    run_app()
