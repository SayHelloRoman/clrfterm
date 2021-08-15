<h1 align="center" style="font-size: 60px;">clrfterm</h1>
<p align="center" style="font-size: 20px;font-style: oblique;">Module that decorates your console</p>

---
* [Source code](https://github.com/SayHelloRoman/clrfterm)
---
## Description
clrfterm makes it easy to work with ANSI escape sequences that decorate your console.
ANSI escape sequences are a standard for in-band signaling to control cursor location, color, font styling, and other options on video text terminals and terminal emulators. Certain sequences of bytes, most starting with an ASCII escape character and a bracket character, are embedded into text. The terminal interprets these sequences as commands, rather than text to display verbatim.
## Installation
* Tested on CPython 3.7, 3.8 and 3.9
* No requirements other than the standard library.
```
pip install clrfterm
```
## Usage
##### Colored Output
```python
from clrflterm import (
    Styles,
    Foreground,
    Backgrounds,
    rprint,
    reset,
)


print(Foreground.RED + "Red foreground text")
print(Backgrounds.WHITE + "White backgrounds text")
print(Styles.UNDERLINE + "Underlined text")
reset()
print("Back to normal text")

rprint("Auto reset", foreground=Foreground.GREEN)
print("Normal text")
```
##### Available formatting constants are:
```
Foregrounds: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE.
Backgrounds: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE.
Styles: BOLD, UNDERLINE, RESET
```

reset the function resets the foreground, background. It must be called upon exiting the program.
## License
This module  is licensed under the terms of the MIT license.