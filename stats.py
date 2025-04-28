def num_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def count_characters(file_contents):
    counts = {}
    for char in file_contents.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_count(char_counts):
    def sort_on(dict):
        return dict["num"]
    
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list