## creating a namespace for a package

```
namespaces/
├── README.md
├── proj1
│   ├── setup.py
│   └── x
│       └── dataframe
│           ├── __init__.py
│           └── core
│               ├── __init__.py
│               ├── dataframe.py
│               └── series.py
└── proj2
    ├── setup.py
    └── x
        └── analytics
            ├── __init__.py
            ├── mle
            │   ├── __init__.py
            │   └── glm.py
            └── sqle
                ├── __init__.py
                └── glm.py

```

A python namespace package is a special package that has no `__init__.py` file.
See Reference: https://packaging.python.org/guides/packaging-namespace-packages/

In the implicit implementation, the namespace package is a stub that just contains the top level package.

You can have a github repo for each namespace (x.analytics or x.dataframe) but they can also be in one repo.
The setup.py marks the folders in the same level as a distribution - something people can download and install.

You can merge the two packages analytics + dataframe under the namespace x, or keep them separate as is done here.
If they were to be merged the setup.py file would be at the same level as x. So when a user downloads the package, 
they download both dataframe and analytics packages.

```
namespaces/
├── README.md
├── proj1
│   ├── setup.py
│   └── x
│       └── dataframe
│       |   ├── __init__.py
│       |   └── core
│       |       ├── __init__.py
│       |       ├── dataframe.py
│       |       └── series.py
        └── analytics
            ├── __init__.py
            ├── mle
            │   ├── __init__.py
            │   └── glm.py
            └── sqle
                ├── __init__.py
                └── glm.py

```


The name of the distribution can be different from the name of the library
- sqlalchemy-terdata is the name in setup.py so that people do pip install sqlalchemy-teradata
- but when they actually use it, the name of the package directory is `sqlalchemy_teradata` (i.e `import sqlalchemy_teradata`)
 
