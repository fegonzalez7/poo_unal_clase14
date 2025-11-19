
# * An iterator is... an object! How rare, right?
# * An iterator is supposed to go through a collection of elements, do something for every one of them (or at least do something in every iteration, i.e., every time next() is called), and track which elements it has already iterated through.
# * In the class of an iterator, two methods are defined, next() and iter(), define in the classes as, respectively, __next__ and __iter__.

# * The __iter__ method usually returns self, since the objects of the class are iterators
# * The __next__ method defines what will the object return in every iteration

# * An iterator usually holds a reference that points to a collection of data so it can access only the necessary 'chunk', portion or element of the collection needed in every iteration.

# * Every time an iterable is going to be iterated over, an iterator object of the iterable is created. For example, a for loop has the base syntax `for item in collection:`. This in reality means that a collection iterator object is created, and item is the value returned by iterator.__next__() in each iteration.

# * Note: Lists, tuples, dictionaries and sets are called iterables precisely because an associated iterator can iterate over1 them.