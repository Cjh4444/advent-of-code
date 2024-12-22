def mix(secret, given):
    return secret ^ given

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    num = prune(mix(secret, secret * 64))
    num = prune(mix(num, num // 32))
    num = prune(mix(num, num * 2048))
    return num
    
with open("data.txt") as f:
    total = 0
    for secret in f:
        num = int(secret)
        for i in range(2000):
            num = next_secret(num)
        print(secret.strip(), num)    
        total += num
    print(total)
