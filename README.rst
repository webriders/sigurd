==============
Sigurd project
==============

Sigurd project is **Django project configurator**.

Django is very flexible framework. You could build web-application of any size and complexity with it.
But if your project becomes big, sometimes (*often, actually*) its structure becomes a mess!
And its configuration becomes very complex.

Our goal is to make configuration simple and clear for big and complex Django projects. We even offer a project profiles!

Sigurd contains of two parts:
  1. **Project utilities** (tools to configure your project)
  2. **Web-configurator** (DB of existent configurations)

-----------------
Project Utilities
-----------------

Utilities extends your Django project configuration:
  1. You can add/remove applications into your Django project from the command line
  2. You can it as well from the config file
  3. After apps were installed you can to manually re-configure them
  4. You can create different Django project profiles

There are:
  1. Command-line project utils
  2. Python (Django) configuration utils

Installation
^^^^^^^^^^^^

TODO: we are plan to make a distributive that you could install with pip:

::
    
    pip install sigurd

But for now only source code is available at http://github.com/webriders/sigurd


----------------
Web-configurator
----------------

Web-configurator is a web-site which contains Django apps configurations and profiles.
We have deployed it here for now: http://sigurd.webriders.com.ua/

At the site you can do next:
  * Manually download specific Django app config and add it into your project
  * Upload your own app config or profile
  * Construct on-line (choose apps) and download Django project *(Note: we don't know if we will make it in scope of DjangoDash 2011)*

Installation
^^^^^^^^^^^^

We provide this site sources.
You can deploy it locally or make a clone if you want.
We have specific project structure. You will find the Site Django project in the *'source'*.

Extra information
^^^^^^^^^^^^

For license instructions, see LICENSE.