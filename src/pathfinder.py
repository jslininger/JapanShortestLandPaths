import math

def shortestPath(start, end, roads):
    if start not in roads or end not in roads:
        raise IndexError("cities not in this time period")
    times = {}
    for town in roads:
        if town == start:
            times[town] = 0
        else:
            times[town] = math.inf
    parents, time = _search(start, end, roads, times)
    path = _backpedal(start, end, parents)
    return path, time

def _search (start, end, roads, time):
    parents = {}
    nextTown = start
    while nextTown != end:
        for neighbor in roads[nextTown]:
            if roads[nextTown][neighbor] + time[nextTown] < time[neighbor]:
                time[neighbor] = roads[nextTown][neighbor] + time[nextTown]
                parents[neighbor] = nextTown
            del roads[neighbor][nextTown]
        del time[nextTown]
        nextTown = min(time, key=time.get)
    return (parents, time[end])

def _backpedal(source, target, searchResult):
    node = target
    backpath = [target]
    path = []
    while node != source:
        backpath.append(searchResult[node])
        node = searchResult[node]
    for i in range(len(backpath)):
        path.append(backpath[-i - 1])
    return path

# basic algorithm from https://likegeeks.com/python-dijkstras-algorithm/