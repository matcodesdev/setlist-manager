# Setlist Manager

**Setlist Manager** is a lightweight tool for musicians and bands to manage songs and setlists. Initially built in Python, this project is structured for future expansion into a full-featured desktop or web application.

---

## Features (v0.1.2)

- Add and store song data including title, artist, album, key, and tuning
- View a working setlist that displays all added songs
- Add new setlists with name, venue, and date
- Store song and setlist entries as dictionaries (preparing for future data storage)
- Clean modular codebase using custom classes and functions
- Clear separation between functionality and data models
- Structured foundation for future features like assigning songs to setlists and event tracking

---

## How to Use

This version runs locally and allows users to:
- Add new songs with structured details
- View the current list of songs (titles and artists only)
- Add new setlists including name, venue, and date

More functionality is in development, including setlist management, song assignments, and data export.

---

## File Structure

```plaintext
├── main.py           # Handles user interaction and menu flow
├── addsongs.py       # Contains the Song class and song creation logic
├── addsetlists.py    # Contains the Setlist class and setlist creation logic
├── version.py        # Stores the version number
├── README.md         # Project documentation
