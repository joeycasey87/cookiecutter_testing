#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

def test_plugins_discovery():
    """It is recommended to at least test that the plugin modules provided by the plugin are
    correctly detected by pysteps. For this, the tests should be ran on the installed
    version of the plugin (and not against the plugin sources).
    """

    from pysteps.io import interface as io_interface
    from pysteps.postprocessing import interface as pp_interface


    plugin_name = '{{cookiecutter.plugin_name}}'
    if plugin_name == "importer"
        new_importers = ["{{cookiecutter.plugin_name }}_xxx"]
        for importer in new_importers:
            assert importer.replace("import_", "") in io_interface._importer_methods

    elif plugin_name =='diagnostics':
        new_diagnostics = ["{{cookiecutter.plugin_name }}"]
        for diagnostic in new_diagnostics:
            assert  diagnostic.replace("diagnostics-") in pp_interface._diagnostics_methods


def test_importers_with_files():
    """Additionally, you can test that your plugin correctly reads the corresponding
    some example data.
    """

    # Write the test here.
    pass
