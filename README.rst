cookiecutter-django-bootstrap
=============================

A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

Work-in-progress template for a complete django-based website with these intentions:

    - as lightweight as possible
    - looking at Django 1.6's startproject as a basis, but for now installs Django 1.5
    - should be easily deployable to procfile based hosting providers
    - tries to use as many environment variables as possible
    - I love dj-static by Kenneth Reitz - serving static files without a cdn

It uses a fixed set of versions as requirements, making sure that at least the dependancies that are listed, work well together.

Initial login for Django admin is whatever you set as username when cookiecutting (defaulting to "admin") and the password is "changeme".


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cd <your-workspace>
    $ cookiecutter  https://github.com/urga/cookiecutter-django-bootstrap.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.


Structure
---------

The structure used should look quite familiar:

**Requirements**

The ``requirements`` folder contains a requirements file for each environment.

If you need to add a dependency please choose the right file.

**Settings**

The ``settings`` folder contains a settings file for each environment and the ``local`` settings should be gitignored.

If you take a look at ``base.py``, you'll see that it includes the optional module ``local.py``
in the same folder. There you can override the local values and gitignore will
exclude it from your commits.

The ``testing.py`` module is loaded automatically after ``base.py`` and ``local.py`` every time you
run ``python ./manage.py test``.

**Apps**

The ``apps`` folder should contain all your local django apps, this is to keep
the structure of the project clean.

When it's time to ``python ./manage.py startapp <name>``, just move the generated
module to ``apps``. If you want to know why this works, just take a look at the line::

    sys.path.insert(0, root('apps'))

in ``settings/base.py``.


Done!
-----

Now, it's time to write the code!!!


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:

Fork This
~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* cookiecutter_ so it gets listed in the README as a template.
* The cookiecutter grid_ on Django Packages.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutter/

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they make my own project development
experience better.
