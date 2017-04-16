from Conjugation import *
from FileIO import *
from Verb import Verb

array = get_verb_array(range(3,11))
for verb in array:
    try:
        print tai(verb.causative())[0]
    except TypeError:
        print "N/A"


