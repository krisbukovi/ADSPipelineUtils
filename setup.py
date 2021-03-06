import os
from subprocess import Popen, PIPE

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ""

with open('requirements.txt') as f:
    required = f.read().splitlines()

def get_git_version(default="v0.0.1"):
    try:
        p = Popen(['git', 'describe', '--tags'], stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        line = line.strip()
        return line
    except:
        return default

setup(
    name='adsputils',
    version=get_git_version(default="v0.0.1"),
    url='https://github.com/adsabs/ADSPipelineUtils',
    license='MIT',
    author="NASA/SAO ADS",
    description='ADS Pipeline Utils',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=required,
    #entry_points={
    #      'kombu.serializers': [
    #          'adsmsg = adsputils.serializer:register_args'
    #      ]
    #  }
  )
