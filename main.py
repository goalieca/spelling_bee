from typing import Set


def find_words(filename: str, min_len: int, letters: Set, central: str) -> [str]:
    assert len(central) == 1, "central is supposed to be a single letter"
    words = []
    with open(filename, "r") as file:
        for line in file:
            word = line.rstrip()
            if len(word) >= min_len:
                matches = False
                for c in word:
                    if c == central:
                        matches = True
                        continue
                    if c not in letters:
                        matches = False
                        break
                if matches:
                    words.append(word)
    return words


answers = find_words('wordsEn.txt', 4, {'n', 'o', 'a', 'i', 'l', 't'}, 'd')
print(sorted(answers, key=len, reverse=True))
