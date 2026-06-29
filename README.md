# Lomiri Documentation

-- note, Claude has been used for the configuration of Sphinx. It has not been used to write content. --

Sphinx-based documentation for the **Lomiri** operating system shell. The
project bundles two linked documents:

* `source/hig/` — the **Human Interface Guidelines** (principles, navigation,
  gestures, convergence).
* `source/design-system/` — the **Design System** guide (tokens, components,
  usage guidelines).

The landing page in `source/index.rst` ties them together with a single
toctree.

## Requirements

* Python 3.10+
* [Sphinx](https://www.sphinx-doc.org/)
* [Furo](https://pradyunsg.me/furo/) — the HTML theme (matches the
  [UBports documentation](https://docs.ubports.com) look-and-feel: same
  Ubuntu-orange accent, same light/dark surface palette, same custom
  stylesheet, same brand logos).
* [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/) — for the
  live-reload preview workflow.

## Install dependencies

It is recommended to work inside a Python virtual environment so the docs
toolchain stays isolated from the system packages.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install sphinx furo sphinx-autobuild
```

If you prefer to install into the system environment instead (not advised on
shared hosts), use:

```bash
pip install --break-system-packages sphinx furo sphinx-autobuild
```

## Build the docs

From the project root, run the standard Sphinx `html` builder:

```bash
make html
```

The rendered site is written to `build/html/`. Open `build/html/index.html`
in a browser to view it.

## Live-reloading preview

While authoring, `sphinx-autobuild` watches `source/` and rebuilds the HTML
on every change, then refreshes the browser automatically. Use a port that
isn't already in use (Plausible is known to occupy 8000 on the Lomiri
infrastructure):

```bash
sphinx-autobuild source build/html --port 8001
```

Open <http://127.0.0.1:8001> in a browser and edit any `.rst` file under
`source/` to see updates live.

## Project layout

```
.
├── Makefile              # convenience targets (make html, make clean, ...)
├── make.bat              # Windows counterpart of the Makefile
├── source/
│   ├── conf.py           # Sphinx configuration (theme = furo)
│   ├── index.rst         # landing page with the root toctree
│   ├── _static/          # static assets copied verbatim into the build
│   │   ├── css/lomiri.css       # UBports-style theme overrides
│   │   ├── images/logo-light.svg
│   │   ├── images/logo-dark.svg
│   │   └── font/                # drop Ubuntu-*.ttf here for pixel-perfect fonts
│   ├── _templates/       # HTML template overrides
│   ├── hig/              # Human Interface Guidelines
│   │   ├── index.rst
│   │   ├── principles.rst
│   │   ├── navigation.rst
│   │   ├── gestures.rst
│   │   └── convergence.rst
│   └── design-system/    # Design System guide
│       ├── index.rst
│       ├── tokens.rst
│       ├── components.rst
│       └── usage-guidelines.rst
└── build/                # generated output (ignored by git)
```

## Theme

The visual look is intentionally a faithful port of
[docs.ubports.com](https://docs.ubports.com):

* `html_theme = "furo"` with `light_logo` / `dark_logo` pointing at
  `images/logo-*.svg` (the same SVGs shipped on docs.ubports.com).
* Ubuntu-orange brand accent (`#E95420`) and the full UBports light/dark
  palette are passed to Furo via `html_theme_options["light_css_variables"]`
  and `html_theme_options["dark_css_variables"]` in `source/conf.py`.
* `source/_static/css/lomiri.css` carries the per-component tweaks (rounded
  sidebar search, the right-margin offset, the language grid, hidden
  in-page anchors) so the rendered result is visually on-brand without
  forking Furo.

If you want pixel-identical typography, drop the Ubuntu font files
(`Ubuntu-Light.ttf`, `Ubuntu-Bold.ttf`, `UbuntuMono-Regular.ttf`) into
`source/_static/font/` — the `lomiri.css` `@font-face` rules already point
at them. Without them, the browser falls back to the system sans-serif,
which looks slightly different but keeps the layout intact.

## Cleaning the build

To start fresh:

```bash
make clean
```
