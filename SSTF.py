def SSTF(head, requests_str):

    requests = [int(x) for x in requests_str.split()]
    requests.insert(0, head)
    sequence = []
    temp = requests
    Total_Seek_Time = 0
    curr_track = head
    size = len(requests)
    i = 0
    while i < size:
        next_track = find_next_track(temp, curr_track)
        Total_Seek_Time += abs(curr_track - next_track)
        sequence.append(curr_track)
        temp.remove(curr_track)
        curr_track = next_track
        i += 1

    return sequence , Total_Seek_Time

def find_next_track(requests, curr_track):
    min_diff = float('inf')
    diff = 0
    next_track = -1
    for i in range(0, len(requests)):
        if requests[i] != curr_track:
            diff = abs(curr_track - requests[i])
            if diff < min_diff:
                min_diff = diff
                next_track = requests[i]
    if next_track == -1:
        return curr_track
    else:
        return next_track




