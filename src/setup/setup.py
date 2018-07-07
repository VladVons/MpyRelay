from setuptools import setup, find_packages
import sdist_upip


setup (
    name         = 'mpy-relay',
    version      = '0.0.1',
    description  = 'IoT api for micropython',
    author       = 'Vladimir Vons',
    author_email = 'VladVons@gmail.com', 
    cmdclass     = {'sdist': sdist_upip.sdist},
    packages     = find_packages(),
    keywords     = 'micropython esp8266 dht22'
)

#python3 setup.py sdist
