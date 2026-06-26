Bottom Edge
===========

The bottom edge is the one screen edge that belongs to your app rather than to the system. A swipe up from the bottom reveals a surface that you control, and it is the intended home for your app's most important
action or a frequently used view. This page explains what to put there, how people discover it, and how it behaves across devices.


What the bottom edge is for
----------------------------

Where the other three edges serve the system, the bottom edge serves your app. Use it for the single most important thing a person does in your app, or a view they return to often. Common examples are creating new content (a new message, a new note, a new alarm), opening a short form (adding a contact), or switching between the app's open views.

Because it is reached with one deliberate swipe and is consistent across every Lomiri app, the bottom edge lets you keep the main action available without spending permanent screen space on it. This is the content-first principle from :doc:`principles` in practice, because the action is there when wanted and out of the way when not.

Do not build a competing bottom bar. If you put a custom toolbar or a second set of controls along the bottom of the screen, it fights the bottom-edge swipe and confuses what the bottom of the screen means. Let the bottom edge be the bottom edge.


How people discover it
-----------------------

A swipe with no visible cue is invisible, so the bottom edge announces itself with a built-in, two-stage hint. You don't need to design your own.

When you app is first opened, the person sees a small floating icon at the bottom of the screen. This is the first hint in that it signals something that can be revealed by swiping up. After the perosn has interacted with it, the hint changes into a second form that shows a label, an icon, or both, giving more detail about what the bottom edge will reveal, such as "+ New page". 
The two stages move from "there is something here" to "here is what it does", without taking over the screen.


How it behaves
---------------

When the bottom edge is pulled up, its view stacks over the current page, in the same way a page stack works in :doc:`navigation`. A downward-pointing chevron appears so the person can return to the previous page. 

On a device with a pointer rather than a touchscreen, there is no swipe from the edge, so the same action is reached from a control in the header instead. This is the convergence rule from :doc:`convergence` again: the bottom edge is the touch affordance, and a person using a mouse or keyboard reaches the same place a different way. Whatever the bottom edge reveals must therefore also be reachable without a swipe, so that nothing is locked behind a touch-only gesture.


A short checklist
------------------

- Put your most important action or most-returned-to view on the bottom edge, not buried in a long menu of everything.
- Let the built-in two-stage hint introduce it, do not invent your own permanent bottom control to point at it. That would be redundant.
- Make sure the same action is reachable with a pointer and keyboard, since swiping does not exist in that context.
- Do not place a competing toolbar or controls along the bottom that fight the swipe.
