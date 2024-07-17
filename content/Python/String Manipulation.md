---
title: String Manipulation
---
### How to Concatenate Strings

You can use the `+` operator to concatenate strings.

```
word1 = 'Deepak '

word2 = 'Nishad'

print(word1 + word2)
```

```
New York
```

### How to Replace Part of a String

The `replace()` method replaces a part of the string with another

```
str1 = 'Deepak Nishad'.replace('Nishad', 'Singh')
```

```
Deepak Singh
```

### How to Count

Specify what to count as an argument.

In this case, we are counting how many spaces exist in "Rio de Janeiro", which is 2.

```
word = "Rio de Janeiro"

print(word.count(' '))
```

```
2
```

## How to Split a String in Python

Splitting a string into smaller parts is a very common task. To do so, we use the `split()` method in Python.

#### Example 1: use whitespaces as delimiters

In this example, we split the phrase by whitespaces creating a list named **my_words** with five items corresponding to each word in the phrase.

```
my_phrase = "let's go to the beach"

my_words = my_phrase.split(" ")

for word in my_words:

	print(word)

print(my_words)
```

## How to Remove All White Spaces in a String in Python

Notice that the `\s` represents not only space `' '`, but also form feed `\f`, line feed `\n`, carriage return `\r`, tab `\t`, and vertical tab `\v`.

In summary, `\s = [ \f\n\r\t\v]`.

The `+` symbol is called a quantifier and is read as 'one or more'. This means that it will consider, in this case, one or more white spaces since it is positioned right after the `\s`.

```
import re

txt = "The rain in Spain"

no_space = re.sub(r"\s", "", txt)

print(no_space)
```

```
TheraininSpain
```

## How to Handle Multiline Strings in Python

### Triple Quotes

To handle multiline strings in Python you use triple quotes, either single or double.

This first example uses double quotes.

```
long_text = """This is a multiline,

a long string with lots of text,

I'm wrapping it in triple quotes to make it work."""

print(long_text)

#output:
#This is a multiline,
#
#a long string with lots of text,
#
#I'm wrapping it in triple quotes to make it work.

```

Now the same as before, but with single quotes:

```
long_text = '''This is a multiline,

a long string with lots of text,

I'm wrapping it in triple quotes to make it work.'''

print(long_text)
#output:
#This is a multiline,
#
#a long string with lots of text,
#
#I'm wrapping it in triple quotes to make it work.
```