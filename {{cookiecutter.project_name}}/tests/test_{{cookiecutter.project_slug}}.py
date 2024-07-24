#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

def test_postprocessors_discovery():
    """It is recommended to at least test that the postprocessors provided by the plugin are
    correctly detected by pysteps. For this, the tests should be ran on the installed
    version of the plugin (and not against the plugin sources).
    """

    from pysteps.postprocessing import interface

    new_postprocessors = ["{{cookiecutter.postprocessor_name }}_xxx"]
    for postprocessor in new_postprocessors:
        assert postprocessor.replace("postprocessor_", "") in interface._postprocessor_methods


def test_postprocessors_with_files():
    """Additionally, you can tests that your postprocessors correctly reads the corresponding
    some example data.
    """

    # Write the test here.
    pass
