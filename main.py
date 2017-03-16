# -*- coding: utf-8 -*-
from Verb import Verb
from Conjugation import regular,te,tara, tai,ba,get_random_conjugation
import FileIO


test_list = FileIO.import_verb_list('testing_verb_list.csv')
test_verbs = list()

for row in test_list:
    test_verbs.append(Verb(row[0], row[1], row[2], row[3]))

def test():
    for verb in test_verbs:
        for i in range(0,60):
            print get_random_conjugation(verb,[0,1,2], [0,1,2,3,4,5],plain = True, polite = True, pos = True, neg = True, past = True, pres = True, kana = True, kanji = True)

if __name__ == '__main__':
    test()
