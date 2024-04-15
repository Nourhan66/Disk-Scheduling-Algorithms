def CLOOK(requests_str,head,direction):

    requests = [int(x) for x in requests_str.split()]
    left = []
    right = []
    sequence = []
    Total_Seek_Time = 0
    curr_track = head

    if direction == "left":
        for elem in requests:
            if elem < head:
                left.append(elem)
            else:
                right.append(elem)

        left.sort(reverse=True)

        right.sort(reverse=True)

    elif direction == "right":
        for elem in requests:
            if elem > head:
                right.append(elem)
            else:
                left.append(elem)
        
        right.sort()

        left.sort()


    sequence.append(head)
    if direction == "left":
        for i in left:
            sequence.append(i)
            Total_Seek_Time+=abs(curr_track-i)
            curr_track = i
        for j in right:
            sequence.append(j)
            Total_Seek_Time+= abs(j-curr_track)
            curr_track = j
    elif direction == "right":
        for j in right:
            sequence.append(j)
            Total_Seek_Time+=abs(j-curr_track)
            curr_track = j
        for i in left:
            sequence.append(i)
            Total_Seek_Time+=abs(curr_track-i)
            curr_track = i
    
    return sequence,Total_Seek_Time
