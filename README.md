# Setlist Manager

A lightweight tool for musicians and bands to manage songs and setlists. Initially built in Python, this project is structured for future expansion into a full-featured desktop or web application.

---

## Features (v0.1.1)
- Add and store song data including title, artist, album, key, and tuning
- View a working setlist that displays all added songs
- Store song entries as dictionaries (preparing for future data storage features)
- Clean modular codebase using custom classes and functions
- Clear separation between core functionality and data models
- Placeholder structure for setlist creation and event tracking

---

## How to Use

This version runs locally and allows users to:
- Add new songs with structured details
- View current song list (titles and artists)

More functionality is in development, including setlist creation, event planning, and data export.

---

## File Structure

```plaintext
├── main.py         # Handles user interaction and menu flow
├── addsongs.py     # Contains the Song class and song creation logic
├── version.py      # Stores the version number
├── README.md       # Project documentation
