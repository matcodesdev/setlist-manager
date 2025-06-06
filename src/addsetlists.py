class Setlist: #unsued at the moment, will need it's own module
    def __init__ (self, name, venue, date):
        self.name = name
        self.venue = venue
        self.date = date

    def to_dict(self):
        return {
            'setlist name': self.name,
            'setlist venue': self.venue,
            'setlist date': self.date
        }

    def __str__(self): #prints full setlist info when {new_set} is called
        return (f'''
New Setlist Added!
Setlist Name: {self.name}
Venue Name: {self.venue}
Show Date: {self.date}       
''')


def add_new_setlist(): #asks user for input on new setlist info
    name = input('Please enter setlist name: ').title().strip()
    venue = input('Please enter venue name: ').title().strip()
    date = input('Please enter show date (DD/MM/YYYY): ').title().strip()
    return Setlist(name, venue, date)