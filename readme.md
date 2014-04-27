# Natural language Calculator

Natural Language Calculator is a program for Python 3 that takes string
input that includes either digits or alphabetic words of numbers,
evaluates that input as an expression, and prints out the result of
that evaluation. The program accepts alphabetic words up to a
trillion. As an example, entering

`two million three hundred forty thousand and twenty eight - seven thousand`

will print out
```bash
Parsed your input as 2340028-7000
This evaluates to 2333028
```

You can also mix numbers represented by alphabetic characters and digits

`2 thousand 20 two`

The program ignores spaces and the string "and" for non-digit tokens, so feel free to use or
ignore them based on your aesthetic preferences. The program also maps
the following words to their appropriate operator: `plus`, `minus`,
`divide`, `multiply`, `mod/modulus`, `point/dot`, `negative`. Do not use the
`-` character to hyphenate numbers, as it will be interpreted as a minus sign.

Note that the program does not check your input to determine if it makes any
sense. Rather than raise an error, nonsensical input will likely result
in nonsensical output.
