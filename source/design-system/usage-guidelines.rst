Usage guidelines
================

Tokens give you the raw values and components give you the building blocks, but a
design system only works if they are combined well. This page covers the rules for
combining them: how to keep an app accessible to everyone, how to make it adapt
across devices, and how to make it work in every language. These are the
cross-cutting concerns that touch every screen, no matter which components it uses.

Accessibility
-------------

An app is only finished when it works for people who see, hear, move, and read
differently. A few rules carry most of the weight.

**Never rely on colour alone.** This is the most frequently broken accessibility
rule and the easiest to fix. Colour in Lomiri carries meaning — green for positive,
red for negative — but a significant number of people cannot distinguish those
hues. Every time colour communicates something, a second cue must communicate the
same thing: a label, an icon, or a position. A red "Delete" button is fine; a
button that is *only* red, with no word or icon, is not.

**Keep touch targets large enough.** Anything a person can tap must be big enough to
hit comfortably, including people with larger fingers or reduced fine motor control.
Because Lomiri measures in grid units (see :doc:`tokens`), sizing targets in grid
units keeps them comfortable across every device automatically. Do not shrink a
control below a comfortable target size to fit more onto a screen.

**Provide more than one way to act.** As covered in the gestures guidance, a gesture
must never be the only route to an action, because gestures are invisible and not
everyone can perform them. Every important action needs a visible control as well.
This is an accessibility rule as much as a discoverability one.

**Respect contrast and text size.** Use the tokens as intended: regular text in the
text colour, secondary content in the secondary colour, against the matching
background. Do not place tertiary-grey text on a coloured background where it
becomes hard to read. Let people's chosen text size take effect rather than forcing
a fixed size.

**Make state visible to assistive technology.** A control's state — selected,
disabled, in progress — should be conveyed in a way that is available to screen
readers and other assistive tools, not only shown visually.

Responsiveness and convergence
------------------------------

Lomiri apps run on phones, tablets, and desktops, and the same app should feel right
on each. The full principles are in :doc:`../hig/convergence`; the rules that bear
directly on combining components are these.

**Adapt the layout; do not just scale it.** A larger screen is an opportunity to
show more at once and to remove steps, not merely to enlarge everything. Use the
adaptive multi-column layout so that a single column on a phone becomes several
panels on a desktop, rather than stretching one column to fill the width.

**Build in grid units, not pixels.** Expressing every size and space in grid units
is what allows one layout to hold its proportions across devices. A layout built in
fixed pixels will look right on exactly one screen.

**Support touch, pointer, and keyboard at once.** These are not separate modes. The
same app may be used by finger, then by trackpad, then by keyboard, within a minute.
Every component must respond to all three: a list item that can be swiped on touch
must also offer its actions to a right-click and to keyboard focus. When you add an
interaction, ask how it works with each of the three inputs before considering it
done.

**Let the right affordance lead on each device.** Supporting every input does not
mean every input works identically. On touch, an edge swipe may be the natural way
in; with a pointer, a visible control is often clearer. Offer each input the way of
working that suits it, while keeping every action reachable by all of them.

Localisation
------------

An app that only works well in English is unfinished for most of the world.

**Leave room for text to grow.** Translated text is often longer than the English
original — sometimes much longer. Design layouts that flex to accommodate longer
labels rather than truncating them or breaking. Do not hardcode a width that only
fits the English string.

**Anchor to leading and trailing, not left and right.** Lomiri supports right-to-left
languages such as Arabic, in which the whole layout mirrors. A control placed at the
"leading" edge sits on the left in English and on the right in Arabic, which is
correct in both. A control hardcoded to "the left" is wrong in every right-to-left
language. Building in leading and trailing terms, as the components are designed to,
lets the layout mirror correctly.

.. note::

   The extent to which the current toolkit mirrors layouts automatically for
   right-to-left languages is worth confirming against a real build and an
   right-to-left locale. The rule for app authors is stable regardless: describe and
   anchor positions as leading and trailing, never as fixed left and right.

**Do not assume formats.** Dates, times, numbers, and currencies are written
differently in different places. Use the system's localisation facilities to format
them rather than assembling them by hand, so they are correct for each person's
locale.

**Keep words out of images.** Text baked into an image cannot be translated. Where
text must appear over an image, keep it as real text laid on top, so it can be
translated like any other string.

Putting it together
-------------------

The thread running through all three sections is the same one that runs through the
whole Design System: a small set of shared decisions, applied consistently, serves
people better than each app solving the same problems its own way. An app that uses
the tokens as intended, composes the standard components, and respects these
accessibility, convergence, and localisation rules will feel like part of Lomiri —
which is the entire purpose of having a design system at all.