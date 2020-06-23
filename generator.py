import nltk
from cleantext import clean
from emoji import demojize
#from nltk.stem import PorterStemmer
import re
import random

def generate_siht():
    text_samples = []
    sent_samples = []
    words = []
    with open('bloggy.txt', 'r') as reader:
        line = reader.readline()
        line = demojize(line)
        while line != '': 
            text_samples.append(line)
            line = reader.readline()
            line = demojize(line)
    print(text_samples)

    #porter = PorterStemmer()
    for sample in text_samples:
        for sent in nltk.sent_tokenize(sample):
            sent_samples.append(sent)

    for sent in sent_samples:
        for word in nltk.word_tokenize(sent):
            words.append(word)
    
    tagged_sentences = []
    word_tags = []
    for item in sent_samples:
        tagged = nltk.pos_tag(nltk.word_tokenize(item))
        print(tagged)
        tagged_sentences.append(tagged)

    sent_structs = []
    sent_count = 0
    for item in tagged_sentences:
        sent_structs.append("")
        for word_tuple in item:
            word_tags.append(word_tuple)
            sent_structs[sent_count] = sent_structs[sent_count] + " " + word_tuple[1] 
        sent_count += 1

    print(sent_structs)
    
    parts_dict = {}
    for tag in word_tags:
        if tag[1] not in parts_dict:
            parts_dict[tag[1]] = []
        if tag[0] not in parts_dict[tag[1]]:
            (parts_dict[tag[1]]).append(tag[0])
     
    #Generation Starts
    sent_to_generate = sent_structs[random.randint(0,len(sent_structs) - 1)]
    new_sent = ""
    for word in sent_to_generate.split(' '):
        if word in parts_dict:
            new_sent = new_sent + (parts_dict.get(word))[random.randrange(0,len(parts_dict[word]),1)] + " "
    print("\n" + new_sent)

    random.seed()

    sent_to_generate = sent_structs[random.randint(0,len(sent_structs) - 1)]
    new_sent = ""
    for word in sent_to_generate.split(' '):
        if word in parts_dict:
            new_sent = new_sent + (parts_dict.get(word))[random.randrange(0,len(parts_dict[word]),1)] + " "
    print("\n" + new_sent)

    fun_text = clean(new_sent,
    fix_unicode=True,               # fix various unicode errors
    to_ascii=True,                  # transliterate to closest ASCII representation
    lower=True,                     # lowercase text
    no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
    no_urls=False,                  # replace all URLs with a special token
    no_emails=False,                # replace all email addresses with a special token
    no_phone_numbers=False,         # replace all phone numbers with a special token
    no_numbers=False,               # replace all numbers with a special token
    no_digits=False,                # replace all digits with a special token
    no_currency_symbols=False,      # replace all currency symbols with a special token
    no_punct=False,                 # fully remove punctuation
    replace_with_url="<URL>",
    replace_with_email="<EMAIL>",
    replace_with_phone_number="<PHONE>",
    replace_with_number="<NUMBER>",
    replace_with_digit="0",
    replace_with_currency_symbol="<CUR>",
    lang="en"                       # set to 'de' for German special handling
    )

    return fun_text.capitalize()

generate_siht()

