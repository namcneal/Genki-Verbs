# -*- coding: utf-8 -*-
from Verb import Verb
from Conjugation import regular,te,tara, tai,ba
import FileIO


test_list = FileIO.import_verb_list('testing_verb_list.csv')
test_verbs = list()

for row in test_list:
    test_verbs.append(Verb(row[0], row[1], row[2], row[3]))

for verb in test_verbs:
    print ba(verb,speech_level="polite",polarity="positive",tense="past")[0].encode("utf-8", errors='replace')
