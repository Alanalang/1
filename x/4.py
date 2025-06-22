
while True:
    try:
        # n:坐标系长度，k:青蛙初始位置
        n,k=list(map(int,input().split(' ')))
        s=input()

        # 第i步有可能在j位置
        dp=[False]*(n+2)
        dp[k]=True
        i=1

        for char in s:
            tmp=[False]*(n+2)
            for i in range(1,n+1):
                if dp[i]:
                    if char =='R':
                        if i==n:
                            tmp[i]=True
                        else:
                            tmp[i+1]=True
                    elif char =='L':
                        if i==1:
                            tmp[i]=True
                        else:
                            tmp[i-1]=True
                    else:
                        if i==n:
                            tmp[i]=True
                        if i==1:
                            tmp[i]=True   
                        tmp[i-1]=True
                        tmp[i+1]=True
            dp=tmp
        
        res=''
        for i in range(1,n+1):
            if dp[i]:
                res+='1'
            else:
                res+='0'
        print(res)


    except:
        break