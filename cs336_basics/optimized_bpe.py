from collections import defaultdict

# text = """
# low low low low low
# lower lower widest widest widest
# newest newest newest newest newest newest
# """

def get_frequency(text):
    # Get frequency
    frequency = defaultdict(int)
    for line in text.split("\n"):
        for word in line.split():
            word_bytes = word.encode("utf-8")
            bytes_tuple = tuple([ bytes([b]) for b in word_bytes ])
            frequency[bytes_tuple] += 1
    return frequency

def get_vocab(d):
    vocab = set()
    for word in d.keys():
        for i in word:
            vocab.add(i)
    return vocab

def merges_bpe(frequency, merges, run, limit):
    

    vocab = get_vocab(frequency)
    if len(vocab) == limit or (merges == [] and limit > len(vocab)):
        return merges, vocab
    
    # Get the frequency of pairs
    pairs = defaultdict(int)
    word_index = defaultdict(list)

    merges = merges.copy()
    for bytes, count in frequency.items():
        for i in range(len(bytes) - 1):
            pair = (bytes[i], bytes[i+1])
            pairs[pair] += count
            word_index[pair].append(bytes)

    # Find the most frequent pair with lexicographically greatest value
    sorted_items = sorted(
        pairs.items(),
        key=lambda x: (x[1], max(x[0])),
        reverse=True
    )
    max_val = max(pairs.values())
    max_keys = [k for k, v in pairs.items() if v == max_val]
    top_pair = max(max_keys)
    top_pair_value = (b''.join(top_pair),)

    merges.append(top_pair)
    
    # Replace the most frequent pair of bytes with the merges pair
    keys = word_index[top_pair]
    for bytes in keys:
        for i in range(len(bytes) - 1):
            if (bytes[i], bytes[i+1]) == top_pair:
                new_bytes = bytes[:i] + top_pair_value + bytes[i+2:]
                frequency[new_bytes] = frequency[bytes]
                del frequency[bytes]
     
    return merges_bpe(frequency, merges, run+1, limit)

#merges, vocab = merges_bpe(get_frequency(text), [], 0, 8)




