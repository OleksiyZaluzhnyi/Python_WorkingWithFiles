from urllib.parse import unquote
import pyperclip

def main():
    url = input("Встав URL (закодований):\n")

    decoded_url = unquote(url)

    print("\nРозкодований URL:")
    print(decoded_url)

    pyperclip.copy(decoded_url)
    print("\nСкопійовано в буфер обміну!")


if __name__ == "__main__":
    main()