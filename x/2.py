while True:
    try:

        #数据组数
        t=int(input())
        for _ in range(t):
            #字符串长度
            n=int(input())
            s=input()

            #字符串由01组成
            #权值=使字符串任意相邻的两个字符不相等需要的最少编辑次数

            #字符串[i:j+1]需要的最小编辑次数
            dp=[[0]*n for i in range(n)]
            res=0

            for L in range(1,n):
                for i in range(n-L):
                    j=i+L
                    if j-i==0:
                        dp[i][j]=0
                    elif j-i==1 and s[i]==s[j]:
                        dp[i][j]=1
                        res+=1
                    else:
                        dp[i][j]=dp[i][j-1]
                        if s[j]==s[j-1]:
                            dp[i][j]+=1
                        res+=dp[i][j]
            print(res)

    except:
        break
