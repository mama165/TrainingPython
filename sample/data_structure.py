import array


def iterateThroughList(list):
    dictionary = {}
    visited = []

    for n in range(len(list)):
        count = 1
        if not (list[n] in visited):
            visited.append(list[n])
            for m in range(n+1, len(list)):
                if list[m] == list[n]:
                    count = count + 1
            dictionary[list[n]] = count
    return dictionary
