import numpy as np

def dct_new(x_sig):
    #based on formula from https://benchpartner.com/describe-discrete-cosine-transform-dct-with-example/
    N=len(x_sig) #Assume N is even
    x_dct=np.zeros(N)
    x_dct[0:N]=x_sig
    X_dct=np.fft.fft(x_dct[0:N])
    for u in range(0,N):
        X_dct[u]=X_dct[u]*np.exp(np.complex(0,-1)*np.pi*u/(2*N))
        #now we take only the cosine
        X_dct=X_dct.real
        X_dct=X_dct
    return X_dct



x=range(10)
dct=dct_new(x)
print(dct)