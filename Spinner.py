import random


class Spinner:
    def __init__(self, myresults_file):
        self.synonym_dict = self.load_synonyms(myresults_file)
        self.load_synonyms(myresults_file)

    def load_synonyms(self, results_file):
        synonym_dict = {}
        with open(results_file, 'r') as file:
            for line in file:
                word, synonyms = line.strip().split(':')
                synonym_dict[word] = synonyms.split(',')
        return synonym_dict

    def spinner_text(self, text):
        words = text.split()
        spinner_text = []

        for word in words:
            clean_word = word.lower().strip(".,!?")
            if clean_word in self.synonym_dict and random.randint(1, 100) > 50:
                spinner_text.append(random.choice(self.synonym_dict[clean_word]))
            else:
                spinner_text.append(word)
        return " ".join(spinner_text)
