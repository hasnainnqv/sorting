def sorting(lst):
    n=len(lst)
    # (lst.sort(reverse=True))
    print(lst)
    count=0
    for i in range(n-1):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                # tem=lst[j]
                lst[j],lst[j+1]=lst[j+1],lst[j]
                # lst[j+1]=tem
                count+=1
    return lst,count
