# Complete the function below.

import time as tt

def howManyAgentsToAdd(noOfCurrentAgents, callsTimes):
    """
    From start time of first call, to end time of last call,
    check how many overlaps happen. Take max overlaps as 
    total no of agents needed in total.
    """
    start_time = tt.time()
    start = min(call[0] for call in callsTimes)
    end = max(call[1] for call in callsTimes)

    def overlap(time, callTimes):
        n = 0
        for t in callTimes:
            if time in range(t[0], t[1]+1):
                n += 1
        return n

    max_agents = noOfCurrentAgents
    time = start
    while (time <= end):
        max_n = overlap(time, callsTimes)
        if max_n > max_agents:
            max_agents = max_n
        time += 1
    
    //print('Runtime:', (tt.time() - start_time)*1000)

    return max_agents - noOfCurrentAgents

def main(noOfCurrentAgents, callsTimes):
    """More efficient method, checking only start time of each call against the rest"""
    start_time = tt.time()
    max_agents = 1 # Assume at least one agent
    for n, (t1, t2) in enumerate(callsTimes):
        overlaps = 1 # Every call needs one agent
        for m, (x1, x2) in enumerate(callsTimes):
            if m != n: # Don't check it's own call
                if t1 in range(x1, x2+1): # Check this call's start time for overlap with other call times
                    overlaps += 1
        max_agents = max(max_agents, overlaps)
    
    //print('Runtime:', (tt.time() - start_time)*1000)

    return max_agents - noOfCurrentAgents


if __name__ == "__main__":
    noOfCurrentAgents = 2
    callsTimes = [
        [1481122000, 1481122020],
        [1481122000, 1481122040],
        [1481122030, 1481122035],
        [1481122030, 1481122050],
        [1481122000, 1481122020],
        [1481122000, 1481122040],
        [1481122030, 1481122035],
        [1481122030, 1481122050],
    ]
    res = howManyAgentsToAdd(noOfCurrentAgents, callsTimes)
    print('first', res)
    res = main(noOfCurrentAgents, callsTimes)
    print('second', res)



