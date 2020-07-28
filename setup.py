from setuptools import setup, find_packages

setup(
    name='website',
    version='1.0',
    description='Personal Website for Scott',
    author='Scott P. White',
    author_email='spwhite1337@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'requests',
        'flask',
        'flask-wtf',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-login',
        'flask-cors',
        'gunicorn',
        'plotly',
        'dash',
        'ipykernel',
        'tqdm',
        'awscli'
    ]
)
