# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
#import sphinx_rtd_theme
import sphinxcontrib.bibtex
import myst_parser
import sphinxcontrib.apa



# -- Project information -----------------------------------------------------

project = 'Justpsychiatry Article Archive'
copyright = '2022, Justpsychiatry'
author = 'Justpsychiatry'


#release = 'latest'
#version = 'latest'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx_sitemap',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.apa',
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_design',
    'sphinx_search.extension',
    'hoverxref.extension',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),

   'BJPsychBulletin':
              ('https://www.justpsychiatry.co.uk/projects/bjpsych-bull/index.html',
              ),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = "Justpsychiatry Article Archive"
html_baseurl ='https://justpsychiatry.co.uk/'
bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = 'author_year'
sitemap_filename = "sphinxsitemap.xml"
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True



hoverxref_roles = [
    'numref',
    'term',
    'abbr',
    'ref',
]



# -- Options for EPUB output
epub_show_urls = 'footnote'

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.



source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'myst',
}

rst_prolog= """


.. admonition:: Copyright Notice
 
    The historical material in this project falls into one of three categories for clearances and permissions:

    1. Material currently under copyright, made available with a Creative Commons license chosen by the publisher.
    
    2. Material that is in the public domain
    
    3. Material identified by the Welcome Trust as an Orphan Work, made available with a Creative Commons Attribution-NonCommercial 4.0 International License. 
    
    While we are in the process of adding metadata to the articles, please check the article at its original source for specific copyrights.  

    See https://www.ncbi.nlm.nih.gov/pmc/about/scanning/

"""
