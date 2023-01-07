# n=number of the charge
#p momentum
#E_kin kinetic energy of the particle
#m0 rest mass
#q total charge
import math 
def get_rigidty(m0,E_kin,n):
    c=299792458 #speed of light
    q=n*1.602e-19
    p=math.sqrt((E_kin/c)**2+(2*E_kin*m0))
    rigidity=p/q
    print("magnetic rigidity=",rigidity, "Tm")
    
get_rigidty(3.9521e-25,7.245e-9,28) #for question 1
get_rigidty(3.27e-25,1.294e-8,77) #for question 2
get_rigidty(9.109e-31,1.602e-9,1) #for question 3

