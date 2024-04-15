def LOOK(head,requests_str,direction):

    requests = [int(x) for x in requests_str.split()]
    right = []
    left = []
    sequence = []
    Total_Seek_Time = 0
    curr_track= head

    if direction == "left":
        for elem in requests :
            if elem < head :
                left.append(elem)
            else :
                right.append(elem)

        left.sort(reverse=True)

        right.sort()


    elif direction == "right":
        for elem in requests:
            if elem > head:
                right.append(elem)
            else:
                left.append(elem)

        right.sort()

        left.sort(reverse=True)

    sequence.append(head)
    if direction == "left":
        for i in left:
            sequence.append(i)
            Total_Seek_Time+=(curr_track-i)
            curr_track=i
        for j in right:
            sequence.append(j)
            Total_Seek_Time+=(j-curr_track)
            curr_track=j

    elif direction == "right":
        for j in right:
            sequence.append(j)
            Total_Seek_Time+=(j-curr_track)
            curr_track=j
        for i in left:
            sequence.append(i)
            Total_Seek_Time+=(curr_track-i)
            curr_track=i
    return sequence,Total_Seek_Time