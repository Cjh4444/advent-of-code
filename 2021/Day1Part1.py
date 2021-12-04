with open("inputs/Day1Input.txt") as f:
    inputs = [int(line.strip()) for line in f]
    result = 0
    for i in range(len(inputs)):
        a = inputs[i]
       
        if i != len(inputs) - 1 :
            b = inputs[i+1]
        else:
            break

        if b > a:
            result += 1
    print(result)
