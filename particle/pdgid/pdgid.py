# Licensed under a 3-clause BSD style license, see LICENSE.
"""
Class representing a PDGID.

All methods of HepPID are implemented in a Pythonic version, see the functions module.
"""

from __future__ import absolute_import

from . import functions as _functions

# Collect all the relevant functions in the pdgid.functions module
_exclude = ('IntEnum', 'Location', 'print_function', 'division', 'absolute_import')
_fname = [ fname for fname in dir(_functions) if not fname.startswith('_') and fname not in _exclude]

class PDGID(int):
    """
    Holds a PDGID.

    Example
    -------
    >>> PDGID(11).is_lepton
    True
    """
    __slots__ = () # Keep PDGID a slots based class

    def __repr__(self):
        return "<PDGID: {:d}{:s}>".format(int(self),'' if self.is_valid else ' (is_valid==False)')

    def __str__(self):
        return repr(self)

    def __neg__(self):
        return self.__class__(-int(self))

    __invert__ = __neg__

    def print_all(self):
        for item in _fname:
            print("{item:14} {value}".format(item=item, value=getattr(self, item)))


# Decorate the PDGID class with all relevant functions defined in the pdgid.functions module
for _n in _fname:
    _decorator = property( lambda self, meth=getattr(_functions, _n) : meth(self) )
    setattr(PDGID, _n, _decorator)
