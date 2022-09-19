import re

special_consonants = "ЦцЧчЖжШшЩщ"
regularize_vowel_after_special_consonant = {
    "ю": "у",
    "я": "а",
    "ы": "и",
    "Ю": "U",
    "Я": "A",
    "Ы": "И",
    # "ё": "о",
    # "Ё": "O",
}

def regularize(word: str) -> str:
    """
    Regularizing orthography a bit to simplify conversion algorithm.

    1. Regularizing soft vowels after 'special' consonants ЦцЧчЖжШшЩщ.
    After these consonants, only vowels УуАаИиЕеЁё are allowed (they are formally always soft).
    For example: жюри -> жури, парашют -> парашут, цыплёнок -> циплёнок.
    But note that ЕеЁё are not touched: шёлк -> шёлк, жена -> жена. (You may change that in conversion table.)

    2. Converting ьо to ьё.

    3. Removing ь after 'special' consonants, for example мышь -> мыш.
    """
    for con in special_consonants:
        for oldvow, newvow in regularize_vowel_after_special_consonant.items():
            word = re.sub(fr"{con}{oldvow}", fr"{con}{newvow}", word)

    word = re.sub(r"[ьъ]о", lambda x: f"{x.group()[0]}ё", word)

    for con in special_consonants:
        word = re.sub(fr"{con}ь", fr"{con}", word)

    return word