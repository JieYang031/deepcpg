from .utils import *

from . import dna
from . import cpg
from . import joint


def get_class(name):
    _name = name.lower()
    if _name == 'dna01':
        return dna.Dna01
    elif _name == 'cpg01':
        return cpg.Cpg01
    elif _name == 'joint01':
        return joint.Joint01
    else:
        raise ValueError('Invalid model "%s"!' % name)