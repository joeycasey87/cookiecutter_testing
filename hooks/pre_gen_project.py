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

plugin_name = '{{ cookiecutter.plugin_name}}'
if not plugin_name.startswith("importer_") or not plugin_name.startswith("diagnostics_"):
    print('\nERROR: The plugin_name must start with the "importer_" or the "diagnostics_" prefix')
    sys.exit(1)
