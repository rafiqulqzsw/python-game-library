Game library built within python which allows you to view, add, find, and remove games while storing their ratings in a dictionary

**Features**
- Show all games and their ratings
- add new games
- find games and view their ratings
- remove games
- rate games from 0-10
- prevent duplicates
- input validation for invalid ratings and menu choices
- runs continuously until user chooses to quit

**What i practised**
- dictionaries
- functions
- while and for loops
- try / except
- return values
- None
- dictionary methods such as .items()
- basic program structure and organisation

**V2 Updates**
- added file-based data persistence
- games are loaded from a file when the program starts
- game data is saved back to the file when changes are made
- added the ability to edit game ratings
- maintained rating validation (1-10)
- data is preserved between sessions

**V2 Concepts learned**
- file I/O
- reading and writing files
- file -> dictionary / dictionary -> file
- data persistence

**V3 Updates**
- split the application into separate modules
- separated game logic, file storage and input validation
- structured application around main() function
- added if __name__ == "__main__" as the program entry point

**V3 structure**
- main.py controls the main program and menu
- games.py contains / handles game operation
- storage.py loads and saves data
- validation.py handles input validation
- test2.txt stores saved game data

**V3 concepts learned**
- utilizing modules to organise a project into separate components
- work with file paths using os.path 
