from .dataframe import DataFrame
from .series import Series

# from teradata.dataframe.core import * will only import the items in __all__
# commenting out __all__ wil import the DataFrame and Series, as well as the modules it contains (dataframe, series)
__all__ = ['DataFrame', 'Series']
