# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:17:52 2020

@author: sharma._.g
"""

from distutils.core import setup
setup(
  name = 'topsis_101703557',         # How you named your package folder (MyLib)
  packages = ['topsis_101703557'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Implementation of topsis. User should install pandas, sys, math and operator libraries prior to execution of topsis. Command line example to run is: python topsis_101703557.py data.csv "1,2,3,4" "+,+,-,+". ',   # Give a short description about your library
  author = 'sharma._.g',                   # Type in your name
  author_email = 'souravsharma6633@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/souravsharma6633/topsis_101703557',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/souravsharma6633/topsis_101703557/archive/0.3.tar.gz',    # I explain this later on
  keywords = ['HAVE', 'A', 'GOOD','DAY'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)