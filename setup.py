from distutils.core import setup
import glob

bin_files = glob.glob("bin/*.py") + glob.glob("bin/*.txt")

# The main call
setup(name='despyfitsutils',
      version ='1.0.1',
      license = "GPL",
      description = "A set of handy Python fitsfile-related utility functions for DESDM",
      author = "Felipe Menanteau, Michelle Gower",
      author_email = "felipe@illinois.edu",
      packages = ['despyfitsutils'],
      package_dir = {'': 'python'},
      scripts = bin_files,
      data_files=[('ups',['ups/despyfitsutils.table']),]
      )

