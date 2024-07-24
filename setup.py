# -*- coding: utf-8 -*-

from distutils.core import setup

# Need to potentially adjust licensing details???
setup(
    name='cookiecutter-pysteps-postprocessing-plugin',
    packages=[],
    version='0.1.0',
    description='Cookiecutter template for a Pysteps postprocessing plugin package',
    author="PySteps developers",
    license='BSD',
    keywords=['cookiecutter', 'template', 'pysteps', 'postprocessing', 'plugin'],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Hydrology",
        # "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
