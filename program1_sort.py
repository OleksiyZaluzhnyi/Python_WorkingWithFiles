import re

def is_ukrainian(word):
    return bool(re.search(r'[а-яА-ЯіїєґІЇЄҐ]', word))


def sort_words(words):
    return sorted(words, key=lambda w: (
        0 if is_ukrainian(w) else 1,
        w.lower()
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