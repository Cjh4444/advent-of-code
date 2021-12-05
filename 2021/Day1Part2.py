with open("inputs/Day1Input.txt") as f:
    inputs = [int(line.strip()) for line in f]
    print()
    result = 0
    for i in range(len(inputs)):
        a = inputs[i]

        if i != len(inputs) - 3 :
            b = inputs[i+1]
            c = inputs[i+2]
            d = inputs[i+3]
        else:
            break
        
        set1 = a+b+c
        set2 = b+c+d
        
        if set2 > set1:
            result += 1
    print(result)
