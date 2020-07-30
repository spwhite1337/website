from setuptools import setup, find_packages

setup(
    name='backend',
    version='1.0',
    description='Backend to app',
    author='Scott P. White',
    author_email='spwhite1337@gmail.com',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-cors',
        'uwsgi',
    ],
)
