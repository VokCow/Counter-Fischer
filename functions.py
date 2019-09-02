import numpy as np
import copy

def eigs(Matrix,Rounded=True):
    '''
    returns ordered set of eigenvaleus and eigenvectors of 
    a given Matrix, rounded to 2 by default. 
    Numpy and Copy modules are required 
    '''
    E=np.linalg.eig(Matrix)
    if(Rounded):vals,aux=np.around(E[0],2),np.around(E[1],2)
    else: vals,aux=E[0],E[1]
    vecs=copy.deepcopy(aux)
    indxs=vals.argsort()
    vals.sort()
    for i in range(len(vals)):
        vecs[:,i]=aux[:,indxs[i]] 
    return vals,vecs
 

def CounterFischer(S,k):
    vals,vecs=eigs(S)
    n=len(S)
    if(k>n): 
        print('k provided greater than S dimension')
        return
    else:
        kprim=n-k+1
        print('Let k = ', k ,' \n S is the eigenspace formed by the eigenvectors with greatest eigenvalues of the specturm, that is: ')
        print('S = span(',vecs[:,-k:],')')
        print('Therefore, lambda_k is the minimum egienvalue corresponding to these eigenvectors, lambda_k=lambda_',k,'= min(',vals[-k:],') = ',min(vals[-k:]))
        print('T is the eigenspace with dim n-k+1=',n,'-',k,'+',1,'=',kprim,', formed by the eigenvectors with smallest eigenvalues of the specturm, that is: ')
        print('T = span(',vecs[:,:kprim],')')
        print('Therefore lambda_k the maximum eigenvalue corresponding to these eigenvectors \n lambda_k=lambda_',k,'= min(',vals[:kprim],') = ',max(vals[:kprim]))
