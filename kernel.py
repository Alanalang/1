import math

# 定义 RBF 核矩阵计算函数
def rbf_kernel_matrix(X, gamma=1.0):
    """
    计算给定数据集 X 的 RBF 核矩阵。
    
    参数:
        X: 输入数据集，列表形式，每个元素是一个特征向量
        gamma: RBF 核的参数
        
    返回:
        K: RBF 核矩阵，列表形式
    """
    n = len(X)
    K = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i <= j:  # 只计算上三角部分，因为它是对称的
                dist = (X[i][0]-X[j][0])**2+(X[i][1]-X[j][1])**2
                K[i][j] = math.exp(-gamma * dist)
                K[j][i] = K[i][j]  # 对称性填充
                
    return K

# 示例数据
X = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# 计算 RBF 核矩阵
gamma = 1.0  # 可以根据需要调整 gamma 值
K = rbf_kernel_matrix(X, gamma)

print("RBF Kernel Matrix:")
for row in K:
    print(row)