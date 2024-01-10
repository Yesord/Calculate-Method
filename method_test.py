import sys 
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))# 加入上上级目录
import math 
from Iterative_method_for_Linear_algebra_equations import GS_iterative_method as GS
from Iterative_method_for_Linear_algebra_equations import Jacobi_iterative_method as Jacobi
from Iterative_method_for_Linear_algebra_equations import SOR_iterative_method as SOR
from Numerical_Solutions_Of_Ordinary_Differential_Equations import Eular_solutions as Euler
print("Test start...\n")

GS.test()
Jacobi.test()
SOR.test()
Euler.test()

print("\nTest end...")