"""

    Autores:
    Diogo Azevedo nº 104654 / Ricardo Madureira nº 104624
    19/11/2021

"""

# Imports
import sys
import re
from turtle import up
from typing import final       # Regex
import Stemmer  # Stemmer

""" Main Class """


class Tokenizer:

    pos_tokens = {}
    pos_tokensArr = []

    def __init__(self, min_tamanho, tokenizer_mode, steemer):
        self.stemmer = Stemmer.Stemmer('english')
        self.tokenizer_mode = tokenizer_mode
        self.min_tamanho = min_tamanho
        stopwords_file = "snowball_stopwords_EN.txt"

        if sys.argv[1] == "no":
            print("Minimo Tamanho palavra == 0")
        else:
            print("Minimo Tamanho palavra == ", self.min_tamanho)

        if tokenizer_mode == "no":
            self.stopwords = []
            print("Stopwords == No")
        elif tokenizer_mode == "yes":
            text = open(stopwords_file, 'r')
            self.stopwords = [word.strip() for word in text.readlines()]
            print("Stopwords == yes")
        else:
            try:
                print("tokenizer_mode -->", tokenizer_mode)
                self.stopwords_file = tokenizer_mode
                text = open(self.stopwords_file, 'r')
                self.stopwords = [word.strip() for word in text.readlines()]
                print("Stopwords == yes")
            except IOError:
                print("Error: File does not exist.")
                exit()

        print("Stemmer == ", sys.argv[3])

    def tokenize(self, input_string, index):
        final_tokens = []
        count_pos_word = 0

        tokens = re.sub("[^a-zA-Z]+", " ", input_string).lower().split(" ")

        if sys.argv[3] == "yes":
            tokens = self.stemmer.stemWords(tokens)

        if sys.argv[1] == "no":
            for token in tokens:
                if len(token) < 0 or token in self.stopwords:
                    continue
                else:
                    final_tokens.append((token, index))
        else:
            for token in tokens:
                count_pos_word += 1
                if len(token) < int(self.min_tamanho) or token in self.stopwords:
                    continue
                else:
                    final_tokens.append((token, index))
                    #final_tokens.append((token, index, count_pos_word))
                    self.pos_tokensArr.append({token : {index : (count_pos_word - 1)}})
                    """
                    if token not in self.pos_tokens:
                        self.pos_tokens[token] = {index : count_pos_word}
                    else:
                        if index not in self.pos_tokens[token]:
                            #self.pos_tokens[token].update({index:count_pos_word})
                            self.pos_tokens[token].update({index:count_pos_word})
                        else:
                            self.pos_tokens[token][index] += count_pos_word

                    #print("self.pos_tokens ->\n", self.pos_tokens.items())
                    """

            final_tokens

            # print("self.pos_tokensArr ->\n", self.pos_tokensArr)

        return final_tokens

    def tokenize2(self, input_string):
        final_tokens = []

        tokens = re.sub("[^a-zA-Z]+", " ", input_string).lower().split(" ")

        if sys.argv[3] == "yes":
            tokens = self.stemmer.stemWords(tokens)

        for token in tokens:
            if len(token) < int(self.min_tamanho) or token in self.stopwords:
                continue
            else:
                final_tokens.append(token)

            final_tokens

        return final_tokens
