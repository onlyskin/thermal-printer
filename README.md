Python (2.7) script for printing to a CSN-A2 thermal printer over UART, including printing
Kanji from Unicode string literals.

The printer is stateful, meaning that if you use the function `set_big_chars`, it will always print large size until you use `unset_big_chars`.

