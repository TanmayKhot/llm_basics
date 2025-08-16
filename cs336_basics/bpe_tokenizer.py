import re
from optimized_bpe import *

# Read the whole file into one string
# with open("/home/tanmay/Desktop/python-projects/llm_basics/datasets/TinyStoriesV2-GPT4-valid.txt", "r", encoding="utf-8") as f:
#     data = f.read()

special_tokens = ['<|endoftext|>']

def preprocess_data(filepath, special_tokens):
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()

    escaped_tokens = [re.escape(token) for token in special_tokens]
    split_pattern = '|'.join(escaped_tokens)

    data = re.split(split_pattern, data)

    return data

# # List of stories
# stories = preprocess_data(data, special_tokens)

def train_bpe(input_path: str, vocab_size: int, special_tokens: list[str]):
    # 1. Read file
    data = preprocess_data(input_path, special_tokens)

    print("Data\n", data)
    # 2. Initialize token counts (like your frequency dict)
    
    vocab = {}
    id_counter = 0

    # Add special tokens first
    for tok in special_tokens:
        vocab[id_counter] = tok.encode("utf-8")
        id_counter += 1

    # 4. Iteratively merge until vocab size reached
    for batch in data:
        print("Batch\n", batch, "\n")
        print("Passing voab limit: ", vocab_size-len(vocab))
        token_counts = get_frequency(batch)
        merges, new_vocab = merges_bpe(token_counts, [], 0, vocab_size-len(vocab))
        # Add tokens from counts
        for token in new_vocab:
            vocab[id_counter] = token
            id_counter += 1

    return vocab, merges

vocab, merges = train_bpe('./sample.txt', 7, special_tokens)

print("Result\n")
print("Vocab\n ", vocab)
print("\nMerges:\n", merges)