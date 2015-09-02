from setuptools import setup, find_packages
import cheetah

__author__ = 'marc.henri'

# source = https://python-packaging-user-guide.readthedocs.org/en/latest/distributing.html
# TODO - dependencies packages

setup(
    name='cheetah',
    version=cheetah.__version__,
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
    install_requires={
        'git+https://github.com/marco-gires/pip_packaging_test.git@dev',
    },
    packages=find_packages(
        exclude=['tests']
    ),
    entry_points={
      'console_scripts': [
          'python_cheetah_testing = python_cheetah:main',
      ],
    },
    # TODO - license, url

)
