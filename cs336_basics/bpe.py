text = """
low low low low low
lower lower widest widest widest
newest newest newest newest newest newest
"""

def get_frequency(text):
    # Get frequency
    frequency = {}
    for line in text.split("\n"):
        for word in line.split():
            bytes = tuple(i for i in word)
            if bytes not in frequency:
                frequency[bytes] = 0
            frequency[bytes] += 1
    return frequency

def merges(frequency, merged, run, limit):

    if run >= limit:
        return frequency, merged
    
    # Get the frequence of pairs
    pairs = {}
    merged = merged.copy()
    for bytes, count in frequency.items():
        for i in range(len(bytes) - 1):
            pair = (bytes[i], bytes[i+1])
            if pair not in pairs:
                pairs[pair] = 0
            pairs[pair] += count

    # Find the most frequent pair with exicographically greatest value
    sorted_items = sorted(
        pairs.items(),
        key=lambda x: (x[1], max(x[0])),
        reverse=True
    )
    max_val = max(pairs.values())
    max_keys = [k for k, v in pairs.items() if v == max_val]
    top_pair = max(max_keys)
    
    merged.append(top_pair)
    top_pair_value = (''.join(top_pair),)
    # Replace the most frequent pair of bytes with the merged pair
    keys = list(frequency.keys())
    for bytes in keys:
        for i in range(len(bytes) - 1):
            
            if bytes[i] == top_pair[0] and bytes[i+1] == top_pair[1]:
                
                new_bytes = bytes[:i] + top_pair_value + bytes[i+2:]
                frequency[new_bytes] = frequency[bytes]
                del frequency[bytes]

           
    return merges(frequency, merged, run+1, limit)

res, merged = merges(get_frequency(text), [], 0, 6)

print(res, "\n\n")
print(merged)
