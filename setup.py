from psfile import __version__ as version
from distutils.core import setup

setup(name='psfile',
      version=version,
      description='a Python module to create PostScript files',
      author='Jochen Voss',
      author_email='voss@seehuhn.de',
      url='http://seehuhn.de/pages/psfile',
      py_modules=['psfile'],
      license='GPL',
      )
