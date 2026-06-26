Navigation
==========

Navigation is how a person moves through your app, and just as importantly, how they always know where they are and what they can do. 
Consistent, predictable navigation is a large part of what makes an app feel like part of Lomiri rather than a world of its own. This page covers how to structure
an app, the two ways people move through it, the role of the header, and one important rule about not imitating the system itself.


Plan the structure before you build
------------------------------------

Before writing any interface, think about how your content is organised and how a person will move between its parts. Two ideas help here.

++++++++++++++++++++++
Group related content
++++++++++++++++++++++

Sort your content and actions into logical groups, so a person can scan the app and find what they need without learning where everything is one item at a time. Groups that match
how people already think about the content are easier to navigate than groups that match how your code is organised. 

++++++++++++++++++++++
Signpost consistently
++++++++++++++++++++++

Signposts are the recurring interface elements that tell a person where they can go. Think of elements like the header, sections and the back button. Using the same signposts in the same places throughout your app creates a 
familiar environment and lowers the amount a person has to learn. Inconsistent signposting makes even a well-organised app feel confusing. 

A useful way to organise most apps is in four levels, from most to least immediately accessible:

#. **Overview**: The content you want a person to reach instantly, such as a list of emails.
#. **Top level**: Filters or groupings of that overview, such as recent or archived items.
#. **Lower level**: Detailed views of a single item, such as one email or one contact's full information.
#. **App settings**: A place for the app's own settings, kept separate from the content itself.


Two ways to move through an app
--------------------------------

Lomiri apps use two navigation models. Most real apps combine them, but it helps to know which one you're using for a given relationship between screens. 

**Header sections** switch between views of equal importance, none of them inside another. Use them when the views are peers, such as All, Recent, and Archive in an inbox. This is sometimes called flat navigation, because a person moves sideways between screens rather than deeper into anything.
Header sections are described in full below.

.. figure:: /_static/images/screenshot20260623_134838823.png

The page stack drills down into a hierarchy and back out again. Use it when one screen contains or leads to another, such as a list, and one item from that list, then a detail of that item. This is sometimes called deep navigation, because each screen sits one level further in and the back button walks the person out again. The page stack is described in full below.

The distinction is worth keeping in mind because it tells you which mechanism to reach for. Peer relationships call for header sections, and containment relationships call for the page stack.


The header
-----------

The header is the main signpost in most apps. It answers three questions for the person at a glance: where am I, what can I do here and where can I go. It should hold the app's most important actions and its main navigation.

There's a few guidelines on how to use it:

- The title is **mandatory**. It tells the person where they currently are. An optional subtitle can sit below it.
- Navigation lives at the leading edge (a back button, or a drawer holding the app's main views when they do not all fit). The leading edge is the start of the reading direction: the left in a left-to-right language such as English, the right in a right-to-left language such as Arabic.
- Actions live at the trailing edge (such as search or settings), with the most important ones surfaced directly and the rest moved into an action drawer only when there is no room. 
- Do not use a navigation drawer and an action drawer at the same time. A person is unlikely to tell them apart, and the two compete for the same corners. 
- Place negative or destructive actions at the leading edge and positive actions at the trailing edge, consistently, so muscle memory carries from one app to the next. 

Describe positions as leading and trailing rather than left and right, and anchor your components to those edges rather than hardcoding a side. An app that hardcodes "back on the left" is broken for every right-to-left language, even though it looks correct in English.

The header can appear in a few ways depending on what the screen needs: fixed (the default, useful when actions must stay reachable while scrolling), transparent (present but not the focus), or hidden, which suits full-screen apps such as a gallery or camera. If you choose to have no header at all,
you must still plan how people will move through the apps. Some apps, such as a clock, use their own arrangement of on-screen controls instead.


Header sections
----------------

A header section sits directly below the main header and lets a person switch between related views within the same screen, such as filtering an inbox between Recent and Archive. One section is always selected. This is how flat navigation is expressed in practice.

Keep the number of sections small, two or three is a good ceiling, so the header stays clear readable. When there are more sections than fit, the extra ones are reached by swiping on a touchscreen, or revealed by an arrow when a pointer is present. The way the same control adapts to touch and pointer is covered on the :doc:`convergence` page.


The page stack and the back button
-----------------------------------

Deep navigation uses a page stack. When a person opens an item, its page stacks on top of the previous one, and a back button appears in the header to return them. The back button always goes back one step, until the person reaches a main view, where it is no longer shown because there is nowhere further back to go.

On a phone, only one page is visible at a time, so the stack is simply the path the person took to get where they are. On larger screens this behaves differently, which is the next section.


Navigation across panels
-------------------------

On a larger screen, an app can show two or more panels side by side instead of one page at a time, which reduces how much navigating a person has to do. How the page stack behaves then depends on which panel an action starts in:

- An action triggered in the leading panel opens the new page across all panels.
- An action triggered in the trailing panel stacks the new page over that panel only, leaving the others as they were.

This is what lets a layout like Settings keep its list of categories in the leading panel while the chosen category fills the trailing panel. The broader principles of adapting to screen size, and to touch, pointer, and keyboard together, are on the :doc:`convergence` page.


Do not imitate the system
--------------------------

This is the rule the :doc:`gestures` page pointed forward to, and it is worth stating carefully because it is easy to misread. 

The system already has a card-stack metaphor: a long swipe from the right edge shows all open apps as a stack of cards (the spread). That deck of cards is the shell's way of representing open apps, and it belongs to the system. Your app should not build its own deck-of-cards interface that a person shuffles through,
because then there are two different card-stacks on the main device meaning two different things, which breaks the mental model rather than reinforcing it.

To be clear, this is not a warning against the page stack. Hierarchical drill-down, where one page sits on top of the previous one with a back button, is exactly the sanctioned pattern described above. What to avoid is a visible card-deck metaphor that mimics the app spread. For relationships between screens that are not a simple hierarchu, prefer a two-dimensional model where a person pans or zooms between screens,
rather than an elaborate stack.


The bottom edge
----------------

The bottom edge is the other main navigation surface, and it is specific to your app. It gives quick access to your app's most important action or a frequently used view, revealed by a swipe up on touch, or by an action in the header when a pointer is attached.
Because it is significant and has its own behavior, it has its own page: see :doc:`bottom-edge`.