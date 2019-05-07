def return_bool(experience):
    """Returns a bool depending experience arg passed in"""
    if experience.upper() == "YES":
        return True
    return False

def return_integer(value):
    """Converts key value to int"""
    return int(value.split()[0:1][0])
