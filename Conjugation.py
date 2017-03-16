# -*- coding: utf-8 -*-
import random

"""All the conjugation methods you could ever want. Returns tuples of (kanji, kana)"""

def regular(verb, speech_level="plain", polarity="positive",tense="present"):
    does_not_exist = []

    if verb in does_not_exist:
        return None
    
    # Ichidan Verbs
    elif verb.group == u"ru":
        ending = ""
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                if tense == "present":
                    ending = u"る"
                elif tense == "past":
                    ending = u"た"
            # Negative
            elif polarity == "negative":
                if tense == "present":
                    ending = u"ない"
                elif tense == "past":
                    ending = u"なかった"

        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
                if tense == "present":
                    ending =  u"ます"
                elif tense == "past":
                    ending = u"ました"
            # Negative
            elif polarity == "negative":
                if tense == "present":
                    ending = u"ません"
                elif tense == "past":
                    ending = u"ませんでした"

        return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)
    
    # Godan
    elif verb.group == u"u":
        ending = ""
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                if tense == "present":
                    ending = verb.kana[-1]
                elif tense == "past":
                    
                    endings = {u"う" : u"った",
                               u"つ" : u"った",
                               u"る" : u"った",
                               u"む" : u"んだ",
                               u"ぶ" : u"んだ",
                               u"ぬ" : u"んだ",
                               u"す" : u"した",
                               u"く" : u"いた",
                               u"ぐ" : u"いだ"}

                    ending = endings[verb.kana[-1]]
                    if verb.kana == u"いく": ending = u"った"
                    
            # Negative
            elif polarity == "negative":
                if tense == "present":
                    endings = {u"う" : u"わない",
                               u"つ" : u"たない",
                               u"る" : u"らない",
                               u"む" : u"まない",
                               u"ぶ" : u"ばない",
                               u"ぬ" : u"なない",
                               u"す" : u"さない",
                               u"く" : u"かない",
                               u"ぐ" : u"がない"}
                    ending = endings[verb.kana[-1]]
                elif tense == "past":
                    endings = {u"う" : u"わなかった",
                               u"つ" : u"たなかった",
                               u"る" : u"らなかった",
                               u"む" : u"まなかった",
                               u"ぶ" : u"ばなかった",
                               u"ぬ" : u"ななかった",
                               u"す" : u"さなかった",
                               u"く" : u"かなかった",
                               u"ぐ" : u"がかった"}
                    ending = endings[verb.kana[-1]]

        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
                if tense == "present":
                    endings = {u"う" : u"います",
                               u"つ" : u"ちます",
                               u"る" : u"ります",
                               u"む" : u"みます",
                               u"ぶ" : u"びます",
                               u"ぬ" : u"にます",
                               u"す" : u"します",
                               u"く" : u"きます",
                               u"ぐ" : u"ぎます"}
                    ending = endings[verb.kana[-1]]
                elif tense == "past":
                    endings = {u"う" : u"いました",
                               u"つ" : u"ちました",
                               u"る" : u"りました",
                               u"む" : u"みました",
                               u"ぶ" : u"びました",
                               u"ぬ" : u"にました",
                               u"す" : u"しました",
                               u"く" : u"きました",
                               u"ぐ" : u"ぎました"}
                    ending = endings[verb.kana[-1]]
            # Negative
            elif polarity == "negative":
                if tense == "present":
                    endings = {u"う" : u"いません",
                               u"つ" : u"ちません",
                               u"る" : u"りません",
                               u"む" : u"みません",
                               u"ぶ" : u"びません",
                               u"ぬ" : u"にません",
                               u"す" : u"しません",
                               u"く" : u"きません",
                               u"ぐ" : u"ぎません"}
                    ending = endings[verb.kana[-1]]
                elif tense == "past":
                    endings = {u"う" : u"いませんでした",
                               u"つ" : u"ちませんでした",
                               u"る" : u"りませんでした",
                               u"む" : u"みませんでした",
                               u"ぶ" : u"びませんでした",
                               u"ぬ" : u"にませんでした",
                               u"す" : u"しませんでした",
                               u"く" : u"きませんでした",
                               u"ぐ" : u"ぎませんでした"}
                    ending = endings[verb.kana[-1]]
        return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)
    
    elif verb.group == u"i":
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                if tense == "present":
                    return (verb.kanji, verb.kana)
                elif tense == "past":
                    if verb.kana==u"する":
                        return (u"した", u"した")
                    else:
                        return (u"来た", u"きた")
            # Negative
            elif polarity == "negative":
                if tense == "present":
                    if verb.kana==u"する":
                        return (u"しない", u"しない")
                    else:
                        return (u"来ない", u"こない")
                elif tense == "past":
                    if verb.kana==u"する":
                        return (u"しなかった", u"しなかった")
                    else:
                        return (u"来なかった", u"こなかった")

        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
                if tense == "present":
                    if verb.kana==u"する":
                        return (u"します", u"します")
                    else:
                        return (u"きます", u"きます")
                elif tense == "past":
                    if verb.kana==u"する":
                        return (u"しました", u"しました")
                    else:
                        return (u"来ました", u"きました")
            # Negative
            elif polarity == "negative":
                if tense == "present":
                    if verb.kana==u"する":
                        return (u"しません", u"しません")
                    else:
                        return (u"来ません", u"きません")
                elif tense == "past":
                    if verb.kana==u"する":
                        return (u"しませんでした", u"しませんでした")
                    else:
                        return (u"来ませんでした", u"きませでした")
        else:
            return None

def te(verb, speech_level="plain", polarity="positive",tense="present"):
    does_not_exist = []

    if verb in does_not_exist:
        return None
    
    # Ichidan Verbs
    elif verb.group == u"ru":
        ending = u"て"
        return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)
    
    # Godan
    elif verb.group == u"u":
        endings = {u"う" : u"って",
                   u"つ" : u"って",
                   u"る" : u"って",
                   u"む" : u"んで",
                   u"ぶ" : u"んで",
                   u"ぬ" : u"んで",
                   u"す" : u"して",
                   u"く" : u"いて",
                   u"ぐ" : u"いで"}
        ending = endings[verb.kana[-1]]
        if verb.kana == u"いく": ending = u"って"
        return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)
                    
    elif verb.group == u"i":
        if verb.kana== u"する":
            return (u"して", u"して")
        else:
            return (u"来て", u"きて")

def tai(verb, speech_level="plain", polarity="positive",tense="present"):
    does_not_exist = [u"ある", u"いる"]

    if verb.kana in does_not_exist:
        return None
    
    kanji_stem = regular(verb, "polite", "positive", "present")[0][:-2]
    kana_stem = regular(verb, "polite", "positive", "present")[0][:-2]
    
    ending = u""
    # Positive
    if polarity == "positive":
        if tense == "present":
            ending = u"たい"
        elif tense == "past":
            ending  = u"たかった"
    # Negative
    elif polarity == "negative":
        if tense == "present":
            ending = u"たくない"
        elif tense == "past":
            ending = u"たくなかった"
    
    if speech_level == "polite":
        ending += u"です"

    return (kanji_stem + ending, kana_stem + ending)


def tara(verb, speech_level="plain", polarity="positive",tense="present"):
    does_not_exist = []
    if verb.kana in does_not_exist:
        return None

    initial_part = u""
    if polarity == "positive":
        initial_part = regular(verb, "plain", "positive", "past")
        

    elif polarity == "negative":
        initial_part = regular(verb, "plain", "negative", "past")

    return (initial_part[0] + u"ら", initial_part[1] + u"ら")

def ba(verb, speech_level="plain", polarity="positive",tense="present"):
    does_not_exist = []
    if verb.kana in does_not_exist:
        return None

    # Ichidan Verbs and Godan Verbs have the same pattern, as well as the irregular verbs. 
    else:
        all_endings = {u"う" : u"えば",
                       u"つ" : u"てば",
                       u"る" : u"れば",
                       u"む" : u"めば",
                       u"ぶ" : u"べば",
                       u"ぬ" : u"ねば",
                       u"す" : u"せば",
                       u"く" : u"けば",
                       u"ぐ" : u"げば"}

        ending = all_endings[verb.kana[-1]]

    return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)




def volitional(verb, speech_level="plain", polarity="positive",tense="present"):
    ## INCLUDE BOTH MASHOU AND YOU
    does_not_exist = [u"ある", u"いる"]
    if verb.kana in does_not_exist:
        return None
        
    elif verb.group == u"ru":
        if speech_level == "polite":
            ending = u"ましょう"
            return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)


        elif speech_level == "plain":
            ending = u"よう"
            return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)
            
    elif verb.group == u"u":
        if speech_level == "polite":
        
            all_endings = {u"う" : u"いましょう",
                           u"つ" : u"ちましょう",
                           u"る" : u"りましょう",
                           u"む" : u"みましょう",
                           u"ぶ" : u"びましょう",
                           u"ぬ" : u"にましょう",
                           u"す" : u"しましょう",
                           u"く" : u"きましょう",
                           u"ぐ" : u"ぎましょう"}
        
            ending = all_endings[verb.kana[-1]]
        
            return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)

        elif speech_level == "plain":
            
            all_endings = {u"う" : u"おう",
                           u"つ" : u"とう",
                           u"る" : u"ろう",
                           u"む" : u"もう",
                           u"ぶ" : u"ぼう",
                           u"ぬ" : u"のう",
                           u"す" : u"そう",
                           u"く" : u"こう",
                           u"ぐ" : u"ごう"}
        
            ending = all_endings[verb.kana[-1]]
            
            return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)


def get_random_conjugation(verb, aspect_indices, form_indices, plain, polite, pos, neg, past, pres, kana, kanji):
    random.seed()
    information = list()

    information.append(verb.kana)
    information.append(verb.meaning)
    if kanji:
        information[0] = u"%s(%s)" %(verb.kanji, verb.kana)

    information.append("Aspect: ")
    aspect = -1
    while aspect not in aspect_indices:
        aspect = random.randint(0,1000)%5
    if aspect == 0:
        information[2] += "Regular"
    elif aspect == 1:
        verb = verb.potential()
        information[2] += "Potential"
    elif aspect == 2:
        verb = verb.passive()
        information[2] += "Passive"
    elif aspect == 3:
        verb = verb.causative()
        information[2] += "Causative"
    elif aspect == 4:
        verb = verb.causative_passive()
        information[2] += "Causative-passive"

    possible_speech_levels = list()
    if plain:
        possible_speech_levels.append("Plain")
    if polite:
        possible_speech_levels.append("Polite")
    level = random.choice(possible_speech_levels)
    

    possible_polarities = list()
    if pos:
        possible_polarities.append("Positive")
    if neg:
        possible_polarities.append("Negative")
    polarity = random.choice(possible_polarities)

    possible_tenses = list()
    if pres:
        possible_tenses.append("Present")
    if past:
        possible_tenses.append("Past")
    tense = random.choice(possible_tenses)
    
    conjugated = None
    information.append("")
    form = -1
    while form not in form_indices:
        form = random.randint(0,1000)%6

    if form == 0:
        information[3] = "Regular"
        conjugated = regular(verb, level.lower(), polarity.lower(), tense.lower())
    elif form == 1:
        information[3] = "Te form"
        conjugated = te(verb, level.lower(), polarity.lower(), tense.lower())
    elif form == 2:
        information[3] = "Tai form"
        conjugated = tai(verb, level.lower(), polarity.lower(), tense.lower())
    elif form == 3:
        information[3] = "Volitional"
        conjugated = volitional(verb, level.lower(), polarity.lower(), tense.lower())
    elif form == 4:
        information[3] = "Tara"
        conjugated = tara(verb, level.lower(), polarity.lower(), tense.lower())
    elif form == 5:
        information[3] = "Ba"
        conjugated = ba(verb, level.lower(), polarity.lower(), tense.lower())

    information.append(polarity)
    information.append(tense)
    information.append(level)
    information.append(conjugated)

    # Use this to fill in the GUI screen. It will give you Dictionary, 
    return information


    
    
    









