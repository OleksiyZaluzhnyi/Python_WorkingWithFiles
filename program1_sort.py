import re

UKRAINIAN_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UKRAINIAN_ORDER = {char: index for index, char in enumerate(UKRAINIAN_ALPHABET)}


def is_ukrainian(word):
    return bool(re.search(r'[а-яА-ЯіїєґІЇЄҐ]', word))


def ukrainian_sort_key(word):
    return [
        UKRAINIAN_ORDER.get(char.lower(), len(UKRAINIAN_ALPHABET) + ord(char.lower()))
        for char in word
    ]


def sort_words(words):
    return sorted(words, key=lambda w: (
        0 if is_ukrainian(w) else 1,
        ukrainian_sort_key(w) if is_ukrainian(w) else w.lower()
    ))


def main():
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    print("Оригінальний текст:\n")
    print(text)

    words = re.findall(r'\w+', text)

    sorted_words = sort_words(words)

    print("\nВідсортований список:\n")
    print(sorted_words)


if __name__ == "__main__":
    main()
