class Song: #class to store info of new songs
    def __init__ (self, title, artist, album, key, tuning):
        self.title = title
        self.artist = artist
        self.album = album
        self.key = key
        self.tuning = tuning

    def to_dict(self): #converts song info to a k, v pair
        return {
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'key': self.key,
            'tuning': self.tuning
        }

    def __str__(self): #prints full song info when {new} is called
        return (f'''
New Song Added!
Song Title: {self.title}
Artist: {self.artist}
Album: {self.album}
Key: {self.key}
Tuning: {self.tuning}
''')
    
def add_new_song(): # asks user for info on song they're adding
    title = input('Please enter the song title: ').title().strip()
    artist = input('Please enter the artist name: ').title().strip()
    album = input('Please enter the album name: ').title().strip()
    key = input('Please enter the key of the song: ').capitalize().strip() #capitlize only in case key is X#m (minor)
    tuning = input('Please enter the tuning used for the song: ').title().strip()
    return Song(title, artist, album, key, tuning)
