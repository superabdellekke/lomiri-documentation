Convergence
===========

Convergence is the idea that a Lomiri app is a single app that runs on a phone, a tablet, and a desktop, adapting to each one. It is not three seperate apps, and it is not one phone layout strechted to fill a larger screen.
The same app, the same code, changes its shape to suit whatever device and screen it finds itself on. This page explains what that means and how to design for it.

Convergence is one of the core principles in :doc:`principles`. It is listed here in full because, like the gesture model, it is not a feature you add at the end. It shapes how you lay out a screen from the very first decision.


What convergence is, and is not
--------------------------------

Convergence is a single user experience that spans every form factor and adapts to how the device is being used. The same operating and the same applications run on phones, tablets, and desktops, using layouts that respond to the size of the screen or window.

The distinction that matters most is that the layout genuinely **adapts**, it doesn't just scale. Scaling makes everything bigger on a bigger screen, which wastes the extra space and still forces the person through the same narrow path they had on the phone. Adapting uses
the same extra space to show more at once and to remove steps. A bigger screen should mean less navigating, not just larger buttons.

The appeal of this is concrete. A person can begin drafting an email on their phone during the journey to work, then plug the phone into a monitor at their desk and continue composing that very email in a desktop layout, without switching apps or losing their place.


Support every input at the same time
-------------------------------------

This is the heart of convergence and the rule most likely to catch a developer out. A Lomiri app must support touch, a pointer (mouse or trackpad), and a keyboard equally and at the same time. These are not seperate modes that the app switches between. A person using a laptop with a touchscreen might tap the screen one moment and use the trackpad the next, and the app
must handle both without caring which is which.

The clearest example is a context menu, reached three different ways for the same result:

.. list-table::
    :header-rows: 1
    :widths: 25 75

    * - Input
      - How the context menu is opened
    * - Touch 
      - Swipe or long-press the item.
    * - Pointer 
      - Right-click the item.
    * - Keyboard 
      - Focus the item and press the Super key.

Every component is built to work this way. The rule that follows for your own app is the one introduced in the :doc:`gestures` page: a gesture must never be the only way to do something. A touch-only gesture has no equivalent for a person using a pointer or a keyboard, so it does not just inconvenience them, it breaks convergence outright. Every action needs a path for all three inputs.

Within that rule, let the most suitable affordance lead on each device. On a touchscreen, a swipe or an edge may be the most natural way to reach something. With a pointer attatched, a visible control or a hover hint is often clearer. The point is not to force the touch model onto the desktop, nor the desktop model onto the phone, but to offer each input the way of working that fits it, while keeping every action reachable by all of them.


Adapt the layout with panels
-----------------------------

An app lives in a window (in a windowed, desktop-like environment) or a surface (in a non-windowed environment), and its layout responds to the size of that window or surface. The common way to build a responsive layout is with panels.

On a small surface, such as a phone, a single panel is shown at a time. The person moves between panels by tapping into tiems and using the back button, exactly the page stack described in :doc:`navigation`. As the window or surface grows, the app can show two or more panels side by side instead, so related content is visible at once and the person navigates less. Contacts, messages, and email apps are typical examples: a list and a detail view that sit on seperate pages
on a phone become two panels side by side on a desktop.

 
The platform provides a way to build this kind of adaptive, multi-column layout that tracks how many columns can be shown at once and automatically switches between, for example, a one-panel and a two-panel arrangement as the person resizes
the window. When panels are joined and the window is resized, it is normally the trailing panel that resizes while the leading panel keeps its dimensions. You specify where panels should go and the width at which they are allowed to expand, as the layout places them for you.


Grid units
-----------

Convergence depends on a measurement that does not change between devices of different pixel densities. The platform provides this through grid units. A size given in grid unites occupies the same proportion of the screen whether the device is a low-density phone or a high-density tablet, so a layout keeps its proportions across devices without per-device pixel work.

Panel widths are often expressed in grid units. When a layout resizes, the trailing panel commonly settles at around 40 or 50 grid units, though a panel can be made resizable depending on what the app needs.


Designing a convergent app
---------------------------

Pulling the above together, a few practical habits make an app converge well:

- **Design for the smallest and the largest screen together, from the start.**
    - Phone-first designs will cause an app to scale rather than adapt. Decide early what extra panels or content a larger screen should reveal.

- **Make every action reachable by touch, pointer, and keyboard.**
    - If you can only describe how to do something by swiping, it isn't convergent yet.

- **Anchor to leading and trailing, not left and right.**
    - This serves convergence and right-to-left languages at once, as described in :doc:`navigation`.

- **Use the platform's adaptive layout facilities rather than hand-building your own breakpoints.**

- **Test by resizing the window, not only by running on one device.**
    - Most convergence problems appear at the moment the layout switches between one panel and several, and resizing is the fastest way to find them.

Several of Lomiri's built-in apps, such as the calendar, contacts, and music apps, are built this way and behave consistently from phone to desktop. They are a useful reference for how a convergent app should feel.
