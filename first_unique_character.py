def first_unique_char(str):
    dis={}
    count=0;
    for ch in str:
        if ch in dis:
            dis[ch]=-1;
        else:
            dis[ch]=count;
        count=count+1;
    temp=min(i for i in dis.values() if i > 0)
    return [key for key in dis if dis[key]==temp]

print(first_unique_char('mainshma'))