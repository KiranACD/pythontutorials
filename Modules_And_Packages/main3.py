import sys
import importer

module2 = importer.import_('module2', 'Modules_And_Packages/module2.py', '.')

import module3
module3.hello()