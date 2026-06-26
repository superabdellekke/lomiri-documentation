Gestures
========

The :doc:`principles` page explained that Lomiri uses gestures and the edges of the screen instead of hardware buttons or a fixed navigation bar. This page explains what that means in practice:
which gestures belong to the system, which belong to your app, and the rules that keep the two from getting in each other's way.

Two kinds of gestures 
---------------------

.. figure:: /_static/images/gestures.png
  :width: 75%

Every gesture in Lomiri falls into one of two groups, and the difference between them matters more than anything else on this page.

**System gestures** start at one of the four edges of the screen and are handled by the shell, not by your app. They behave identically in every application, so a person only has to learn them once.
Your app does not own these gestures and must never assign its own meaning to a swipe that begins at a screen edge. 

**In-app gestures** happen inside your content area. These are yours to use, with their familiar, expected meaning. A tap selects something, a pinch zooms, and so on.

The reason this split exists comes straight from the content-first principle. The center of the screen belongs to your content, and the four edges belong to the system. As long as your app respects that boundary, it can never collide with the platform it runs on.

The four system edges
---------------------

Each edge has a distinct job, and the reasoning behind each one is worth knowing, because it helps you understand and predict how a new gesture should be designed if one is ever added.

.. list-table::
    :header-rows: 1
    :widths: 15 35 50

    * - **Edge**
      - **What it does**
      - **Why**
    * - Left
      - Short swipe reveals the launcher (pinned and recent apps). A longer swipe
        opens the app drawer.
      - Most people regularly use a fairly small number of apps. The left edge
        gives fast access to those favourites without ever leaving the app
        currently open.
    * - Right
      - Short swipe switches to the previously used app. A longer swipe opens the
        spread: an overview of all open apps, where swiping a card upward closes
        it.
      - Most switching happens between just two or three apps at a time, so a
        quick swipe handles the common case. The spread covers the less common
        case of needing the full picture.
    * - Top
      - Swipe down opens the indicator panel: network, sound, battery, and
        notifications.
      - These are important but peripheral. The goal is a quick glance or a small
        adjustment without leaving what you were doing and going to a settings
        menu.
    * - Bottom
      - Swipe up reveals controls that belong to the app currently in focus.
      - This is your app's own space. See :doc:`bottom-edge` for the full detail,
        it is significant enough to deserve its own page.

.. note::
    
    The exact swipe distance and trigger area for each edge can vary slightly by device. Treat the behavior above as fixed and treat any specific pixel or distance value
    as something to confirm against a real device before writing it down as a hard number.

In-app gestures
----------------

Inside your own content, use gestures with the meaning people already expect from the rest of the system. Inventing a new meaning for a familiar gesture works against existing guidelines, so we recommend that you do not do so.

.. figure:: /_static/images/gesture-diagram.png
  :width: 75%

.. list-table::
    :header-rows: 1
    :widths: 30 70

    * - Gesture
      - Expected meaning
    * - Tap 
      - Select or activate whatever is under the finger.
    * - Long press 
      - Reveal secondary actions, enter a selection mode, or begin a drag.
    * - Long press drag
      - Pick up, move, and select multiple items.
    * - Vertical drag / scroll
      - Move through content taller than the screen
    * - Horizontal swipe on a list item
      - Reveal actions for that item, such as deleting it.
    * - Pinch
      - Zoom content in or out.
    * - Rotate (two fingers)
      - Rotate an object around a centre point, such as when editing an image. 
    * - Drag
      - Move or reorder an object the person is directly holding.
    * - Pull down from the top of a list
      - Refresh the contents of that list.

Never collide with the edges
------------------------------

If your app needs a horizontal swipe of its own, keep that interaction away from the very edges of the screen. A swipe that starts close enough to the screen will be caught by the
system instead of your app, which means the person tries to use your feature and accidentally opens the launcher or switches apps instead. If that happens during testing, the gesture is
positioned too close to the edge, not too sensitive on the system's part.

This rule also has a quieter implication for navigation design. Because the right edge already shows a spread of open apps as a stack of cards, your own app should not build a similar nested stack of
of screens inside itself. Doing so creates a second card-stack metaphor that competes with the system's, which is confusing rather than familiar. The full reasoning for this is on the :doc:`navigation` page.

A gesture must never be the only way to do something
-----------------------------------------------------

Gestures are fast, but they're invisible. There's no label on screen telling a new user that a swipe exists, the way a button announces itself just by being visible. Because of this, any important action reachable by a gesture
must also be reachable through a visible control surface: a button, a menu entry, a list item. The gesture is a shortcut for people who already know it's there. The visible control makes sure nobody is ever stuck because they did not.

This becomes even more important once a person is using your app with a mouse and keyboard instead of touch, which is covered on the :doc:`convergence` page.


Helping people discover gestures
---------------------------------

Because gestures have no built-in visual cue, it's worth teaching the ones that aren't obvious. Lomiir gives you three tools for this, from lightest to heaviest. Reach for the lightest one that
does the job.

+++++++++++++++
Bottom edge hints
+++++++++++++++

The bottom edge has a built-in, two-stage hint, so for that gesture you usually do not need to add anything of your own. When your app is first launched, the user sees a small floating icon: this is Hint 1.
After the user interacts with it, the hint morphs into Hint 2, which shows a label, an icon, or both, giving more detail about what the bottom edge will reveal, such as "+ New page". See :doc:`bottom-edge` for the full behavior.

.. figure:: /_static/images/bottom-edge-1.png
  :width: 69%
k
+++++++++++++++
Coach marks
+++++++++++++++



Use a coach mark as a single instructional overlay that points out one interaction that is not obvious or naturally discoverable. A coach mark should look visually distinct from your app's normal interface, so it is 
clearly a temporary hint and not a permanent part of the screen. Show one interaction at a time, at the moment it becomes useful, rather than explaining everything at once.

.. figure:: /_static/images/coachmark.png
  :width: 60%

+++++++++++++++
Tutorials
+++++++++++++++

Use a tutorial, a short sequence of instructions, only on the rare occasions where a single coach mark is not enough, for example when the same app is laid out differently on a larger screen and the user needs to be shown where features have moved. 
Use tutorials sparingly, because a screen covered in explanatory arrows defeats the purpose of a clean, content-first interface just as much as a screen covered in buttons would.          


Give immediate feedback
------------------------

A gesture should feel physically connected to whatever it acts on. When a person drags an item, it should move with their finger in real time, not jump to a finished state once the gesture ends. When they swipe a list row,
the row should follow the finger and reveal the action underneath as it goes. Feedback that starts the moment the gesture starts, rather than only after it finishes, is what makes an interaction feel like it belongs on this platform.


Make destructive gestures recoverable
--------------------------------------

If a gesture deletes or permanently changes something, give the person a way back. A short-lived "Undo" option after a swipe-to-delete is usually better than a confirmation dialog, because it doesn't interrupt the person who did what they meant to do.
Save confirmation dialogs for actions that genuinely cannot be undone afterward.