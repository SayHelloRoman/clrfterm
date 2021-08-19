<h1 align="center" style="font-size: 60px;">clrfterm</h1>
<p align="center" style="font-size: 20px;font-style: oblique;">Module that decorates your console</p>

---
* [Source code](https://github.com/SayHelloRoman/clrfterm)
---
## Description
clrfterm makes it easy to work with ANSI escape sequences that decorate your console.
ANSI escape sequences are a standard for in-band signaling to control cursor location, color, font styling, and other options on video text terminals and terminal emulators. Certain sequences of bytes, most starting with an ASCII escape character and a bracket character, are embedded into text. The terminal interprets these sequences as commands, rather than text to display verbatim.
## Installation
* Tested on CPython 3.7, 3.8, 3.9 and PyPy 3.7.10
* No requirements other than the standard library.
```
pip install clrfterm
```
## Usage
##### Colored Output
```python
from clrflterm import (
    Style,
    Foreground,
    Background,
    rprint,
    reset,
)


print(Foreground.RED + "Red foreground text")
print(Background.WHITE + "White backgrounds text")
print(Style.UNDERLINE + "Underlined text")
reset()
print("Back to normal text")

rprint("Auto reset", foreground=Foreground.GREEN)
print("Normal text")
```
##### Available formatting constants are:
```
Foreground: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE.
Background: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE.
Style: BOLD, UNDERLINE, RESET
```
reset the function resets the foreground, background. It must be called upon exiting the program.

#### Fluent interface
In software engineering, a fluent interface is an object-oriented API whose design relies extensively on method chaining.

clrfterm has a Message, Phrase, PhraseStyle classes that implements the Fluent interface
```python
from clrfterm import Foreground, Background, Style
from clrfterm.messages import Message, Phrase, PhraseStyle

style = (
    PhraseStyle()
        .set_foreground(Foreground.RED)
        .set_background(Background.CYAN)
        .set_style(Style.BOLD)
)
print(Message()
    .add(Phrase()
        .set_text('hello')
        .set_style(style))
    .add(Phrase()
        .set_text('world')
        .set_style(style))
)
```
## Windows

The [Windows Console](https://en.wikipedia.org/wiki/Windows_Console) did not support ANSI escape sequences, nor did Microsoft provide any method to enable them.
But In 2016, Microsoft released the Windows 10 version 1511 update which unexpectedly implemented support for ANSI escape sequences, over two decades after the debut of Windows NT.

clrfterm can enable ANSI escape sequences in CMD.

```python
from clrflterm import (
    enable_ansi,
    Foreground,
    reset,
)


enable_ansi()
print(Foreground.RED + "Hello")
reset()
```

## License
This module  is licensed under the terms of the MIT license.
Name by @xterdd