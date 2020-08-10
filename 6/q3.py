import numpy as np

def zigzag(M,N):
    mat = np.arange(M*N).reshape(M,N)
    zig=np.concatenate([np.diagonal(mat[::-1,:],k)[::((-1)**(M-1))*(2*(k%2)-1)] for k in range(1-M,M+1)])
    return zig

zig=zigzag(3,4)
print (zig)