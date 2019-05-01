import constants

basketball_emoji = "\U0001F3C0"


print("""
{basektball} BASKETBALL TEAM STATS TOOL {basektball}

          --- Menu ---

Here are your choices:
    1) Display TEAM
    2) Quit
    
""".format(basektball = basketball_emoji))


try:
    response = int(input("Enter an option > "))
except ValueError:
    print("Letters are invalid. Please enter 1 or 2")


player_list = []

def return_bool(experience):
    if experience.upper() == "YES":
        return True
    return False


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


if __name__ == "__main__":
    pass
