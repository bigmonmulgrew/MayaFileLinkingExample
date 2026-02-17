This repo contains a minimum viable product to show linking up different script files for usage in Maya with python/MEL.

It only outputs messages on sucessfully running each program.
It is a teaching sample only and provides no actual funcationality.

You would usually run from main.py (this is a convention and optional)
- main_simple.py - This is one example of how you could link multiple files
- main_menu.py - A slightly different example allowing running each step discreetly through a menu

### Where to place ##
By defaul Maya will detect scripts in
Documents/maya/\<version\>/scripts

If you are using a different location you can add this to your path with this.
```
import sys
sys.path.append(r"C:\myScripts")
```

### Warning ####
Maya caches modules and wont update them if you make changes. You can force this without restarting by running this, example for step1.py
```
import importlib
import step1
importlib.reload(step1)
```
You will need to do this for any changed files
