input = open("2015/Day2Pt1.txt", "r")
total = 0

def surface_area(h,w,l):
    return 2*l*w + 2*w*h + 2*h*l

def extra_paper(h,w,l):
    value_list = [h,w,l]
    value_list.sort()
    return value_list[0] * value_list[1]

def wrapping_paper(h,w,l):
    paper = surface_area(h,w,l)
    extra = extra_paper(h,w,l)
    return paper + extra

def ribbon(h,w,l):
    value_list = [h,w,l]
    value_list.sort()
    return 2*(value_list[0] + value_list[1])

def bow(h,w,l):
    return h*w*l

def total_ribbon(h,w,l):
    return ribbon(h,w,l) + bow(h,w,l)


assert(total_ribbon(2,3,4) == 34)
assert(total_ribbon(1,1,10) == 14)
for line in input:
    (h,w,l) = line.split("x")
    total += total_ribbon(int(h),int(w),int(l))

print(total)