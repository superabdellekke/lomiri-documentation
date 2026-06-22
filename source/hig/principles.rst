Principles
==========

Everything in these guidelines follows from a small number of ideas. This page states those ideas and the pages that follow are each one principle worked out in detail, so it's
worth reading this page first and returning to it whener a later rule seems arbitrary.

.. note::
    This page describes principles that have remained stable since Lomiri's predecessor, Unity8, first established them, during the Ubuntu Phone days when Canonical was still spearheading the project.

Focus on content, not controls
------------------------------

This is the most fundamental principle in Lomiri, and the one that every other rule ultimately serves. The content or task in front of the person should have the screen's full
attention. Everything else is secondary. It should stay out of the way until it is wanted, and then be easy to reach.

A simple way to imagine it is this: think of looking through a photo album. What matters is the photos. The scissors and tape used to mount them are not on display, they did their
job and then blend in with the background. An app that keeps every control permanently visible is like leaving the scissors glued to the page. It takes up space that the content
deserves, for the sake of actions the person *might* use. 

This gives a concrete test you can apply to any screen you design, namely: **is the content the most important thing on the screen, or is the interface competing with it?** 
If a button, toolbar or label is permanenty visible, it has to earn that position by being needed almost all the time. If it's not needed that often, it belongs behind a gesture, a menu
or an edge.

This principle is also the reason why Lomiri doesn't have a permanent home button, navigation bar (unless on Desktop) or fixed toolbar. Interaction happens through gestures and the edges of the screen instead,
which is the subject of the next page.

Suru: the same idea, expressed visually
---------------------------------------

Lomiri's visual language is called **Suru**. Suru is inspired by Japanese origami: paper folded into a precise, solid shape that can still unfold to reveal more. It is the content principle applied to both layout and surface, rather
than to interaction. on a small screen, information is folded into a compact, deliberate shape. As the screen grows, that shape can unfold to expose more at once, without losing its structure.

In practice, Suru mean sharp, deliberate lines; a clear and limited use of transparency; and the sense that every element was placed on purpose rather than left where it landed. An app that uses Suru's visual language 
consistently and follows the content-first principle should be recognisable as a Lomiri app even from a distance, without needing to see a logo.

One family
-----------

Every native Lomiri app should feel and behave as part of the same family, regardless of which toolkit or language it happens to be written in. If someone knows how one Lomiri app works,
they should already know roughly how to use yours: where the main actions live, what a swipe from each edge does, how a list behaves. Consistency is something the system provides, not something each app
has to invent for itself.

Fast and natural interaction
----------------------------

The second core principle, after content, is that interaction should be fast and direct, without relying on hardware buttons or a fixed on-screen button bar. Lomiri us built around
gestures and the edges of the screen. This is covered in full on the :doc:`gestures` page, but it is listed here as a core principle because it shapes almost every other decision in an app's design:
if an action is important, the question is not "where do I put a button for this", but "which gesture or edge is the right place for this."

Convergence
------------

The third core principle is that a Lomiri app is not a phone app that happens to also run elsewhere. It is the same app, genuinely adapting to whatever device it finds itself on: phone, tablet or desktop with a mouse and keyboard,
rather than simply stretching its phone layout to fill a bigger screen. This is covered in full on the :doc:`convergence` page. It is listed as a core principle here because, like fast interaction, it has to be considered from the first decision you make about how a screen is laid out.

