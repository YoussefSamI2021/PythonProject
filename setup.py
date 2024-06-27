from setuptools import setup

with open("requirements.txt") as rq:
    requirements = rq.read().split('\n')

setup(
    name='cipherCe',
    version='0.0.1',
    author='data_engineers',
    packages=['cipherCe'],
    # license='LICENSE.txt',
    description='Package that adds two numbers',
    # long_description=open('README.txt').read(),
    install_requires=[requirements],
)
