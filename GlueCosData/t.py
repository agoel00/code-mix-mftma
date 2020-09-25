from indictrans import Transliterator
vocab = []

with open('all_roman.txt', 'r') as infile:
    con = infile.readlines()

vocab = [x.strip('\n') for x in con]

trn = Transliterator(source='eng', target='hin')

with open('transliterations.txt', 'w+') as outfile:
    for word in vocab:
        deva = trn.transform(word)
        outfile.write(word + "\t" + deva + "\n")