from itertools import islice
import re

import numpy as np


with open("data.txt") as f:
    total = 0
    while True:
        lines = [x.strip() for x in islice(f, 3)]        
        if not lines:
            break
                
        button_A = [int(x[1:]) for x in re.findall(r"\+\d+", lines[0])]
        button_B = [int(x[1:]) for x in re.findall(r"\+\d+", lines[1])]
        prize = [int(x[1:]) + 10000000000000 for x in re.findall(r"\=\d+", lines[2])]
        
        A = np.array([[button_A[0], button_B[0]], [button_A[1], button_B[1]]])
        B = np.array(prize)

        solution = np.linalg.solve(A, B)
    
        rounded_sol = (round(solution[0]), round(solution[1]))
        
        rounded_solution_is_correct = (
            button_A[0] * rounded_sol[0] + button_B[0] * rounded_sol[1] == prize[0] and
            button_A[1] * rounded_sol[0] + button_B[1] * rounded_sol[1] == prize[1]
        ) 

        if np.all(solution > 0) and rounded_solution_is_correct:
            print(f"solution is a = {round(solution[0])}, b = {round(solution[1])}")
            total += solution[0] * 3 + solution[1]
        else:
            print("not valid")
        
        f.readline()
print(total)        