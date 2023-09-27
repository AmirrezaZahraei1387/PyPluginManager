#!/usr/bin/env python
import setuptools
from setuptools import setup

setup(
    name='pmlion',
    version='0.1',
    description='A cross platform tool for managing the plugins of applications.',
    author='Amirreza Zahraei',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
    keywords="Windows linux Plugin PluginManager Library LibraryManager BuildTool",
    author_email='amir.reza.zahraei@gmail.com',
    url='https://github.com/AmirrezaZahraei1387/PyPluginManager',
    packages=setuptools.find_packages(),
    install_requires=[
        'Vmanager'
    ],
)