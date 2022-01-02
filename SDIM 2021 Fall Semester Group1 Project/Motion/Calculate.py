import sympy
import math

def CalculateAngle(length,high):
    #给定指定高度于长度抓取指定位置，仍需调试
    alpha3, alpha4, alpha5 = sympy.symbols("alpha3, alpha4, alpha5")
    # alpha3 = sympy.Symbol('alpha3')
    # alpha4 = sympy.Symbol('alpha4')
    # alpha5 = sympy.Symbol('alpha5')
    L = length
    H = high
    # res = [1.5,1.5,1.5]
    # for x in range(10):
    #     tns = sympy.nsolve([18*sympy.cos(alpha5) + 12*sympy.sin(alpha3) - L + 6, 18*sympy.sin(alpha5) + 12*sympy.cos(alpha3) - H + 3, alpha3 + alpha4 + alpha5 - 3/2*3.14],[alpha3,alpha4,alpha5],[res[0],res[1],res[2]])
    #     res[0] = tns[0]
    #     res[1] = tns[1]
    #     res[2] = tns[2]
    print("start")
    res = sympy.nsolve([24-L-9*alpha5**2+12*alpha3-2*alpha3**3,15-H+18*alpha5-3*alpha5**3-6*alpha3**2,alpha3+alpha4+alpha5-4.71],[alpha3, alpha4, alpha5],[1.5,1.71,1.5])
    #res = sympy.nonlinsolve([18*(1-alpha5**2/2+alpha5**4/24) + 12*(alpha3-alpha3**3/6+alpha3**5/120) - L + 6, 18*(alpha5-alpha5**3/6+alpha5**5/120) + 12*(1-alpha3**2/2+alpha3**4/24) - H + 3, alpha3 + alpha4 + alpha5 - 3/2*3.14],[alpha3, alpha4, alpha5])
    print("stop")
    alpha3 = Simplify(math.degrees(res[0]))
    alpha4 = Simplify(math.degrees(res[1]))
    alpha5 = Simplify(math.degrees(res[2]))
    if(alpha3<0 or alpha3>180 or alpha5<0 or alpha5>180 or alpha4<0 or alpha4>270):
        ans = [0,90,180]
        print(alpha3,alpha4,alpha5)
        return ans
    else:
        ans = [alpha3,alpha4,alpha5]
        print(alpha3,alpha4,alpha5)
        return ans

def Simplify(number):    
    while(number<0 or number>360):
        if(number<0):
            number += 360
        else:
            number -= 360
    number1 = int(number)
    return number1
