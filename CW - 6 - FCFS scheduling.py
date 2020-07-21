def fcfs(processes): # [arrival time, burst time, time remaining]
    for process in processes:
        process.append(process[1])
        process.append(None)
        process.append(None)
    #print(processes)
    done = []
    currentTime = 0
    while len(processes) > 0:
        if currentTime >= processes[0][0]:
            if processes[0][3] is None:
                processes[0][3] = currentTime

            if processes[0][2] > 1:
                processes[0][2] -= 1
            else:
                processes[0][4] = currentTime + 1
                done.append(processes[0])
                processes.pop(0)
        
        currentTime += 1
    print(currentTime, processes, done)

    output = [0,0,0,0]
    for complete in done:
        output[0] += complete[4]
        output[1] += complete[4] - complete[0]
        output[2] += complete[4] - complete[0] - complete[1]
        output[3] += complete[1]

    for i in range(0, 4):
        output[i] = round(output[i] / len(done), 2)
    
    return tuple(output)
        

# [arrival time, burst time, remaining time, start time, end time]
# (Avg-CompletionTime, Avg-TurnAroundTime, Avg-WaitTime, Throughput)

print(fcfs([[0, 4], [2, 1], [3, 3], [7, 13]],)) # (9.5, 6.5, 1.25, 5.25)
print(fcfs([[0, 2], [1, 2], [5, 3], [6, 4], [7, 9]])) # (9.4, 5.6, 1.6, 4.0)
print(fcfs([[4, 4], [12, 1], [20, 3]])) # (14.67, 2.67, 0.0, 2.67)