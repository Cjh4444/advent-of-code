from collections import deque
incorrect_list = ['z34', 'z26', 'z25', 'z24', 'z23', 'z19', 'z17', 'z16', 'z15', 'z14']
in_to_out: dict[str, list[str]] = {}
out_to_in = {}

# def print_tree(output, tab=0):
#     print(tab * " " + f"{output} = {out_to_in[output]}")
    
#     left_path, op, right_path = out_to_in[output].split()
    
#     if not left_path.startswith("x") and not left_path.startswith("y"):
#         print_tree(left_path, tab + 1)
#     # else:
#     #     print(tab * " " + f"{left_path}")
    
#     if not right_path.startswith("x") and not right_path.startswith("y"):
#         print_tree(right_path, tab + 1)
#     # else:
#     #     print(tab * " " + f"{right_path}")
    

# with open("data.txt") as f:
#     _ = f.read().split("\n\n")
    
#     start_vals = _[0].split("\n")
#     vals_to_check = _[1].split("\n")

#     register_to_binary = {}

#     for _ in start_vals:
#         string, binary_val = _.split(":")
#         register_to_binary[string] = int(binary_val)
        
#     # x_registers = [register for register in register_to_binary if register.startswith("x")]
#     # y_registers = [register for register in register_to_binary if register.startswith("y")]
    
#     # correct_num = 0
#     # carry_over = 0
#     # last_digit = len(x_registers) - 1

#     # for mult, (x, y) in enumerate(zip(sorted(x_registers), sorted(y_registers))):
#     #     digit = register_to_binary[x] + register_to_binary[y]
                
#     #     # Handle intermediate digits
#     #     if last_digit != mult:
#     #         if digit + carry_over >= 2:
#     #             correct_num += (digit + carry_over - 2) * 10 ** mult
#     #             carry_over = 1
#     #         else:
#     #             correct_num += (digit + carry_over) * 10 ** mult
#     #             carry_over = 0
#     #     else:
#     #         if digit + carry_over >= 2:
#     #             correct_num += (digit + carry_over - 2) * 10 ** mult
#     #             correct_num += 10 ** (mult + 1) 
#     #         else:
#     #             correct_num += (digit + carry_over) * 10 ** mult
        
#     # print(correct_num)
#     # print(int(str(correct_num), 2))
        
#     for x in vals_to_check:
#         split_str = x.split("->")
#         in_to_out.setdefault(split_str[0].strip(), []).append(split_str[1].strip())
        
#     for k, v in in_to_out.items():
#         outputs = v
#         for output in outputs:
#             out_to_in[output] = k
    
#     # blah = set()
#     # for incorrect in incorrect_list:
#     #     print(f"{incorrect}: {output_to_input_dict[incorrect]}")
#     #     split_thing = output_to_input_dict[incorrect].split()
#     #     blah.add(split_thing[0])
#     #     blah.add(split_thing[2])

#     # blah2 = set()
#     # for bla in blah:
#     #     split_thing = output_to_input_dict[bla].split()
#     #     blah2.add(split_thing[0])
#     #     blah2.add(split_thing[2])
#     # print(len(blah2))
    
    
#     inputs = set(in_to_out.keys())
    
#     while inputs:
#         input_to_check = inputs.pop()
#         outputs = in_to_out[input_to_check]
        
#         left, op, right = input_to_check.split()
        
#         val = 0
        
#         if left in register_to_binary and right in register_to_binary:
#             if op == "AND":
#                 val = register_to_binary[left] and register_to_binary[right]
#             elif op == "OR":
#                 val = register_to_binary[left] or register_to_binary[right]
#             elif op == "XOR":
#                 val = register_to_binary[left] ^ register_to_binary[right]
            
#             for output in outputs:
#                 register_to_binary[output] = val
#         else:
#             inputs.add(input_to_check)
    
#     # for incorrect in incorrect_list:
#     #     print(incorrect)
#     #     print_tree(incorrect)

#     print_tree("z02")
        
#     # z_dict = {}
    
#     # for register, binary in register_to_binary.items():
#     #     if register.startswith("z"):
#     #         z_dict[register] = binary
        
#     # num = 0
#     # for mult, x in enumerate(sorted(list(z_dict.keys())[::-1])):
#     #     num += z_dict[x] * 10 ** mult
    
#     # print(num)
#     # print(int(str(num), 2))

# hyperneutrino solution

formulas = {}
with open("data.txt") as f:
    for line in f:
        if line.isspace(): break
    
    for line in f:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)
        
def make_wire(char, num):
    return char + str(num).rjust(2, "0")        

def verify_z(wire, num):
    print("vz", wire, num)
    op, x, y = formulas[wire]
    if op != "XOR": return False
    if num == 0: return sorted([x,y]) == ["x00", "y00"]
    return vix(x,num) and vcb(y, num) or vix(y, num) and vcb(x, num)

def vix(wire, num):
    print("vx", wire, num)
    op, x, y = formulas[wire]
    if op != "XOR": return False
    return sorted([x,y]) == [make_wire("x", num), make_wire("y", num)]

def vcb(wire, num):
    print("vc", wire, num)
    op, x, y = formulas[wire]
    if num == 1:
        if op != "AND": return False
        return sorted([x,y]) == ["x00", "y00"]
    if op != "OR": return False
    return vdc(x,num - 1) and vrc(y, num - 1) or vdc(y, num - 1) and vrc(x, num - 1)

def vdc(wire, num):
    print("vd", wire, num)
    op, x, y = formulas[wire]
    if op != "AND": return False
    return sorted([x,y]) == [make_wire("x", num), make_wire("y", num)]

def vrc(wire, num):
    print("vr", wire, num)
    op, x, y = formulas[wire]
    if op != "AND": return False
    return vix(x,num) and vcb(y, num) or vix(y, num) and vcb(x, num)

def verify(num):
    return verify_z(make_wire("z", num), num)

i = 0

while True:
    if not verify(i): break
    i += 1

print(f"failed on {make_wire("z", i)}")

print(",".join(sorted(["hbk", "z14", "kvn", "z18", "dbb", 'z23', "tfn", "cvh"])))