import sphinx_rtd_theme
import os
import sys

# Add the path to the folder containing your Python source code files
sys.path.insert(0, os.path.abspath('C:/Users/Misu/Documents/GitHub/2023-24d-fai1-adsai-teamwork-t12/ILO_7/project_deployment'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Google Maps Ext'
copyright = '2024, Sally, Sasha, Peter, Jonas, Mihai'
author = 'Sally, Sasha, Peter, Jonas, Mihai'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   'sphinx.ext.duration',
   'sphinx.ext.doctest',
   'sphinx.ext.autodoc',
   'sphinx.ext.autosummary',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
