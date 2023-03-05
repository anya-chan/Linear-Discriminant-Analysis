import numpy as np
import math

def GaussianDiscriminantAnalysis(X1, X2):
    N1 = X1.shape[0]
    N2 = X2.shape[0]
    N = N1 + N2
    phi = N1/(N1 + N2)#take average of y i.e. y is classes
    print("P1 = " + str(phi))
    mu1 = np.mean(X1, axis = 0) #sum up each col and take average
    mu2 = np.mean(X2, axis = 0) #sum up each col and take average
    print("mu1 = " + str(mu1))
    print("mu2 = " + str(mu2))
    S1 = (1/N1)*np.matmul((X1-mu1).T,(X1-mu1))
    print("S1 = " + str(S1))
    S2 = (1/N2)*np.matmul((X2-mu2).T,(X2-mu2))
    print("S2 = " + str(S2))
    
    S = (N1/N)*S1 + (N2/N)*S2
    print("S = " + str(S))
    
    S_inverse = np.linalg.inv(S) #inverse a matrix
    print("Sinv=" + str(S_inverse))
    
    mu_difference = mu1 - mu2
    w = np.matmul(S_inverse, mu_difference.T) #matmul = matrix multiplication this is w
    print("w = " + str(w))
    
    w0 = (np.log(phi / (1 - phi)) - 0.5*np.matmul(np.matmul(mu1,S_inverse),mu1.T)+0.5*np.matmul(np.matmul(mu2,S_inverse),mu2.T))
        
    print("w0 = " + str(w0))
    
    return [w,w0]
          




'''

plt.plot(x, y, c = "red")

plt.show()

plt.figure()

plt.plot(X_valid2[y_valid2 == 1, 0], X_valid2[y_valid2 == 1, 1], 'bx')
plt.plot(X_valid2[y_valid2 == 0, 0], X_valid2[y_valid2 == 0, 1], 'go')

plt.xlabel("x1")
plt.ylabel("x2")

x = np.arange(min(X_valid2[:, 0]), max(X_valid2[:, 1]), 0.01)
y = -1 * (gda2.w[0] / gda2.w[2] + gda2.w[1] / gda2.w[2] * x)

plt.plot(x, y, c = "red")

plt.show()


'''

