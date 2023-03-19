# python3

def parallel_processing(n, m, data):
    output = []
    # list to store the finishing times of each thread
    finish_time = [0] * n
    # iterate through each job
    for i in range(m):
        # find the earliest finishing time among the threads
        min_finish_time = min(finish_time)
        # find the thread with the earliest finishing time
        thread_index = finish_time.index(min_finish_time)
        # calculate the starting time for the job
        start_time = finish_time[thread_index]
        # calculate the finishing time for the job
        end_time = start_time + data[i]
        # update the finishing time for the thread
        finish_time[thread_index] = end_time
        # append the output pair
        output.append((thread_index, start_time))
    return output

def main():
    # read input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # calculate the output pairs
    result = parallel_processing(n, m, data)
    
    # print out the results, each pair in its own line
    for pair in result:
        print(pair[0], pair[1])
        
if __name__ == "__main__":
    main()