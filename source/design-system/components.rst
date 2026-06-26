Components
==========

Components are the reusable building blocks an app is built from. While :doc:`tokens` defines the smallest decisions (color, type size, spacing), components combine those decisions into 
functional pieces of the interface. This page, compared to the Human Interface Guidelines, documents what each component is, its purpose, anatomy and how it behaves.

.. note::
    This section documents the components at the design level. Because this is an ever changing document, specific API names or references are not noted here. For the current API, always refer to the current version of the
    Lomiri UI Toolkit. This page tells you what each component does and what its used for, while the LUITK tells you how to actually use it.


App structure
----------------------

Every app is rooted in a main view, which is the single root container that wraps the whole app, applies the theme, provides the app header and toolbar, and handles screen orientation.

Within the main view, the unit of content is a page, which is either a single screen or view within the app. Pages can be presented one at a time on a small screen or side by side on a larger one.

The page stack manages deep navigation, a last-in-first-out stack where pushing a page shows it on top. The back button in the header is connected to this stack. See :doc:`../hig/navigation` for when to use the page stack vs sections.

The adaptive multi-column layout is the primary tool for convergence. It tracks how many columns the current window or surface can accommodate and places pages into those columns automatically. On a phone it shows one columng, on a tablet or desktop,
it can show two or more side by side, switching as the window is resized. See :doc:`../hig/convergence` for the full treatment. Column behaviour is configured by specifying column metrics and breakpoints while the layout handles placement automatically.

The panel is a surface that can be swiped in and out from an edge of the window. For most apps, the main view's built-in bottom toolbar is the right choice.


.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item::
      :columns: 12 12 4 4

      .. figure:: /_static/images/luitk/doc-app-phone.png
         :width: 100%

   .. grid-item::
      :columns: 12 12 8 8

      .. figure:: /_static/images/luitk/doc-app-desktop.png
         :width: 100%


The header
-----------

The header is covered in full in :doc:`../hig/navigation`. In component terms, it has two layers.

The page header is the main strip, which is a title with a leading action bar and a trailing action bar. The leading area holds navigation. Think of a back button, or a drawer for main views when they don't all fit. The trailing area holds actions.
When there are more actions than slots, an overflow button appears automatically to surface the rest.

.. figure:: /_static/images/luitk/luitk-PageHeader.png
  :width: 40%

The sections strip sits below the header and provides flat navigation: a row of labelled sections where one is always selected. Tapping a section switches the view, while swiping reveals sections that don't fit in the visible area. A pointer hovering reveals an arrow for the same purpose.

.. figure:: /_static/images/luitk/luitk-Sections.png
  :width: 40%

The edit-mode toolbar appears below the header when an app enters an editing state. It holds the actions relevant to editing, like selecting, rearranging, or deleting content. It disappears when editing ends.

.. figure:: /_static/images/luitk/doc-header-editmode.png
  :width: 40%

Actions
-------

An action is a named, reusable unit of functionality with a label, an icon and a trigger. Actions are objects, which means that they can be shared between components, grouped into lists and made visible or invisible by context. This is the model behind everything in the header, the context menu, and the toolbar. Defining actions separately from the components that present them means the same action can appear in the header on a phone and 
in a context meny on a desktop without writing it twice.

The action bar is a row of buttons backed by a list of actions. It manages how many it shows directly and autmatically creates an overflow panel for the rest.\

.. figure:: /_static/images/luitk/luitk-ActionBar.png
  :width: 40%

The bottom edge
---------------

The bottom edge is covered in full in :doc:`../hig/bottom-edge`. In component terms, it has three parts.

The bottom edge gesture handler manages the upward swipe, the content it reveals, and the animations. The revealed content is a page that stacks over the current view and a downward-pointing indicator in the header lets the person return.

The bottom edge hint provides the discoverability mechanism: a floating icon on first launch that transforms into a labelled hint after the first interaction. On a desktop with a pointer, the same content is reached through an action in the header rather than a swipe.

.. figure:: /_static/images/luitk/luitk-BottomEdgeHint.png
  :width: 40%

Bottom edge regions let a developer define distinct zones within the swipe that trigger different content or actions as the gesture passes through them.


Lists and collection views
--------------------------

The list item is the base element of a list. It defines no visual layout of its own, only behaviors So, leading actions revealed by swiping left (for negative or destructive choices), trailing actions revealed by swiping right (for positive ones), a selection state, a drag handle for reordering and dividers between items.

.. figure:: /_static/images/luitk/luitk-ListItem.png
  :width: 40%

The list item layout helper builds a properly proportioned Lomiri list item on top of the list item, which contains a mandatory primary text slot, an optional subtitle, and configurable leading and trailing accessory slots. This is the right starting point for any standard list item. We recommend using this as the right starting point for any standard list item,
because building a custom layout from scratch is harder to keep consistent.

.. figure:: /_static/images/luitk/luitk-ListItemLayout.png
  :width: 40%

The slots layout is a horizontal arrangement of slots following Lomiri design standards. it is the mechanism the list item layout uses internally, and can be used directly for custom horizontal arrangements. 

.. figure:: /_static/images/luitk/luitk-SlotsLayout.png
  :width: 40%

The progression indicator is a fixed chevron that sits in the trailing slot of a list item to signal that tapping will navigate deeper. Nothing else should share the slot it occupies.

.. figure:: /_static/images/luitk/luitk-ProgressionSlot.png
  :width: 40%

The list view is a specialist scrolling list that adds expand and collapse behaviour to items, automatically repositioning an expanding item when it opens and collapsing it when the person taps elsewhere.

.. grid:: 2

   .. grid-item::

      .. figure:: /_static/images/luitk/luitk-LomiriListView.png
         :width: 100%

   .. grid-item::

      .. figure:: /_static/images/luitk/doc-scrollview.png
         :width: 100%

The captions component is a twin-label column, with a primary and secondary label in a vertical stack, for use in slot-based horizontal layouts.

.. figure:: /_static/images/luitk/luitk-Captions.png
  :width: 40%

Buttons and controls
--------------------
 
The standard button performs a single action. Its color expresses its role
using the semantic colours from :doc:`tokens`: green for positive, red for
destructive, themed neutral otherwise. States are at-rest, pressed, focused (for
pointer and keyboard), and disabled. A disabled action should be shown greyed
rather than hidden so people learn it exists.

.. figure:: /_static/images/luitk/luitk-Button.png
  :width: 40%
 
The combo button is a split control: a main button on the left triggers the
primary action. A dropdown button on the right expands a panel showing additional
options. Use it when one action is dominant and a set of related alternatives is
occasionally needed, without committing permanent screen space to all of them.

.. figure:: /_static/images/luitk/luitk-ComboButton.png
  :width: 40%
 
The switch toggles a single binary setting on or off. Use it for settings that
take effect immediately. States are on, off, focused, and disabled.
 

.. figure:: /_static/images/luitk/luitk-Switch.png
  :width: 40%
 

The checkbox allows selecting any combination from a set, or confirming a
single choice such as accepting terms. The label must be unambiguously associated
with the checkbox.

.. figure:: /_static/images/luitk/luitk-CheckBox.png
  :width: 40%
 
Radio-style selection presents a set of mutually exclusive options, meaning that exactly
one is always selected. Do not use this pattern for command actions. If the list is long and
typeable, a text field is more appropriate.

.. figure:: /_static/images/luitk/luitk-RadioSelection.png
  :width: 40%
 
The slider selects a value from a continuous range by dragging a thumb along a
track. Use it for settings with a meaningful range (volume, brightness) rather than
for precise value entry, where a text field is clearer.

.. figure:: /_static/images/luitk/luitk-Slider.png
  :width: 40%
 
The option selector handles both single-value display and multi-choice
expansion in one component. Collapsed, it shows the currently selected value while when
expanded, it shows all options as a scrollable list. It can also be configured to
always appear expanded.


.. figure:: /_static/images/luitk/luitk-OptionSelector.png
  :width: 40%
 
Text input
----------
 
The single-line text field accepts one line of typed input. It supports
validation, input masks, and password echo mode. Anatomy is the input area, an
optional placeholder hint, and optional leading or trailing icons for actions like
clearing or revealing a password. States are empty, focused, filled, and error.

.. figure:: /_static/images/luitk/luitk-TextField.png
  :width: 40%
 
The multi-line text area accepts blocks of text. It scrolls its own content
once it overflows, rather than growing without limit. Use it for notes, messages,
and any input where the person might type more than a sentence.

.. figure:: /_static/images/luitk/luitk-TextArea.png
  :width: 40%
 
Date, time, and value pickers
------------------------------
 
The picker panel shows a date, time, or value picker in a way that adapts to
the form factor: as a fullscreen overlay on a phone where space is tight, as a
popover on a tablet or desktop where there is room. The picker itself presents
values on a scrolling reel, the person selects by scrolling to a value, a
pattern that works naturally with both touch and pointer. Use the system picker
rather than building a custom one, so the behaviour is familiar and accessible.

.. figure:: /_static/images/luitk/dock-picker.png
  :width: 40%
 
Progress and loading
--------------------
 
The activity indicator is a spinning animation for tasks of unknown duration.
Use it when something is happening but no proportion can be measured, such as a
connection being established or a cache being refreshed. It should be visible for as
long as the wait lasts and disappear immediately when it ends.

.. figure:: /_static/images/luitk/luitk-ActivityIndicator.png
 
The progress bar shows measurable progress as a filled track. A determinate
bar should reach 100% and stop exactly once. If the final step is verifying
success, allocate a fraction of the bar to that step rather than jumping to full
and then waiting. An indeterminate progress bar uses an animation rather than a
fill level, for tasks where proportion is unknown.

.. figure:: /_static/images/luitk/luitk-ProgressBar.png
 
Place the progress bar near the action that started it, so the person can see
which operation is running.
 
The pull-to-refresh component wraps a scrollable view and detects an overscroll
pull from the top, triggering a reload of the content. The common gesture for
refreshing a list (pull down and release) is handled automatically.
 
Scrollable areas
----------------
 
The scrollable view is a container that adds scrollbars and keyboard scrolling
to any flickable content. It places scrollbars correctly for both touch (where they
are subtle overlays) and pointer (where they are conventional rails the person can
click). This is the component to wrap a list view, a panel, or a text area when
you need scrolling. Do not build a custom scrollbar. The standard one carries the
behaviour people already expect and includes keyboard and pointer support, which is
part of how an app converges.
 
Visual and shape components
----------------------------
 
The Lomiri shape is a rounded rectangle that blends a source image over a
background colour. It is the signature visual element of the Lomiri aesthetic,
the rounded corner and the fold-like layering of image over surface are what give
apps their characteristic Suru look. Use it wherever you are displaying an
image, artwork, or avatar rather than drawing a raw rectangle.
 
The overlay variant adds a coloured overlay on top of the image layer, useful
for tinting or status colouring.
 
The proportional shape variant is specifically intended for icons and vignettes
where the aspect ratio must be maintained.
 
Animation
---------
 
Lomiri defines standard animation durations and easing curves
that all components use. Using these standards for any custom animation in your app (transitions, reveals, dismissals)
is what makes the app feel like it belongs
in Lomiri rather than running inside it. Consistent animation timing is as much
part of the Lomiri feel as consistent colour or type.
 
A number animation with the standard settings already applied is also provided
for animating numeric property changes. Prefer it over a generic animation with
manually specified timing.
 
Theming
-------
 
The colour palette provides the named colours from :doc:`tokens` as
a programmatic object. Components consume colours from here rather than writing hex
values, so they stay in sync with theme changes.
 
The theme provides facilities for reading the active theme and for themed
components to request the colours appropriate to their current state. A component
asks the theme for "the positive colour in the normal state" and gets the right
value whether Ambiance or Suru Dark is active.
 
The styled item is the base for any component that participates in the theme
system. It allows a component's visual style to be swapped at runtime through a
style name or a custom style component, while still pulling colours and metrics
from the active theme. Use this as the base if you are building a custom component
that needs to remain theme-aware.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item::
      :columns: 12 12 4 4

      .. figure:: /_static/images/luitk/doc-theme-light.png
         :width: 100%

   .. grid-item::
      :columns: 12 12 8 8

      .. figure:: /_static/images/luitk/doc-theme-dark.png
         :width: 100%
 

