from setuptools import setup

setup(
    name='identityservice',
    version='0.1',
    py_modules=['identityservice'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        identityservice=identityservice.cli:cli
    ''',
)