# Classes

Given a class:

    class Foo(object):
        """Documentation for Foo"""
        def __init__(self, **kwargs):
            super(Foo, self).__init__()
            self.kwargs = kwargs
            self.bar = kwargs['bar']
            self.foo = None


## Create an object of class Foo:

    foo = Foo()

## Pass arguments to the initialisation using kwargs:

    foo = Foo(bar="bar")

## Set a field after initialization

    foo.some_field = "buzz"


# Dictionaries

## Create a dictionary

    some_dict = {'00:01': 1,
                 '00:02': 2}

## Get a value from a dictionary

    some_dict['00:01'] # => 1
    some_dict['00:02'] # => 2
    some_dict['foo'] # => Exception


# Lists

## Append to a list

    some_list = []
    some_list.append('bar')  # => some_list = ['bar']
