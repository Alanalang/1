while True:
    try:
        # n:坐标系长度，k:青蛙初始位置
        n,k=list(map(int,input().split(' ')))
        s=input()

        # 第i步有可能在j位置
        now=[k]
        i=1

        for char in s:
            tmp=[]
            for i in now:
                if char =='R':
                    if i==n:
                        tmp.append(i)
                    else:
                        tmp.append(i+1)
                elif char =='L':
                    if i==1:
                        tmp.append(i)
                    else:
                        tmp.append(i-1)
                else:
                    if i==n:
                        tmp.append(i)
                        tmp.append(i-1)
                    elif i==1:
                        tmp.append(i)
                        tmp.append(i+1) 
                    else:
                        tmp.append(i-1)
                        tmp.append(i+1)                        
            now=list(set(tmp))
        
        res=['0']*n
        for item in now:
            res[item-1]='1'
        print(''.join(res))


    except:
        break