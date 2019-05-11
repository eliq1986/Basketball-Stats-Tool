import constants

def prints_intro_message():
    """Prints intro message"""
    basketball_emoji = "\U0001F3C0"
    print("""
    {basketball} BASKETBALL TEAM STATS TOOL {basketball}
             --- Menu ---
    Here are your choices:
     1) Display Team Stats
     2) Quit
    """.format(basketball = basketball_emoji))

def print_teams():
    """Prints out team names"""
    print("\n")
    for index, team in enumerate(constants.TEAMS):
        print(f"{index + 1}) {team}")
