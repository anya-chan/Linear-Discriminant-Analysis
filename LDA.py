import numpy as np

def LDA(X1, X2):
    N1 = X1.shape[0]
    N2 = X2.shape[0]
    mu1 = np.mean(X1, axis = 0) #sum up each col and take average
    mu2 = np.mean(X2, axis = 0) #sum up each col and take average
    print("mu1 = " + str(mu1))
    print("mu2 = " + str(mu2))
    S1 = np.matmul((X1-mu1).T,(X1-mu1))
    S2 = np.matmul((X2-mu2).T,(X2-mu2))
    print("S1 = " + str(S1))
    print("S2 = " + str(S2))
    Sw = S1 + S2
    print("Sw = " + str(Sw))
    SB = np.linalg.inv(Sw)
    #print("mu2-mu1" + str((mu2-mu1).T))
    print("SB = " + str(SB))
    w_non = np.matmul(SB,(mu2-mu1).T)
    w = w_non / np.linalg.norm(w_non)
    print("w = " + str(w))
    Y1 = np.matmul(X1,w.T)
    print("Y1 = " + str(Y1))
    Y2 = np.matmul(X2,w.T)
    print("Y2 = " + str(Y2))
    
    mu_Y1 = (1/N1)*(np.sum(Y1))
    print("mu_Y1 = " + str(mu_Y1))
    
    Var_Y1 = (1/(N1-1))*np.sum((Y1-mu_Y1)**2)
    print("Var_Y1 = " + str(Var_Y1))
    
    mu_Y2 = (1/N2)*(np.sum(Y2))
    print("mu_Y2 = " + str(mu_Y2))
    
    Var_Y2 = (1/(N2-1))*np.sum((Y2-mu_Y2)**2)
    print("Var_Y2 = " + str(Var_Y2))
    
    return [mu_Y1, mu_Y2, Var_Y1, Var_Y2, w, Y1, Y2]
