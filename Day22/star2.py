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
    price_sequences = set()
    
    secret_prices_diff_dict = {}
    
    list_of_dicts = []
    
    for secret in f:
        num = int(secret.strip())
        prices = [num % 10]
        for i in range(2000):
            num = next_secret(num)
            prices.append(num % 10)
            
            
        diff = []
        for p1, p2 in zip(prices, prices[1:]):
            diff.append(p2 - p1)
        
        individual_sequence_to_val = {}
        for i in range(len(diff)):
            if i >= 4:
                sequence = tuple(diff[i - 4: i])
                if sequence not in individual_sequence_to_val:
                    individual_sequence_to_val[sequence] = prices[i]  
        
        list_of_dicts.append(individual_sequence_to_val)      
        
    # print("done indexing dictionarys")

    sequence_to_total_price = {}

    for i, dictionary in enumerate(list_of_dicts):
        # print(f"working on dictionary {i}")
        for k,v in dictionary.items():
            if k not in sequence_to_total_price:
                sequence_to_total_price[k] = v
            else:
                sequence_to_total_price[k] += v
    
    print(max(zip(sequence_to_total_price.values(), sequence_to_total_price.keys())))

      