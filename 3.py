
import numpy as np

x=6.0
y=0.0
iter=1000000
lr=0.3

def sigmoid(x):
    return 1/(1+np.exp(-x))



#x^2-3x+2=0
# def gradient_descent(a, b, c, x0=10,lr=0.001, max_iter=1000,y=0):

#     x=x0

#     for _ in range(max_iter):
#         p= a*x**2+b*x+c
#         loss=(p-y)**2

#         grad=2*(p-y)*(2*a*x+b)

#         x-=grad*lr

#         if loss<0.00001:
#             break
    
#     return x

def gradient_descent(x0=0.3,lr=0.1, max_iter=1000,y=0.5):

    x=x0

    for _ in range(max_iter):

        p= sigmoid(x)
        loss=(p-y)**2

        grad=2*(p-y)*p*(1-p)

        x-=grad*lr

        if loss<0.00001:
            break
    
    return x

# 示例：求解 x² -5x +6=0（两实根x=2, x=3）
roots = gradient_descent(y=0.5)
print(f"方程解：x = {roots}")


