import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print(
        f'\nERROR: The project slug ({module_name}) is not a valid Python module name. '
        'Please do not use a - and use _ instead'
    )
    # Exit to cancel project
    sys.exit(1)

importer_name = '{{ cookiecutter.postprocessor_name}}'
if not postprocessor_name.startswith("postprocessor_"):
    print(postprocessor_name)
    print('\nERROR: The postprocessor_name must start with the "postprocessor_" prefix')
    sys.exit(1)
