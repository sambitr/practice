def find_runner_up(participants, result_array):
    if len(result_array) != participants:
        return "Number of participants and results do not match"
    else:
        get_unique = set(result_array)
        get_unique_array = list(get_unique)
        if len(get_unique_array) < 2:
            return None
        else:
            return sorted(get_unique_array)[-2]