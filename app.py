import constants


def prints_intro_message():
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


def format_players_dict():
    experienced_players = []
    inexperienced_players = []
    for player_index in constants.PLAYERS:
        player_dict = {}
        for key,value in player_index.items():
            if key == "height":
                height_int = int(value.split()[0:1][0])
                player_dict[key] = height_int
            elif key == "experience":
                player_dict[key] = return_bool(value)
            elif key == "guardians":
                 player_dict[key] = value.split("and")
            else:
                player_dict[key] = value
        if player_dict["experience"] == False:
            inexperienced_players.append(player_dict)
        else:
            experienced_players.append(player_dict)
    return experienced_players + inexperienced_players


def print_teams():
    print("\n")
    for index, team in enumerate(constants.TEAMS):
        print(f"{index + 1}) {team}")


def format_teams():
    panthers = []
    bandits = []
    warriors = []
    player_list = format_players_dict()
    experienced_players = player_list[:9]
    inexperienced_players = player_list[9:]
    return [experienced_players[:3] + inexperienced_players[:3], experienced_players[3:6] + inexperienced_players[3:6], experienced_players[6:] + inexperienced_players[6:]]


def get_player_names(team):
    player_names = []
    for index in team:
        for key,value in index.items():
            if key == "name":
                player_names.append(value)
    return player_names


def print_team_stats(index,team):
    player_names_list = get_player_names(team[index - 1])
    team_name = constants.TEAMS[index - 1]
    print("""
Team: {} Stats
--------------------
Total Players: {}

Players on Team:
  {}
    """.format(team_name, len(player_names_list), ', '.join(player_names_list)))


def get_team_stats():
    while True:
        try:
            print("\n")
            select_team_index = int(input("Please enter a number 1-3 > "))
            if select_team_index in range(1,4):
                team_list = format_teams()
                print_team_stats(select_team_index, team_list)
                run_app()
            else:
                print("Sorry but needs to be either 1,2 or 3")
        except:
            print("Sorry but it must be a number...")


def quit_or_continue():
    response = int(input("Enter an option > "))
    if response == 1:
        print_teams()
        get_team_stats()
    else:
        print("Thanks for checking out the teams.")


def run_app():
    prints_intro_message()
    while True:
        try:
            quit_or_continue()
            break
        except ValueError:
            print("Letters are invalid. Please enter a number.")


if __name__ == "__main__":
    run_app()
