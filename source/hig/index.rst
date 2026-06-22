Human Interface Guidelines
==========================

These Human Interface Guidelines (HIG) describe how a native application should look and behave inside Lomiri. 
The purpose of these documents is consistency, a person who already knows one Lomiri app should be able to pick up yours and feel at home immediately. When every app
follows the same principles, the whole system feels cohesive rather than a a collection of completely unrelated programs.

The core idea that sits underneath everything in this document is that you shoud **focus on the content, not the controls**. The screen belongs to the person's content
and the task in front of them. Everything else is kept at the sides and is brought forward only when it is needed. Almost every rule in these guidelines is grounded in this
principle, so keep that in mind.

Who is this for
---------------
This document is for developers building **native** Lomiri applications, which are apps that use the Lomiri UI Toolkit (LUITK) and run directly on the platform. 
It explains how to make those apps behave and feel native. For exact toolkit API's, we refer to the Design System and the LUITK documentation.

What is in scope
----------------
These guidelines apply to native applications only. Web applications and Progressive Web Applications (PWAs) run inside a browser or a webview, which means that they cannot
take advantage of the system's edge gestures or take part fully in the platform's interaction model. They are therefore out of scope. The reason is that native applications are 
the only kind that can act on (and accidentally interfere with) the system itself, so they are the only kind that needs this guidance.

.. note::
   This is a working draft. The principles and interaction rules are stable. Concrete details that depend on specific toolkit components, theory or feature decisions will be
   updated as they appear.





.. toctree::
   :maxdepth: 2
   :caption: HIG Contents:

   principles
   gestures
   navigation
   convergence
   bottom-edge
   
   
