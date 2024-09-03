import pandas as pd

@pd.api.extensions.register_series_accessor("my")
class MyDSAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj
    
    def my_method(self):
        return self._obj + 1


@pd.api.extensions.register_dataframe_accessor("zhang")
class MyDFAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj
    
    def my_method(self):
        print("this is my df accessor")
        return self._obj + 1


s = pd.Series([1, 2, 3])

s.head()
s.tail()

s.google.headtail()

s.headtail()
s.heavyheadheavytail()
getattr()
setattr()

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4]})
print(df.zhang.my_method())