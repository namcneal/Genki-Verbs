import FileIO
from Conjugation import *
import unicodecsv, codecs, cStringIO



class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=unicodecsv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = unicodecsv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

mori_list = open("Example_Verbs_.csv","w+")

writer = UnicodeWriter(mori_list)
writer.writerow(["Regular", "Potential", "Passive", "Causative","Causative-Passive",
                 "Plain present positive", "Plain present negative","Plain past positive","Plain past negative",
                 "Polite present positive","Polite present negative","Polite past positive","Polite past negative",
                 "Te form",
                 "Tai present positive", "Tai present negative","Tai past positive","Tai past negative",
                 "Polite volitional", "Casual volitional",
                 "Tara positive", "Tara negative",
                 "Ba"
                ])

for verb in FileIO.get_verb_array(range(3,11),u=True,ru=True,irr=True):
    row = list()
    row.append(verb.kanji)
    try:
        row.append(verb.potential().kanji)
    except AttributeError:
        row.append("")
    
    try:
        row.append(verb.passive().kanji)
    except AttributeError:
        row.append("")
    
    try:
        row.append(verb.causative().kanji)
    except AttributeError:
        row.append("")
    
    try:
        row.append(verb.causative_passive().kanji)
    except AttributeError:
        row.append("")
    
    for i in ["plain","polite"]:
        for j in [non_past, past]:
            for k in ["positive", "negative"]:
                row.append(j(verb,i,k)[0])    
    row.append(te(verb)[0])
    for i in ["plain"]:
        for j in ["present","past"]:
            for k in ["positive", "negative"]:
                a = tai(verb,i,k,j)
                if a == None:
                    row.append("")
                else:
                    row.append(a[0]) 
    
    row.append(tara(verb, speech_level="plain", polarity="positive")[0])
    row.append(tara(verb, speech_level="plain", polarity="negative")[0])
    row.append(ba(verb)[0])
    

    
    writer.writerow(row)


