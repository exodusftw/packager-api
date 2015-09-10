import base64
import os.path
import itertools

class Packager():
    # Determine Package Manager - YUM or DNF
    if os.path.isfile('/usr/bin/dnf'):
        packager      = 'dnf'
        packager_path = '/usr/bin/dnf'
    else:
        packager      = 'yum'
        packager_path = '/usr/bin/yum'

