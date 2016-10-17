import os
import sys
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')

on_appengine = os.environ.get('SERVER_SOFTWARE','').startswith('Development')
if on_appengine and os.name == 'nt':
    os.name = None
    sys.platform = ''