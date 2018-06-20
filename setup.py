from setuptools import setup, find_packages


with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='ticktock',
  version='1.1.0',
  description='Useful timer-related utilities',
  long_description=readme,
  author='Tianhui Michael Li',
  url='https://github.com/tianhuil/ticktock',
  license=license,
  packages=find_packages(exclude=('test'))
)
