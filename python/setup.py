from setuptools import setup, find_packages

import git_test


__author__ = 'marc.henri'

# source = https://python-packaging-user-guide.readthedocs.org/en/latest/distributing.html
# TODO - dependencies packages

setup(
    name='git_test',
    version=git_test.__version__,
    description='Python-Cheetah package',
    long_description='Python Cheetah SDK package',
    author='marc.henri',
    author_email='mgires@zipcar.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Specify the Python versions you support here. In particular, ensure
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(
        exclude=['tests']
    ),
    entry_points={
      'console_scripts': [
          'python_cheetah = python_cheetah:main',
          'python_cheetah_2 = python_cheetah:main',
      ],
    },
    # TODO - license, url

)
