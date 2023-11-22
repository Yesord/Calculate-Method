import sys 
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))# 加入上上级目录
import math 
from Iterative_method_for_Linear_algebra_equations import GS_iterative_method as GS
from Iterative_method_for_Linear_algebra_equations import Jacobi_iterative_method as Jacobi
from Iterative_method_for_Linear_algebra_equations import SOC_iterative_method as SOC

print("Test start...\n")

GS.test()
Jacobi.test()
SOC.test()

print("\nTest end...")