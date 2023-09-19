import data


def find_word(phrase, mot):
    if mot in phrase:
        return True
    else:
        mots_in_phrase = phrase.split()
        if mot in mots_in_phrase:
            return True
        else:
            return False


def get_response(message: str) -> str:
    p_message = message.lower()
    for i in data.hailey_quinn_dict:
        h = find_word(i.lower(), p_message)
        if h is True:
            return data.hailey_quinn_dict[i]

    return '`omg try again`'


