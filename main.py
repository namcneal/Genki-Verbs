# -*- coding: utf-8 -*-
from Verb import Verb
from Conjugation import regular,te,tara, tai
import FileIO


test_list = FileIO.import_verb_list('testing_verb_list.csv')
test_verbs = list()

for row in test_list:
    test_verbs.append(Verb(row[0], row[1], row[2], row[3]))

for verb in test_verbs:
    """for level in ["plain", "polite"]:
        for polarity in ["positive", "negative"]:
            for tense in ["present", "past"]:
                print regular(verb, level, polarity, tense)[0]"""
    print tai(verb)[0]
    
