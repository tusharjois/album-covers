import albumcovers

album = albumcovers.get_album_name()
band = albumcovers.get_band_name()

print(album)
print(band)

albumcovers.download_file()
albumcovers.draw_album(album, band)
