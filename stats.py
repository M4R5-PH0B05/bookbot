def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_characters(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_characters(char_counts):
    char_list = [{"char": c, "num": n} for c, n in char_counts.items()]

    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
