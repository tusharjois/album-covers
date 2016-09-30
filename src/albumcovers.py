import wikipedia
import wikiquote
import random


def get_band_name():
    return wikipedia.random(1)


def get_album_name():
    title = wikiquote.random_titles(max_titles=1)
    quotes = wikiquote.quotes(title[0], 1)
    return random.choice(quotes)