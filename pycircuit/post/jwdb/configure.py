# -*- coding: latin-1 -*-
# Copyright (c) 2008 Pycircuit Development Team
# See LICENSE for details.

import os
import sipconfig
import platform
from exceptions import KeyError

try:
    mgchome = os.environ["MGC_AMS_HOME"]
except KeyError:
    raise Exception("MGC_AMS_HOME not set, please load Mentor AMS tools setup")

# The name of the SIP build file generated by SIP and used by the build
# system.
build_file = "jwdb.sbf"

# Get the SIP configuration information.
config = sipconfig.Configuration()

# Run SIP to generate the code.
os.system(" ".join([config.sip_bin, "-c", ".", "-b", build_file, "jwdb.sip"]))

# Create the Makefile.
makefile = sipconfig.SIPModuleMakefile(config, build_file)

# Add include files
makefile.extra_include_dirs = [os.path.join(mgchome, 'include')]

# Add the library we are wrapping.  The name doesn't include any platform
# specific prefixes or extensions (e.g. the "lib" prefix on UNIX, or the
# ".dll" extension on Windows).
if platform.machine() == 'x86_64':
    makefile.extra_lib_dirs = [os.path.join(mgchome, 'aol', 'lib')]
    makefile.extra_libs = ["eldogwl_64"]
else:
    makefile.extra_lib_dirs = [os.path.join(mgchome, 'ixl', 'lib')]
    makefile.extra_libs = ["gwl"]


# Generate the Makefile itself.
makefile.generate()
