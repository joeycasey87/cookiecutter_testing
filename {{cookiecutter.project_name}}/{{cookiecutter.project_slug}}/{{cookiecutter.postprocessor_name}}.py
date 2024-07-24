# -*- coding: utf-8 -*-
"""
One-line description of this module. E.g.

This is a more extensive description (optional) that describes the readers implemented
in this module and other relevant information.
"""

# Function {{ cookiecutter.postprocessor_name }}_xxx to create postprocess plugins named xxx.

# IMPORTANT: The name of the postprocessor should follow the "postprocessor_name"
# naming convention. The "postprocessor_" prefix to the postprocessor name is MANDATORY since it is
# used by the pysteps interface.
#
# Check the pysteps documentation for examples of postprocessors names that follow this
# convention:
# https://pysteps.readthedocs.io/en/latest/pysteps_reference/io.html#available-postprocessors
#
# The function prototype for the postprocessor's declaration should have the following form:
#
#  def postprocess_xxx(filename, keyword1="some_keyword", keyword2=10, **kwargs):
#
#
# Function arguments
# ~~~~~~~~~~~~~~~~~~
#
# The function arguments should have the following form:
# (filename, keyword1="some_keyword", keyword2=10,...,keywordN="something", **kwargs)
# The `filename` and `**kwargs` arguments are mandatory to comply with the pysteps
# interface. To fine-control the behavior of the postprocessor, additional keywords can be
# added to the function.
# For example: keyword1="some_keyword", keyword2=10, ..., keywordN="something"
# It is recommended to declare the keywords explicitly in the function to improve the
# readability.
#
#
# Return arguments
# ~~~~~~~~~~~~~~~~
#
# The postprocessor should always return the following fields:
#
#

def {{cookiecutter.postprocessor_name}}_xxx(filename, **kwargs):
  """
  A detailed description of the postprocessor. A minimal documentation is
  strictly needed since the pysteps postprocessors interface expect docstrings.

  For example, a documentation may look like this:

  Import a precipitation field from the Awesome Bureau of Composites stored in
  Grib format.

  Parameters
    ----------
    filename : str
        Name of the file to be processed.

    keyword1 : str
        Some keyword used to fine control the postprocessor behavior.

    keyword2 : int
        Another keyword used to fine control the postprocessor behavior.

    {extra_kwargs_doc}

    ####################################################################################
    # The {extra_kwargs_doc} above is needed to add default keywords added to this     #
    # postprocessor by the pysteps.decorator.postprocess_postprocess decorator.        #
    # IMPORTANT: Remove these box in the final version of this function                #
    ####################################################################################
  Returns
  -------
  filename: file
    The file having been processed.
  """
  ####################################################################################
  # Add the code required to run the postprocessor here.
  file = open(filename, "w")
  file.write("hello world")
  file.close()
  return file

