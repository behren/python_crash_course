def make_album(artist_name, album_title, tracks=0):

    album = {
        'Artist': artist_name, 
        'Title': album_title
        }

    if tracks:
        album['Number of songs']=tracks
    
    return(album)

album_name = make_album('Bob Marley', 'Exodus')
print(album_name)

album_name = make_album('Trettmann', 'DIY')
print(album_name)

album_name = make_album('EMINEM', 'The Marshall Mathers LP', 12)
print(album_name)