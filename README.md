# semver
---------
A Python library that will compare two semantic version strings.

It allows the basic comparison of `<, <=, >, >=, ==, !=`. You can also compare
a version against a requirement to see if it will meet the requirement including
pessimistic `~>` versioning.

```
In [1]: from semver import Version, valid
In [2]: v1 = Version('1.2.3')
In [3]: v1.major
Out[3]: 1
In [4]: v1.minor
Out[4]: 2
In [5]: v1.patch
Out[5]: 3
In [6]: print v1
1.2.3
```

#### Install or Build python wheel
```
git checkout https://github.com/powellchristoph/semver.git
cd semver && virtualenv .venv
source .venv/bin/activate

# install locally
pip install -e .

# or build a python wheel
# This will build dist/semver-0.1.0-py2.py3-none-any.whl
python setup.py bdist_wheel
```

#### Convienence function to validate version
```
In [15]: valid('1.2.3')
Out[15]: True
In [16]: valid('1.2.3-alpha')
Out[16]: True
In [17]: valid('1.2.3.4')
Out[17]: False
```

#### Comparisons
```
In [7]: Version('1.2.3') == Version('1.2.3')
Out[7]: True
In [8]: Version('1.2.3') == Version('1.2.4')
Out[8]: False
In [9]: Version('3.2.1') != Version('1.2.3')
Out[9]: True
In [10]: Version('1.2.3') < Version('3.2.1')
Out[10]: True
In [11]: Version('3.2.1') > Version('1.2.3')
Out[11]: True
In [12]: Version('3.2.1') >= Version('1.2.3')
Out[12]: True
In [13]: Version('3.2.1') >= Version('3.2.1')
Out[13]: True
```

#### Validate that the version will satisfy version requirements
```
In [18]: Version('1.2.3').satisfies('==1.2.3')
Out[18]: True
In [19]: Version('1.2.3').satisfies('!=1.2.4')
Out[19]: True
In [20]: Version('1.2.3').satisfies('>=0.1.2')
Out[20]: True
In [21]: Version('1.2.3').satisfies('~>1.2.1')
Out[21]: True
In [22]: Version('1.2.3').satisfies('~>1.2')
Out[22]: True
In [23]: Version('1.3.3').satisfies('~>1.2')
Out[23]: True
In [24]: Version('0.1.1').satisfies('~>1.2')
Out[24]: False
In [25]: Version('0.1.1').satisfies('~>2.1')
Out[25]: False
```

#### Run Tests
```
$ python test_semver.py
.............
----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
```
