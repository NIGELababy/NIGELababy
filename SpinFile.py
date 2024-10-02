import string

from Spinner import Spinner


def main():
    with open('essay.txt', 'r') as essay_file:
        original_text = essay_file.read().lower()

    original_text = original_text.translate(str.maketrans('', '', string.punctuation))

    print("Original: ", original_text)

    spinner = Spinner('myresults.txt')
    for i in range(1, 4):
        spinner_text = spinner.spinner_text(original_text)
        print(f"Option {i}: ", spinner_text)


if __name__ == "__main__":
    main()
