import re

from ruslat.conversion_tables import *
from ruslat.cyrillic_ortho_fixer import regularize

def convert_jer_or_jerj_plus_vowel(word: str):
    """
    <ь/ъ V> -> <j V>
    """
    for cyr, lat in softvowel_after_jer_or_jerj.items():
        word = re.sub(fr"[ьъ]{cyr}", fr"{lat}", word)
    
    return word 

def convert_consonant_plus_jerj(word):
    """
    <Cь> -> <Cj>
    """
    for cyr, lat in consonant.items():
        word = re.sub(fr"{cyr}ь", fr"{lat}j", word)
    
    return word 

def convert_consonant_plus_softvowel(word):
    """
    <C я/ю> -> <С ia/iu>

    <C e/ё> -> <С e/ë>

    <Cи> -> <Сi>
    """
    for cyr_vow, lat_vow in softvowel_after_consonant.items():
        for cyr_con, lat_con in consonant.items():
            word = re.sub(fr"{cyr_con}{cyr_vow}", fr"{lat_con}{lat_vow}", word)
    return word 

def convert_softvowels_after_vowels(word):
    """
    <V е/ё/ю/я> -> <V je/jë/ju/ja> (V is either vowel or nothing; jer/jerj are not considered vowels.)
    """
    for cyr, lat in softvowel_after_vowel.items():
        word = re.sub(fr"{cyr}", fr"{lat}", word)
    return word 

def final_convert_hard_consonants(word):
    for cyr_con, lat_con in consonant.items():
        word = re.sub(fr"{cyr_con}", fr"{lat_con}", word)
    return word 

def final_convert_hardvowels(word):
    for cyr_con, lat_con in hardvowel.items():
        word = re.sub(fr"{cyr_con}", fr"{lat_con}", word)
    return word

def latinizator(sentense):
    def conv_with_checking_case(conv, word):
        if (was_title := word == word.title()) or (was_upper := word == word.upper()):
            word = word.lower()
        return conv(word).title() if was_title else (conv(word).upper() if was_upper else conv(word))

    for conv in (
        regularize, 
        convert_jer_or_jerj_plus_vowel,
        convert_consonant_plus_jerj,
        convert_consonant_plus_softvowel,
        convert_softvowels_after_vowels,
        final_convert_hard_consonants,
        final_convert_hardvowels):
        sentense = re.sub(r"[^\s]+", lambda m: conv_with_checking_case(conv, m.group(0)), sentense)
    
    # assert all(cyr not in word for cyr in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    return sentense