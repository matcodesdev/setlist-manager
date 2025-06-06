from version import __version__
from addsongs import Song, add_new_song
from addsetlists import Setlist, add_new_setlist

songs = []
setlists = []

def main():
    print(f'Setlist Manager version v{__version__}')
    user_input() #starts menu loop and asks for user input

def user_input():
    while True: #this needs to be moved to its own module
        print('''
              Main Menu
    (new setlist/add song/view setlist)
              ''')
        user_input = input('Choose one of the menu options: ').lower()
        if user_input == 'add song':
            new_song = add_new_song()
            songs.append(new_song.to_dict()) 
            print(f'\n{new_song}') #prints full song info
        elif user_input == 'view setlist': #views 'default setlist, need to add function/class to choose from setlists.
            print('\nSetlist Tracks:')
            for song in songs:
                print(f"- {song['title']} by {song['artist']}")
        elif user_input == 'new setlist':
            new_setlist = add_new_setlist()
            setlists.append(new_setlist.to_dict())
            print(f'\n{new_setlist}') #prints full setlist info
        elif user_input == 'delete song':
            pass
            #choose song to delete
            #ask if sure
            #delete from list
        elif user_input == 'delete setlist':
            pass
            #choose setlist to delete
            #ask if sure
            #delete from list
        else:
            print('Please choose a valid input')

if __name__ == '__main__':
    main()