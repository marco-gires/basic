from setuptools import setup, find_packages
import python_cheetah

__author__ = 'marc.henri'

# source = https://python-packaging-user-guide.readthedocs.org/en/latest/distributing.html
# TODO - dependencies packages

setup(
    name='python_cheetah',
    version=python_cheetah.__version__,
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
        'rabbitpy==0.25.0',
        'pytz==2014.10'
    },
    packages=find_packages(
        exclude=['tests']
    ),
    # TODO - license, url

)
