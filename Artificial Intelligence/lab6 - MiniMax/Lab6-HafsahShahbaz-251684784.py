# Hafsah Shahbaz - 251684784

terminal_states = {'211111': 0, '22111': 1, '2221': 0}

successors = {
    '7': ['61', '52', '43'],
    '61': ['511', '421'],
    '52': ['421', '322', '331'],
    '43': ['421', '331'],
    '511': ['4111', '3211'],
    '421': ['3211'],
    '322': ['2221'],
    '331': ['3211'],
    '4111': ['31111'],
    '31111': ['211111'],
    '3211': ['22111'],
}


def util_value(state, agent):
    if state in terminal_states:
        return terminal_states[state]
    if agent == 'MIN':
        return min_value(state)
    else:
        return max_value(state)


def min_value(state):
    if state in terminal_states:
        return terminal_states[state]
    v = 10000000
    if state in successors:
        neighbours = successors[state]
    for neighbour in neighbours:
        v = min(v, util_value(neighbour, 'MAX'))
    return v


def max_value(state):
    if state in terminal_states:
        return terminal_states[state]
    v = -10000000
    if state in successors:
        neighbours = successors[state]
    for neighbour in neighbours:
        v = max(v, util_value(neighbour, 'MIN'))
    return v


if __name__ == "__main__":
    print(util_value('7', 'MIN'))
    # OUTPUT: 1
