from setuptools import setup, find_packages

setup(
    name='backend',
    version='1.0',
    description='Backend to Website to Connect Flask API with Data Products',
    author='Scott P. White',
    author_email='spwhite1337@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'requests',
        'wheel',
        'flask',
        'flask-wtf',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-login',
        'flask-cors',
        'uwsgi',  # Bypass this on windows
        'plotly',
        'dash',
        'tqdm',
        'awscli',
        'card-classifier @ git+https://github.com/spwhite1337/card-classifier#egg=card-classifier',
        'sports-bettors @ git+https://github.com/spwhite1337/sports-bettors#egg=sports-bettors',
        'presidents-speeches @ git+https://github.com/spwhite1337/presidents-speeches#presidents-speeches'
    ],
)
