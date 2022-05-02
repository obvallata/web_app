from src.lev_space import levenshtein
from src.dogs import DOGS
from src.cats import CATS


def get_close_animals(name):
    min_space_dog = len(name) + 1
    close_dog = ''
    for dog in DOGS:
        new_space = levenshtein(name.lower(), dog.lower())
        if new_space < min_space_dog:
            min_space_dog = new_space
            close_dog = dog
    min_space_cat = len(name) + 1
    close_cat = ''
    for cat in CATS:
        new_space = levenshtein(name.lower(), cat.lower())
        if new_space < min_space_cat:
            min_space_cat = new_space
            close_cat = cat
    return close_dog, min_space_dog, close_cat, min_space_cat
