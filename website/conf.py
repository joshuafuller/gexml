
import sys
import os

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import dexml2

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'hyde.ext.plugins.sphinx']

project = u'dexml2'
copyright = u'2011, Ryan Kelly'

version = dexml2.__version__
release = dexml2.__version__

source_suffix = '.rst'
master_doc = '_sphinx_index'

