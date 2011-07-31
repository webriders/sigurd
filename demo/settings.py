# import dev by default
import os
import sys

PROJECT_ROOT = os.path.abspath('..')

APPS_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, 'demo', 'apps'))
EXTERNAL_APPS_ROOT = os.path.abspath(os.path.join(APPS_ROOT, 'ext'))
LIB_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, 'demo', 'lib'))
EXTERNAL_LIB_ROOT = os.path.abspath(os.path.join(LIB_ROOT, 'ext'))

sys.path = [
    APPS_ROOT,
    EXTERNAL_APPS_ROOT,
    LIB_ROOT,
    EXTERNAL_LIB_ROOT,
] + sys.path

