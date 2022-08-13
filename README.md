# capitalise-delimit
A python library to capitalise words in a string based on a list of given delimiters

## Installation

## Get started
To use the library, simply import and create an instance of the `CapitaliseDelimit` object, which can be used to access this library's functionality. You will need to instantiate this class with a list of delimiters that strings using this class will be split by when being capitalised. Currently, the only supported functionality is the `capitalise` function.
```python
>>> from capitalise_delimit import CapitaliseDelimit

>>> my_str = 'a sample string'
>>> capitalise_space = CapitaliseDelimit([' '])
>>> capitalise_space.capitalise(my_str)
'A Sample String'
```

### Ignore syncategorematic words

The library provides a defined list of words that can be ignored when capitalising the string. The current list of words is:
>* upon
>* at
>* the
>* on
>* in

These words are useful mostly when capitalising place names, such as _Stratford-upon-Avon_. Capitalising this normally would look like
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
If the predefined list of words does not fully suit your needs, you can add a custom list of words using the `custom_ignore_words` parameter. Note that this can be used on its own to define a purely custom list, or in conjunction with `ignore_words` if you simply want to add some extra words on top of the existing list.

Please also note that when passing a custom list of words, this is saved and used for future capitalisations called on that instance. The custom list must therefore be kept attention of, and can be updated upon every call of `.capitalise`. To reset the custom list, simply pass in an empty list or set when you next call `.capitalise`.