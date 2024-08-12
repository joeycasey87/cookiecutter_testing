import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.project_slug}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        f"\nERROR: The project slug ({module_name}) is not a valid Python module name. "
        "Please do not use a - and use _ instead"
    )
    # Exit to cancel project
    sys.exit(1)

plugin_name = "{{ cookiecutter.plugin_name}}"
if plugin_name != "importer" and plugin_name != "diagnostics":
    print(
        '\nERROR: The plugin_name must be "importer" or "diagnostics"'
    )
    sys.exit(1)
