import re
import regex
from typing import Callable

from ruslat.conversion_tables import *
from ruslat.cyrillic_ortho_fixer import regularize

def convert_jer_or_jerj_plus_vowel(word: str) -> str:
    """
    <ь/ъ V> -> <j V>
    """
    for cyr, lat in softvowel_after_jer_or_jerj.items():
        word = re.sub(fr"[ьъ]{cyr}", f"{lat}", word)

    return word 

def convert_consonant_plus_jerj(word: str) -> str:
    """
    <Cь> -> <Cj>
    """
    j = consonant_palatalization_symbol_not_before_vowel
    for cyr, lat in consonant.items():
        
        word = re.sub(f"{cyr}ь", f"{lat}{j}", word)
    
    return word

def convert_consonant_plus_softvowel(word: str) -> str:
    """
    <C я/ю> -> <С ia/iu>

    <C e/ё> -> <С e/ë>

    <Cи> -> <Сi>
    """
    for cyr_vow, lat_vow in softvowel_after_consonant.items():
        for cyr_con, lat_con in consonant.items():
            word = re.sub(f"{cyr_con}{cyr_vow}", f"{lat_con}{lat_vow}", word)
    return word

def convert_softvowels_after_vowels(word: str) -> str:
    """
    <V е/ё/ю/я> -> <V je/jë/ju/ja> (V is either vowel or nothing; jer/jerj are not considered vowels.)
    """
    for cyr, lat in softvowel_after_vowel.items():
        word = re.sub(cyr, lat, word)
    return word

def final_convert_hard_consonants(word: str) -> str:
    for cyr_con, lat_con in consonant.items():
        word = re.sub(cyr_con, lat_con, word)
    return word 

def final_convert_hardvowels(word: str) -> str: 
    for cyr_con, lat_con in hardvowel.items():
        word = re.sub(cyr_con, lat_con, word)
    return word

def conv_with_checking_case(conv: Callable[[str], str], word: str) -> str:
    if word.istitle():
        return conv(word.lower()).title()
    if word.isupper():
        return conv(word.lower()).upper()
    else:
        return conv(word)

def latinizator(sentense: str) -> str:
    for conv in (regularize, 
                 convert_jer_or_jerj_plus_vowel,
                 convert_consonant_plus_jerj,
                 convert_consonant_plus_softvowel,
                 convert_softvowels_after_vowels,
                 final_convert_hard_consonants,
                 final_convert_hardvowels):
        sentense = regex.sub(r"\p{L}+", lambda m: conv_with_checking_case(conv, m.group(0)), sentense)
    
    # assert all(cyr not in sentense for cyr in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    return sentense