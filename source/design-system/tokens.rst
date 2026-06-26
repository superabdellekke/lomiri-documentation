Tokens
======

Tokens are the smallest, named design decisions in Lomiri, namely the colors, the type
sizes, the spacing unit, and the icon styles. They are named once here and reused
everywhere, so that every app draws from the same small set of choices.


.. note::

   The values on this page are the established Lomiri tokens. Where exact pixel
   conversions or names depend on the toolkit, confirm against a current build
   before treating them as fixed. The toolkit is under active development and so a lot is subject to change.

Color
------

Lomiri ships two themes, Ambiance (the light theme) and Suru Dark (the
dark theme). Every color below has a role, and most have a light-theme and a
dark-theme variant so that the same role works in both. The single most important rule when using color is that color always carries meaning: green means positive, 
red means negative, blue means neutral or active.
Never rely on color alone to communicate that meaning, since not everyone can
distinguish the hues, so pair it with a label, an icon, or position.

**Neutrals**
 
.. list-table::
   :header-rows: 1
   :widths: 8 20 16 56
 
   * - 
     - Name
     - Value
     - Role
   * - .. image:: /_static/images/swatches/swatch-white.svg
          :width: 24px
          :height: 24px
     - White
     - ``#FFFFFF``
     - Background on Ambiance (light); regular text on Suru Dark.
   * - .. image:: /_static/images/swatches/swatch-jet.svg
          :width: 24px
          :height: 24px
     - Jet
     - ``#111111``
     - Regular text on Ambiance; background on Suru Dark.
   * - .. image:: /_static/images/swatches/swatch-inkstone.svg
          :width: 24px
          :height: 24px
     - Inkstone
     - ``#3B3B3B``
     - Foreground colours in dark themes.
   * - .. image:: /_static/images/swatches/swatch-slate.svg
          :width: 24px
          :height: 24px
     - Slate
     - ``#5D5D5D``
     - Text and action icons.
   * - .. image:: /_static/images/swatches/swatch-graphite.svg
          :width: 24px
          :height: 24px
     - Graphite
     - ``#666666``
     - Background colouring in dark themes.
   * - .. image:: /_static/images/swatches/swatch-ash.svg
          :width: 24px
          :height: 24px
     - Ash
     - ``#888888``
     - Subtitles and other tertiary content.
   * - .. image:: /_static/images/swatches/swatch-silk.svg
          :width: 24px
          :height: 24px
     - Silk
     - ``#CDCDCD``
     - Neutral action buttons and secondary text.
   * - .. image:: /_static/images/swatches/swatch-porcelain.svg
          :width: 24px
          :height: 24px
     - Porcelain
     - ``#F7F7F7``
     - Foregrounds.
 
**Semantic colours**
 
.. list-table::
   :header-rows: 1
   :widths: 8 20 16 56
 
   * - 
     - Name
     - Value
     - Role
   * - .. image:: /_static/images/swatches/swatch-blue.svg
          :width: 24px
          :height: 24px
     - Blue
     - ``#335280``
     - Progress bars, selection, text cursor, and neutral actions (Ambiance).
   * - .. image:: /_static/images/swatches/swatch-light-blue.svg
          :width: 24px
          :height: 24px
     - Light Blue
     - ``#19B6EE``
     - The same roles as Blue, on Suru Dark.
   * - .. image:: /_static/images/swatches/swatch-green.svg
          :width: 24px
          :height: 24px
     - Green
     - ``#0E8420``
     - Positive action buttons (Ambiance).
   * - .. image:: /_static/images/swatches/swatch-light-green.svg
          :width: 24px
          :height: 24px
     - Light Green
     - ``#3EB34F``
     - Positive action buttons (Suru Dark).
   * - .. image:: /_static/images/swatches/swatch-red.svg
          :width: 24px
          :height: 24px
     - Red
     - ``#C7162B``
     - Negative and irreversible actions, errors, and alerts (Ambiance).
   * - .. image:: /_static/images/swatches/swatch-light-red.svg
          :width: 24px
          :height: 24px
     - Light Red
     - ``#ED3146``
     - Negative and irreversible actions, errors, and alerts (Suru Dark).
   * - .. image:: /_static/images/swatches/swatch-orange.svg
          :width: 24px
          :height: 24px
     - Orange
     - ``#E95420``
     - Branded elements, focus, and intensity.


One note: do not write these hex values directly into a
component. Refer to them through the theme, so that switching between Ambiance and
Suru Dark continues to work. A component that hardcodes ``#0E8420`` is green even
in a context where the theme wants a different green, a component that asks the
theme for "the positive colour" is always correct.

Units and spacing
-----------------

Lomiri measures layout in grid units (``gu``) rather than pixels, so that a
layout keeps its proportions across screens of different sizes and densities. One
grid unit converts to a different number of pixels depending on the display, but
it always represents the same *perceived* size to the person looking at it.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Device
     - Conversion
   * - Most laptops
     - 1 gu = 8 px
   * - High-DPI laptops
     - 1 gu = 16 px
   * - Phone, 4" screen at HD (≈720×1280)
     - 1 gu = 18 px
   * - Tablet, 10" screen at HD (≈720×1280)
     - 1 gu = 10 px

For the rare measurement smaller than one grid unit, a second unit is available:
the density-independent pixel (``dp``), which is typically one pixel on
laptops and low-density phones and tablets. Use grid units for almost everything,
and density-independent pixels only for fine detail such as a one-pixel divider.

Spacing, sizing, and layout should all be expressed in grid units. This is what
makes a layout adapt rather than simply scale, and
it's why touch targets stay large enough to hit on every device without
per-device adjustment.

Typography
----------

The default typeface is the **Ubuntu** font family, a libre typeface intended to
feel precise, reliable, and open. Use it by default.

As with spacing, font sizes are not set in fixed pixels. They are chosen from a
named scale Each size is defined in
grid units, and resolves to different pixel sizes per device automatically.

.. list-table::
   :header-rows: 1
   :widths: 22 13 17 24 24

   * - Size name
     - gu
     - Desktop
     - Phone (4" HD)
     - Tablet (10" HD)
   * - x-small
     - 1.25
     - 10 px
     - 22 px
     - 12 px
   * - small
     - 1.5
     - 12 px
     - 27 px
     - 15 px
   * - medium
     - 1.75
     - 14 px
     - 31 px
     - 18 px
   * - large
     - 2.5
     - 20 px
     - 45 px
     - 25 px
   * - x-large
     - 3.5
     - 28 px
     - 76 px
     - 42 px

Choose a size by its name and its role (a title is large, body text is medium, a
subtitle is small), not by a pixel value. This keeps type consistent between your
app and the rest of the system, and lets it scale correctly.

.. figure:: /_static/images/luitk/luitk-Label.png
  :width: 50%


Iconography
-----------

Lomiri's icons follow the Suru visual language: sharp, deliberate,
paper-fold-inspired shapes, consistent in weight and style. There are two kinds,
and they are governed by different rules:

- App icons are the icon a person sees on the home screen and in the app
  drawer. They identify your app and should follow the Suru app-icon shape and
  grid so that your app sits naturally alongside the others.

- In-app icons are the smaller icons used inside your app for actions and
  navigation (the icons in a header, on a button, in a list). Use the system's
  in-app icon set wherever a suitable icon exists, rather than drawing your own, so
  that a "search" or "delete" icon looks the same in your app as everywhere else.

  

