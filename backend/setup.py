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
        'matplotlib',
        'requests',
        'wheel',
        'flask',
        'flask-wtf',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-login',
        'flask-cors',
        'plotly',
        'dash',
        'tqdm',
        'awscli'
    ]
)
