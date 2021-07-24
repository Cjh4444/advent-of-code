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



assert(wrapping_paper(2,3,4) == 58)
assert(wrapping_paper(1,1,10) == 43)
for line in input:
    (h,w,l) = line.split("x")
    total += wrapping_paper(int(h),int(w),int(l))

print(total)