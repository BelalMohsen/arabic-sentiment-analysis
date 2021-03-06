#! /usr/bin/python
from distutils.core import setup
from glob import glob

# to install type:
# python setup.py install --root=/

setup (name='PyArabic', version='0.1',
      description='pyarabic Arabic text tools',
      author='Taha Zerrouki',
      author_email='taha_zerrouki@gawab.com',
      url='http://pyarabic.sourceforge.net/',
      license='GPL',
      Description="Arabic Light Stemmer and segmentor",
      Platform="OS independent",
      package_dir={'pyarabic': 'pyarabic',},
      packages=['pyarabic'],
      # include_package_data=True,
      package_data = {
        'pyarabic': ['doc/*.*','doc/html/*'],
        },
      classifiers=[
          'Development Status :: 5 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ],
    );

