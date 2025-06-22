

import numpy as np


def sigmoid(x):

    return 1/(1+np.exp(-x))

def ce(p,y):

    loss=y*np.log(p)
    loss=-np.sum(loss,axis=-1)
    return np.mean(loss)

def logitRegress(x,y,lr=0.01,iter=1000):

    # x [batch,dim] y [batch,1]

    batch,dim=x.shape

    w=np.random.random([dim,1])
    b=np.random.random([1])

    for i in range(iter):

        logit=np.matmul(x,w)+b #[batch,1]
        p=sigmoid(logit) 

        dw=np.matmul(x.T,p-y)/batch
        db=np.sum(p-y)/batch

        w-=dw*lr
        b-=db*lr

        loss=ce(p,y)

        if i%100==0:
            print(loss)
    
    return w,b

# 特征矩阵 (5 samples, 2 features)
X = np.array([
    [2.0, 1.5],
    [1.2, 0.8],
    [-0.5, -1.0],
    [-1.5, -2.0],
    [3.0, 2.5]
])

# 标签向量 (二分类0/1)
y = np.array([
    [1],
    [1],
    [0],
    [0],
    [1]
])
# 训练逻辑回归模型
np.random.seed(42)

w,b=logitRegress(X,y)

print( sigmoid(np.matmul(X,w)))