import wikipedia
import wikiquote
from wikiquote.utils import DisambiguationPageException
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import keys
import flickrapi
import urllib.request

api_key = keys.api_key()
api_secret = keys.api_secret()


def get_quote_list(title):
    chosen = False

    while not chosen:
        try:
            quote_list = wikiquote.quotes(random.choice(title), 1)
            chosen = True
        except DisambiguationPageException:
            pass

    return quote_list


def get_band_name():
    return random.choice(wikipedia.random(5))


def get_album_name():
    title = wikiquote.random_titles(max_titles=5, lang='en')

    quote_list = get_quote_list(title)
    chosen = False

    while not chosen:
        try:
            quote = random.choice(quote_list).split()
            chosen = True
        except IndexError:
            quote_list = get_quote_list(title)

    quote_position = random.randint(0, len(quote))

    if quote_position + 5 <= len(quote):
        quote_size = random.randint(quote_position, quote_position+5)
    else:
        quote_size = random.randint(quote_position, len(quote))

    quote_string = ""

    if quote_position == quote_size:
        quote_position = quote_size - 1

    for i in range(quote_position, quote_size):
        quote_string += quote[i]
        quote_string += " "

    return quote_string.title()


def draw_album(album, band):
    img = Image.open("sample.jpg")
    draw = ImageDraw.Draw(img)
    font_album = ImageFont.truetype("OpenSans-Light.ttf", 34)
    font_band = ImageFont.truetype("OpenSans-Light.ttf", 20)
    draw.text((5, 0), band, (255, 255, 255), font=font_band)
    draw.text((5, 25), album, (255, 255, 255), font=font_album)
    img.save('sample-out.jpg')


def download_file():
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    photo = flickr.photos.getRecent()['photos']['photo'][4]
    farm_id = photo['farm']
    server = photo['server']
    photo_id = photo['id']
    secret = photo['secret']
    url = 'https://farm{}.staticflickr.com/{}/{}_{}_z.jpg'.format(farm_id, server, photo_id, secret)
    urllib.request.urlretrieve(url, "sample.jpg")


