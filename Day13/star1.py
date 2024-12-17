from itertools import islice
import re

with open("test.txt") as f:
    total = 0
    while True:
        lines = [x.strip() for x in islice(f, 3)]        
        if not lines:
            break
                
        button_A = [int(x[1:]) for x in re.findall(r"\+\d+", lines[0])]
        button_B = [int(x[1:]) for x in re.findall(r"\+\d+", lines[1])]
        prize = [int(x[1:]) for x in re.findall(r"\=\d+", lines[2])]
        
        max_num_of_A_presses_to_X = prize[0] // button_A[0] + 1
        max_num_of_B_presses_to_X = prize[0] // button_B[0] + 1
        max_num_of_A_presses_to_Y = prize[1] // button_A[1] + 1       
        max_num_of_B_presses_to_Y = prize[1] // button_B[1] + 1
        
        possible_solutions = set()
        
        for i in range(max_num_of_A_presses_to_X):
            for j in range(max_num_of_B_presses_to_X):
                if (i * button_A[0] + j * button_B[0] == prize[0] and
                    i * button_A[1] + j * button_B[1] == prize[0]):
                    possible_solutions.add((i,j))
        
        for i in range(max_num_of_A_presses_to_Y):
            for j in range(max_num_of_B_presses_to_Y):
                if i * button_A[1] + j * button_B[1] == prize[1] and i * button_A[0] + j * button_B[0] == prize[0]:
                    possible_solutions.add((i,j))
        
        # print(possible_solutions)
        
        min = -1
        ans = None
        
        for solution in possible_solutions:
            value = solution[0] * 3 + solution[1]
            if min == -1 or value < min:
                min = value
                ans = solution
        
        if ans != None:
            total += ans[0] * 3 + ans[1]
            print("can be done")
        else:
            print("can't be done")
        
        f.readline()
print(total)        