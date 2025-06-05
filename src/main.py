from version import __version__
from addsongs import Song, new_song

songs = []

def main():
    print(f'Setlist Manager version v{__version__}')
    user_input() #starts menu loop and asks for user input

def user_input():
    while True:
        print('''
              Main Menu
    (new setlist/add song/view setlist)
              ''')
        user_input = input('Choose one of the menu options: ').lower()
        if user_input == 'add song':
            new = new_song()
            songs.append(new.to_dict()) 
            print(f'\n{new}') #prints full song info
        elif user_input == 'view setlist':
            print('\nSetlist Tracks:')
            for song in songs:
                print(f"- {song['title']} by {song['artist']}")
        elif user_input == 'new setlist':
            pass
        else:
            print('Please choose a valid input')

class Setlist: #unsued at the moment, will need it's own module
    def __init__ (self, name, venue, date):
        self.name = name
        self.venue = venue
        self.date = date

if __name__ == '__main__':
    main()