from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ebanx-driver',
    version='0.0.1',
    description='EBANX Python Driver.',
    long_description=long_description,
    url='https://github.com/code-haven/ebanx-python',
    author='Abhinav I',
    author_email='abhinav.qd@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Payment Gateways',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='ebanx python payment gateway',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=['requests'],
)
