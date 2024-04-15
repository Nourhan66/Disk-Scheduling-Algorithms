def FCFS(head,requests_str):
    requests = [int(x) for x in requests_str.split()]

    requests.insert(0,head)
    seek_sequence =[head]

    Total_Seek_Time = 0
    for i in range(1,len(requests)):
        seek_sequence.append(requests[i])
        Total_Seek_Time+=(abs(requests[i]-requests[i-1]))

    return  seek_sequence , Total_Seek_Time