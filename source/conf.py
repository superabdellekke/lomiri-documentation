# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lomiri Documentation'
copyright = '2026, The Lomiri project'
author = 'The Lomiri project'

version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Theme: Furo, configured to match the UBports documentation look-and-feel
# (same logos, same accent color, same custom stylesheet).
html_theme = 'furo'

html_theme_options = {
    "light_logo": "images/logo-light.svg",
    "dark_logo": "images/logo-dark.svg",
    "sidebar_hide_name": True,
    # Furo reads the two *_css_variables options and emits a <style> block
    # that sets the design tokens (font stack, brand color, etc.) so the
    # theme renders with the same look as docs.ubports.com.
    "light_css_variables": {
        "color-brand-primary": "#000000",
        "color-brand-content": "#77216F",
        "color-link": "#000000",
        "color-link-underline--hover": "#77216F",
        "color-background-primary": "#F7F7F7",
        "color-background-secondary": "#FFFFFF",
        "color-sidebar-background": "#FFFFFF",
        "color-sidebar-search-background": "#F7F7F7",
        "color-sidebar-search-border": "transparent",
        "color-sidebar-background-border": "transparent",
        "color-admonition-title-background--note": "#FFFFFF",
        "font-stack": "ubuntu, sans-serif",
        "font-stack--monospace": "ubuntu-mono, Courier, monospace",
        "color-code-background": "#f8f8f8",
        "color-code-foreground": "black",
    },
    "dark_css_variables": {
        "color-brand-primary": "#EDEDED",
        "color-brand-content": "#AD7AA9",
        "color-link": "#EDEDED",
        "color-link-underline--hover": "#AD7AA9",
        "color-background-primary": "#141417",
        "color-background-secondary": "#1A1C1E",
        "color-sidebar-background": "#1A1C1E",
        "color-sidebar-search-background": "#141417",
        "color-code-background": "#202020",
        "color-code-foreground": "#d0d0d0",
    },
}

html_static_path = ['_static']

# Custom stylesheet that adds the Lomiri-specific tweaks (Ubuntu font, the
# UBports-style rounded search, the right-margin offset for the main pane,
# the language grid, etc.) on top of Furo.
html_css_files = [
    'css/lomiri.css',
]
