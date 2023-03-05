import math

def DecisionThreshold(p1, mu1, mu2, Var1, Var2):
    a = Var1 - Var2
    b = 2*mu1*Var2-2*mu2*Var1
    c = (mu2**2)*Var1 - (mu1**2)*Var2 +Var1*Var2*math.log(((p1**2)*Var2)/(((1-p1)**2)*Var1))
    
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    
    s1 = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
    print("s1 = " + str(s1))
    s2 = (-b - math.sqrt((b**2)-4*a*c))/(2*a)
    print("s2 = " + str(s2))
    
    return [s1, s2]

