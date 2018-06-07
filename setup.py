from setuptools import setup, find_packages


def get_version():
    with open('VERSION') as f:
        return f.read().strip()


VERSION = get_version()


setup(
    name='Coup challenge app',
    version=VERSION,
    url='https://github.com/yayfeng/coup-challenge',
    description='App to find number of fleet engineers',

    packages=find_packages(),

    install_requires=[
        'flask-restplus>=0.8.4',
        'Flask>=0.10.1',
        'Flask-UUID>=0.2',
        'Flask-Testing>=0.4.2',
        'gevent>=1.1.0',
    ],

    entry_points={
        'console_scripts': [
            'coup-challenge-app=coup_challenge_app.main:main',
        ],
    },
)
