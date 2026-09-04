"""

Name: Trevor Tourdot
Date: 09/02/2026

"""

import re
from collections import Counter


def read_text_file(filename):
    """
    Read and return the contents of a text file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def whitespace_tokenize(text):
    """
    Tokenize text using whitespace only.

    Example:
    "Hello world!" -> ["Hello", "world!"]
    """
    return text.split()


def preprocess_contractions(text):
    """
    OPTIONAL (Recommended):
    Separate common contractions like:
    don't -> do n't
    I'm -> I 'm

    Hint: Use re.sub()
    """
    #handles n't contractions
    text = re.sub(r"(?i)n['’]t\b", " n't", text)
    #handles common apostrophe contractions
    text = re.sub(r"(?i)['’](m|re|ve|ll|d|s)\b", r" '\1", text)
    return text


def regex_tokenize(text):
    """
    Tokenize text using regular expressions.

    Your tokenizer MUST handle:
    - punctuation (separate it)
    - numbers (keep decimals like 12.50 together)
    - contractions (after preprocessing)
    
    CHALLENGE:
    - Handle URLs OR emails OR hyphenated words
    """

    # OPTIONAL: Call contraction preprocessing
    text = preprocess_contractions(text)

    # Example starting point (you should improve this):
    pattern = (
        r"https?://[^\s]+"  # URLs
        r"|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"  # email addresses
        r"|\d+(?:\.\d+)?"  # integers and decimals
        r"|n't|'(?:m|re|ve|ll|d|s)"  # contraction endings
        r"|[A-Za-z]+(?:-[A-Za-z]+)+"  # hyphenated words
        r"|[A-Za-z]+"  # regular words
        r"|[^\w\s]"  # punctuation
    )

    tokens = re.findall(pattern, text)

    return tokens


def token_statistics(tokens):
    """
    Return:
    - total number of tokens
    - number of unique tokens
    - frequency counts
    """
    total = len(tokens)
    unique = len(set(tokens))
    frequencies = Counter(tokens)

    return total, unique, frequencies


def print_token_report(name, tokens):
    """
    Print:
    - total tokens
    - unique tokens
    - first 20 tokens
    """
    total, unique, frequencies = token_statistics(tokens)

    print(f"\n=== {name} ===")
    print(f"Total tokens: {total}")
    print(f"Unique tokens: {unique}")
    print(f"First 20 tokens: ", tokens[:20])
    print("Top 5 most common tokens: ", frequencies.most_common(5))


def compare_tokenizers(tokens1, tokens2):
    """
    Compare two token lists.
    """
    print("\n=== Comparison ===")

    print("Tokenizer 1 total:", len(tokens1))
    print("Tokenizer 2 total:", len(tokens2))

    print("Tokenizer 1 unique:", len(set(tokens1)))
    print("Tokenizer 2 unique:", len(set(tokens2)))

    print("\nTokenizer 1 sample:", tokens1[:10])
    print("Tokenizer 2 sample:", tokens2[:10])


def main():
    #Change this to the file you will provide
    filename = "Cthulhu.txt"

    try:
        text = read_text_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    # Run both tokenizers
    whitespace_tokens = whitespace_tokenize(text)
    regex_tokens = regex_tokenize(text)

    # Print reports
    print_token_report("Whitespace Tokenizer", whitespace_tokens)
    print_token_report("Regex Tokenizer", regex_tokens)

    # Compare results
    compare_tokenizers(whitespace_tokens, regex_tokens)


if __name__ == "__main__":
    main()