# -*- coding: utf-8 -*-
import random

"""All the conjugation methods you could ever want. Returns tuples of (kanji, kana)"""

def get_stem(verb):
    kanji_stem = u""
    kana_stem = u""

    if verb.group == u"ru":
        kanji_stem = verb.kanji[:-1]
        kana_stem = verb.kana[:-1]           
    
    elif verb.group == u"u":
        endings = {u"う" : u"い",
                   u"つ" : u"ち",
                   u"る" : u"り",
                   u"む" : u"み",
                   u"ぶ" : u"び",
                   u"ぬ" : u"に",
                   u"す" : u"し",
                   u"く" : u"き",
                   u"ぐ" : u"ぎ"}
        kanji_stem = verb.kanji[:-1]+endings[verb.kana[-1]]
        kana_stem = verb.kana[:-1]+endings[verb.kana[-1]]

    if verb.group == u"i":
        if verb.kana[-2:]==u"する":
            kanji_stem, kana_stem = (u"し", u"し")
        else:
            kanji_stem, kana_stem = (u"来", u"き")
    return (kanji_stem, kana_stem)

def non_past(verb, speech_level="plain", polarity="positive",tense="present"):
    if tense == "past":
        return past(verb,speech_level, polarity, tense)
    beginning_kanji = verb.kanji[:-1]
    beginning_kana = verb.kana[:-1]
    ending = ""

    does_not_exist = []

    if verb in does_not_exist:
        return None

    # Ichidan Verbs
    elif verb.group == u"ru":
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                ending = u"る"
            # Negative
            elif polarity == "negative":
                ending = u"ない"
            
        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
                ending =  u"ます"

            # Negative
            elif polarity == "negative":
                ending = u"ません"

        ending_kanji = ending
        ending_kana = ending
    # Godan
    elif verb.group == u"u":
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                ending = verb.kana[-1]

            # Negative
            elif polarity == "negative":
                if verb.kana[-2:] == u"ある":
                    return(verb.kanji[:-2]+u"ない",verb.kana[:-2]+u"ない")
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
      
        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
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

            # Negative
            elif polarity == "negative":
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
        ending_kanji = ending
        ending_kana = ending

    elif verb.group == u"i":
        beginning_kanji = verb.kanji[:-2]
        beginning_kana = verb.kana[:-2]
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                return (verb.kanji, verb.kana[-2:])
            # Negative
            elif polarity == "negative":
                if verb.kana[-2:]==u"する":
                    ending_kanji, ending_kana = (u"しない", u"しない")
                else:
                    ending_kanji, ending_kana = (u"来ない", u"こない")
        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
                if verb.kana[-2:]==u"する":
                    ending_kanji, ending_kana = (u"します", u"します")
                else:
                    ending_kanji, ending_kana = (u"きます", u"きます")
            # Negative
            elif polarity == "negative":
                if verb.kana[-2:]==u"する":
                    ending_kanji, ending_kana = (u"しません", u"しません")
                else:
                    ending_kanji, ending_kana = (u"来ません", u"きません")

    return (beginning_kanji + ending_kanji, beginning_kana + ending_kana)

def past(verb, speech_level="plain", polarity="positive",tense="past"):
    if tense == "present":
        return non_past(verb, speech_level, polarity, tense)
    beginning_kanji = verb.kanji[:-1]
    beginning_kanji = verb.kanji[:-1]
    beginning_kana = verb.kana[:-1]
    ending = ""

    does_not_exist = []

    if verb in does_not_exist:
        return None

    # Ichidan Verbs
    elif verb.group == u"ru":
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                ending = u"た"
            # Negative
            elif polarity == "negative":
                ending = u"なかった"
            
        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
                ending = u"ました"
            # Negative
            elif polarity == "negative":
                ending = u"ませんでした"
        ending_kanji = ending
        ending_kana = ending

    # Godan
    elif verb.group == u"u":
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
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
                if verb.kana[-2:] == u"いく": ending = u"った"
                    
            # Negative
            elif polarity == "negative":
                if verb.kana[-2:] == u"ある":
                    return(verb.kanji[:-2]+u"なかった",verb.kana[:-2]+u"なかった")
                endings = {u"う" : u"わなかった",
                           u"つ" : u"たなかった",
                           u"る" : u"らなかった",
                           u"む" : u"まなかった",
                           u"ぶ" : u"ばなかった",
                           u"ぬ" : u"ななかった",
                           u"す" : u"さなかった",
                           u"く" : u"かなかった",
                           u"ぐ" : u"がなかった"}
                ending = endings[verb.kana[-1]]
      
        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
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
        ending_kanji = ending
        ending_kana = ending

    elif verb.group == u"i":
        beginning_kanji = verb.kanji[:-2]
        beginning_kana = verb.kana[:-2]
        # Plain/Short Forms
        if speech_level == "plain":
            # Positive
            if polarity == "positive":
                if verb.kana[-2:]==u"する":
                    ending_kanji, ending_kana = (u"した",u"した")
                else:
                    ending_kanji, ending_kana = (u"来た", u"きた")
            # Negative
            elif polarity == "negative":
                if verb.kana[-2:]==u"する":
                    ending_kanji, ending_kana = (u"しなかった", u"しなかった")
                else:
                    ending_kanji, ending_kana = (u"来なかった", u"こなかった")
        # Polite/Long forms
        elif speech_level == "polite":
            # Positive
            if polarity == "positive":
                if verb.kana[-2:]==u"する":
                    ending_kanji, ending_kana = (u"しました", u"しました")
                else:
                    ending_kanji, ending_kana = (u"来ました", u"きました")
            # Negative
            elif polarity == "negative":
                if verb.kana[-2:]==u"する":
                    ending_kanji, ending_kana = (u"しませんでした", u"しませんでした")
                else:
                    ending_kanji, ending_kana = (u"来ませんでした", u"きませでした")

    return (beginning_kanji + ending_kanji, beginning_kana + ending_kana)
    
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
        if verb.kana[-2:] == u"する":
             return (verb.kanji[:-2] + u"して", verb.kana[:-2] + u"して")
        else:
            return (verb.kanji[:-2] + u"来て", verb.kana[:-2] + u"きて")

def tai(verb, speech_level="plain", polarity="positive",tense="present"):
    does_not_exist = [u"ある", u"あめがふる"]

    if verb.dictionary_form_kana[-2:] in does_not_exist or verb.dictionary_form_kana in does_not_exist:
        return None    

    kanji_stem, kana_stem = get_stem(verb)
    
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
    if verb.dictionary_form_kana in does_not_exist:
        return None

    initial_part = u""
    if polarity == "positive":
        initial_part = past(verb, "plain", "positive", "past")
        

    elif polarity == "negative":
        initial_part = past(verb, "plain", "negative", "past")

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
    does_not_exist = [u"ある", u"いる"]
    if verb.dictionary_form_kana[-2:] in does_not_exist:
        return None
        
    elif verb.group == u"ru":
        if speech_level == "polite":
            ending = u"ましょう"
            kanji_stem, kana_stem = get_stem(verb)
            return (kanji_stem + ending, kana_stem + ending)

        elif speech_level == "plain":
            ending = u"よう"
            return (verb.kanji[:-1] + ending, verb.kana[:-1] + ending)
            
    elif verb.group == u"u":
        if speech_level == "polite":
            ending = u"ましょう"
            kanji_stem, kana_stem = get_stem(verb)
            return (kanji_stem + ending, kana_stem + ending)

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
    elif verb.group == u"i":
        if speech_level == "polite":
            ending = u"ましょう"
            kanji_stem, kana_stem = get_stem(verb)
            return (kanji_stem + ending, kana_stem + ending)

        elif speech_level == "plain":
            if verb.kana[-2:] == u"する":
                return (verb.kanji[:-2] + u"しよう", verb.kana[:-2] + u"しよう")
            else:
                return (verb.kanji[:-2] + u"来よう", verb.kana[:-2] + u"こよう")

global all_forms, form_names, all_aspects
all_forms = list([non_past, past,te,tai,tara,ba])   
form_names = list([u"Non-past or Past", u"Non-past or Past",u"～て form",u"～たい form",u"～たら conditional",u"～ば conditional"])      
all_aspects = list(["Regular","Potential","Passive","Causative","Causative-passive"])


def get_random_conjugation(verb, aspect_indices, form_indices, plain, polite, pos, neg, past, pres, kana, kanji):
    random.seed()
    information = list()

    information.append(verb.kana)
    information.append(verb.meaning)
    if kanji:
        information[0] = u"%s(%s)" %(verb.kanji, verb.kana)

    information.append("Aspect: ")
    aspect = random.choice(aspect_indices)
    information[2] += all_aspects[aspect]
    try:
        if aspect == 0:
            verb = verb
        elif aspect == 1: 
            verb = verb.potential()
        elif aspect == 2:
            verb = verb.passive()
        elif aspect == 3:
            verb = verb.causative()
        elif aspect == 4:
            verb = verb.causative_passive()
    except AttributeError:
        return None

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
    
    try:
        information.append("")
        form_index = random.choice(form_indices)
        information[3] += form_names[form_index]
        conjugated = all_forms[form_index](verb, level.lower(), polarity.lower(), tense.lower())
    except AttributeError:
        return None
    except TypeError:
        return None

    information.append(polarity)
    information.append(tense)
    information.append(level)
    information.append(conjugated)

    # Use this to fill in the GUI screen. It will give you Dictionary, 
    return information


    
    
    









