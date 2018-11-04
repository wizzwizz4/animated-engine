__all__ = ['SignedList']

class SignedList:
    __slots__ = "_neg", "_nonneg"
    
    def __add__(self, other):
        return self._neg[::-1] + self._nonneg + other

    def __contains__(self, other):
        return other in self._neg or other in self._nonneg

    def __delitem__(self, index):
        if index < 0:
            del self._neg[~index]
        else:
            del self._nonneg[index]

    def __eq__(self, other):
        if isinstance(other, SignedList):
            return (self._neg == other._neg
                    and self._nonneg == other._nonneg)
        if isinstance(other, list):
            return not self._neg and self._nonneg == other
        for i in range(-len(self._neg), len(self._nonneg)):
            try:
                if self[i] != other[i]:
                    return False
            except IndexError:
                return False
        return True

    def __getitem__(self, index):
        if index < 0:
            return self._neg[~index]
        return self._nonneg[index]

    def __iadd__(self, other):
        self._nonneg += other

    def __init__(self, iterable=None):
        self._neg = []
        if iterable is None:
            self._nonneg = []
        else:
            self._nonneg = list(iterable)

    def __iter__(self):
        i = len(self._neg)
        while i:
            i -= 1
            yield self._neg[i]
        yield from self._nonneg

    def __len__(self):
        return len(self._neg) + len(self._nonneg)

    def __reduce__(self):
        return type(self), (), self.__getstate__()

    def __getstate__(self):
        return self._neg, self._nonneg

    def __setstate__(self, state):
        self._neg = state[0]
        self._nonneg = state[1]

    def __setitem__(self, index, value):
        if index < 0:
            self._neg[~index] = value
        else:
            self._nonneg[index] = value

    def append(self, v):
        self += v

    def clear(self):
        self._neg.clear()
        self._nonneg.clear()

    def copy(self):
        new = type(self)()
        new.__setstate__(self.__getstate__)
        return new

    def count(self, v):
        return self._neg.count(v) + self._nonneg.count(v)

    def extend(self, iterable):
        return self._nonneg.extend(iterable)

    def index(self, v):
        for i in range(-len(self._neg), len(self._nonneg)):
            if self[i] == v:
                return i
        raise ValueError("couldn't find it")

    def reverse(self):
        zero = self._nonneg.pop(0)
        self._neg.reverse()
        self._nonneg.reverse()
        self._neg, self._nonneg = self._nonneg, self._neg
        self._nonneg.insert(0, zero)

    def sort(self):
        return (self._neg + self._nonneg).sort()
