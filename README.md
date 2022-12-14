# capitalise-delimit

A python library to capitalise words in a string based on a list of given delimiters. This is quite a niche solution but
is useful when capitalising proper nouns that contain multiple different delimiting characters. An example might be
double barreled names, e.g. where `jim-bob joe` needs to become `Jim-Bob Joe`

PyPI build can be found [here](https://pypi.org/project/capitalise-delimit/).

## Installation

Install this library using
```
pip install capitalise-delimit
```

or via PyPI, which is linked above.

## Get started

To use the library, simply import and create an instance of the `CapitaliseDelimit` object, which can be used to access
this library's functionality. You will need to instantiate this class with a list of delimiters that strings using this
class will be split by when being capitalised. Currently, the only supported functionality is the `capitalise` function.

```python
>>> from capitalise_delimit import CapitaliseDelimit
>>> my_str = 'a sample string'
>>> capitalise_space = CapitaliseDelimit([' '])
>>> capitalise_space.capitalise(my_str)
'A Sample String'
```

Another example:

```python
>>> name = 'jim-bob joe'
>>> CD_space_hyphen = CapitaliseDelimit([' ', '-'])
>>> CD_space_hyphen.capitalise(name)
'Jim-Bob Joe'
```

### Ignore syncategorematic words

The library provides a defined list of words that can be ignored when capitalising the string. The current list of words
is:
> * upon
>* at
>* the
>* on
>* in

These words are useful mostly when capitalising place names, such as _Stratford-upon-Avon_. Capitalising this normally
would look like

```python
>>> capitalise_hyphen = CapitaliseDelimit(['-'])
>>> capitalise_hyphen.capitalise('stratford-upon-avon')
'Stratford-Upon-Avon'
```

However, if we don't want 'upon' to be capitalised, we can supply `True` as the `ignore_words` named parameter

```python
>>> capitalise_hyphen.capitalise('stratford-upon-avon', ignore_words=True)
'Stratford-upon-Avon'
```

If the predefined list of words does not fully suit your needs, you can add a custom list of words using
the `custom_ignore_words` parameter. Note that this can be used on its own to define a purely custom list, or in
conjunction with `ignore_words` if you simply want to add some extra words on top of the existing list.

Please also note that when passing a custom list of words, this is saved and used for future capitalisations called on
that instance. The custom list must therefore be kept attention of, and can be updated upon every call of 
`capitalise()`. To reset the custom list, simply pass in an empty list or set when you next call `.capitalise()`. The 
value provided for `ignore_words` is also remembered, so if you supply the value `True` when invoking `.capitalise()`, 
all following capitalisation using the same class instance will run with `ignore_words=True` until it is manually 
set back to `False`.

## Footnote

This is my first publicly available python package, so please forgive any na??ve mistakes. In fact, if you can be
bothered taking the time to let me know, I am more than happy to take on any constructive criticism.

I do plan on adding features once I think of some that may be relevant. Any feature suggestions are more than welcome.

Thanks for checking out my package :)