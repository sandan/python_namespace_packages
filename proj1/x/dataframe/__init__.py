from .core import *

# only import the exported APIs
# from teradata.dataframe import * will only import DataFrame and Series
# commenting out __all__ will import the core package as well as DataFrame, Series
__all__ = ('DataFrame', 'Series')
