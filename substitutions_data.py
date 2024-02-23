basic_substitutions = {
    'a': ['a', 'A', '@'],
    'b': ['b', 'B', '8'],
    'c': ['c', 'C', '('],
    'e': ['e', 'E', '3'],
    'g': ['g', 'G', '9', '6'],
    'i': ['i', 'I', '1', '!'],
    'l': ['l', 'L', '1', '|'],
    'o': ['o', 'O', '0'],
    's': ['s', 'S', '$', '5'],
    't': ['t', 'T', '7'],
    'z': ['z', 'Z', '2'],
    'd': ['d', 'D'],
    'f': ['f', 'F'],
    'h': ['h', 'H'],
    'j': ['j', 'J'],
    'k': ['k', 'K'],
    'm': ['m', 'M'],
    'n': ['n', 'N'],
    'p': ['p', 'P'],
    'q': ['q', 'Q'],
    'r': ['r', 'R'],
    'u': ['u', 'U'],
    'v': ['v', 'V'],
    'w': ['w', 'W'],
    'x': ['x', 'X'],
    'y': ['y', 'Y'],
    'ü': ["Ü", "ü"],
    "ä": ["ä", "Ä"],
    "ö": ["ö", "Ö"]
}

moderate_substitutions = {
    'a': ['a', 'A', '@', '4'],
    'b': ['b', 'B', '8'],
    'c': ['c', 'C', '('],
    'e': ['e', 'E', '3'],
    'g': ['g', 'G', '9', '6'],
    'i': ['i', 'I', '1', '!'],
    'l': ['l', 'L', '1', '|'],
    'o': ['o', 'O', '0'],
    's': ['s', 'S', '$', '5'],
    't': ['t', 'T', '7'],
    'z': ['z', 'Z', '2'],
    'd': ['d', 'D', 'o'],
    'f': ['f', 'F', 'o'],
    'h': ['h', 'H', '#'],
    'j': ['j', 'J', 'i'],
    'k': ['k', 'K', 'i'],
    'm': ['m', 'M', 'n'],
    'n': ['n', 'N', 'm'],
    'p': ['p', 'P', 'q'],
    'q': ['q', 'Q', 'p'],
    'r': ['r', 'R', 't'],
    'u': ['u', 'U', 'v'],
    'v': ['v', 'V', 'u'],
    'w': ['w', 'W', 'v'],
    'x': ['x', 'X', '+'],
    'y': ['y', 'Y', 'i'],
    'ü': ["Ü", "ü"],
    "ä": ["ä", "Ä"],
    "ö": ["ö", "Ö"]
}


comprehensive_substitutions = {
    'a': ['a', 'A', '@', '4', '/\\'],
    'b': ['b', 'B', '8', '|3', '13'],
    'c': ['c', 'C', '(', '<', '{', '['],
    'e': ['e', 'E', '3', '€', '£'],
    'g': ['g', 'G', '9', '6'],
    'i': ['i', 'I', '1', '!', '|', ']['],
    'l': ['l', 'L', '1', '|', '/\\'],
    'o': ['o', 'O', '0'],
    's': ['s', 'S', '$', '5', 'z'],
    't': ['t', 'T', '7', '+'],
    'z': ['z', 'Z', '2', 's', '5'],
    'd': ['d', 'D', 'o'],
    'f': ['f', 'F', 'o'],
    'h': ['h', 'H', '#'],
    'j': ['j', 'J', 'i'],
    'k': ['k', 'K', 'i'],
    'm': ['m', 'M', 'n'],
    'n': ['n', 'N', 'm'],
    'p': ['p', 'P', 'q'],
    'q': ['q', 'Q', 'p'],
    'r': ['r', 'R', 't'],
    'u': ['u', 'U', 'v'],
    'v': ['v', 'V', 'u'],
    'w': ['w', 'W', 'v'],
    'x': ['x', 'X', '+'],
    'y': ['y', 'Y', 'i'],
    'ü': ["Ü", "ü"],
    "ä": ["ä", "Ä"],
    "ö": ["ö", "Ö"]
}

substitutions = [
    basic_substitutions,
    moderate_substitutions,
    comprehensive_substitutions
]

