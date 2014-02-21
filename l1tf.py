import numpy as np
from numpy.linalg import inv, norm
import matplotlib.pyplot as plt
from pandas import Series

def main():
    y = np.array([1,2,2,2.5,3,5,5,6,4,4,3.5])
    x = l1tf(y, 0.5)
    
def l1tf(y, lamda):
    
    # Parameters
    alpha     = 0.01
    beta      = 0.5
    mu        = 2
    maxiter   = 40
    maxlsiter = 20
    tol       = 1e-4
    
    # Dimensions
    n = y.size
    m = n - 2
    
    # Operator matrices
    I2 = np.identity(n-2)
    O2 = np.zeros((n-2, 1))
    D  = np.concatenate([I2, O2, O2], axis=1) + \
        np.concatenate([O2, -2*I2, O2], axis=1) + \
        np.concatenate([O2, O2, I2], axis=1)
        
    DDT = D.dot(D.T)
    Dy  = D.dot(y)
    
    # Variables
    z   = np.zeros((m, 1))
    mu1 = np.ones((m, 1))
    mu2 = np.ones((m, 1))
    
    t = 1e-10
    pobj = 10000000
    dobj = 0
    step = 0 
    f1 = z - lamda
    f2 = -z - lamda
    
    # Main Loop
    
    for iters in range(maxiter):
        DTz  = (z.T.dot(D)).T
        DDTz = D.dot(DTz)
        w    = (Dy - (mu1 - mu2).T).T
        
        # two ways to evaluate primal objective:
        # 1) using dual variable of dual problem
        # 2) using optimality condition
        pobj1 = 0.5 * w.T.dot(inv(DDT).dot(w)) + lamda * np.sum(mu1+mu2)
        pobj2 = 0.5 * DTz.T.dot(DTz) + lamda * np.sum(np.abs(Dy - DDTz))        
        pobj = min(pobj1, pobj2)
        dobj = -0.5 * DTz.T.dot(DTz) + Dy.T.dot(z)
        gap = pobj - dobj
        
        # Stopping Criterion
        if (gap <= tol):
            print 'Solved'
            x = y - D.T.dot(z)
            line = Series(x[0])
            print 'yo'
            line.plot()
            
            return line
        
        if step >= 0.2:
            t = max(2 * m * mu / gap, 1.2 * t)  
            
        # Calculate Newton Step
        
        rz   = DDTz - w
        vec  = np.divide(mu1,f1) + np.divide(mu2,f2)
        S    = DDT - np.diag(vec)
        r    = np.divide((zip(*-DDTz) + Dy).T + (1/t), f1) - np.divide(1/t,f2)
        dz   = inv(S).dot(r)
        dmu1 = -np.divide(mu1 + ((1/t) + dz.T.dot(mu1)),f1)
        dmu2 = -np.divide(mu2 + ((1/t) + dz.T.dot(mu2)),f2)
        
        resDual  = rz.T
        resCent  = np.concatenate([(-mu1*f1 - 1/t).T, (-mu2*f2 - 1/t).T], axis = 0)
        residual = np.concatenate([resDual, resCent], axis=0)
        
        # Backtracking Linesearch
        negIdx1  = dmu1 < 0
        negIdx2  = dmu2 < 0
        step = 1
        if (np.any(negIdx1)):
            step = min(step, 0.99*min(np.divide(-mu1[negIdx1],dmu1[negIdx1])))
        if (np.any(negIdx2)):
            step = min(step, 0.99*min(np.divide(-mu2[negIdx2],dmu2[negIdx2])));
            
        for liter in range(maxlsiter):
            newz = z + step * dz
            newmu1 = mu1 + step * dmu1
            newmu2 = mu2 + step * dmu2
            newf1 = newz - lamda
            newf2 = -newz - lamda
            
            # Update Residual
            newResDual = DDT.dot(newz) - Dy + newmu1 - newmu2
            newResCent = np.concatenate([(-newmu1 * newf1 - 1/t).T, (-newmu2 * newf2 - 1/t).T], axis=0)
            newResidual = np.concatenate([newResDual, newResCent], axis=0)
            
            if (max(max(newf1), max(newf2)) < 0 and \
                    norm(newResidual) <= (1 - alpha * step) * norm(residual)):
                break
            step = beta * step
            
            # Update primal and dual variables
            z = newz
            mu1 = newmu1
            mu2 = newmu2
            f1 = newf1
            f2 = newf2
        
        x = y - D.T.dot(z)
        print iters
        if (iters >= maxiter - 1):
            print 'Maxiters exceeded'
            return x
    
    print 'Nothing happened'

if __name__ == '__main__':
    main()
    
