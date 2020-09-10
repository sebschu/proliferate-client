.. proliferate documentation master file, created by
   sphinx-quickstart on Wed Sep  9 13:43:10 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

proliferate
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

`proliferate` is a tool that facilitates running JavaScript-based experiments on `Prolific <https://prolific.co>`_.
It provides two main functionalities: 

* Storage of participant data from web-based experiments
* Redirection of users to the Prolific `completion URL <https://researcher-help.prolific.co/hc/en-gb/articles/360009223173>`_

It was originally developed to run MTurk experiments using `experiment templates <https://github.com/alpslab-stanford/experiment_template>`_ 
that are used by many labs at Stanford but it can also be used with any other experiment written in JavaScript.

`proliferate` consists of three different components:

1. a :doc:`server </server>` for collecting, storing, and downloading participant data
2. a :doc:`command line interface (CLI) </command-line-interface>` and a web interface for interfacing with the proliferate server
3. a :doc:`JavaScript library </javascript-library>` for submitting the data from your experiment and redirecting participants to the completion URL

Getting started
---------------

1. Sign up for a `Prolific account <https://www.prolific.co/?ref=7ZLZW7GC>`_ and a `proliferate account <https://proliferate.alps.science/admin/signup>`_.

2. a. If you want to use the command line interface (CLI), follow the :ref:`setup instructions <cli-setup-instruction>` for the command line tool and the :doc:`tutorial for posting an experiment using the CLI </cli-tutorial>`.

   b. If you want to use the web interface, follow the :doc:`tutorial for posting an experiment using the web interface </cli-tutorial>`.


Disclaimer
-------------

Please note that you are using the server at **your own risk**. It is hosted on a reliable
cloud computing provider and we are creating daily backups of all the data 
but we can **NOT** guarantee that there will be no outages or data loss.
You should always download all data from an experiment after running it and backup your data!


Contact
----------------

Proliferate was built and is maintained by `Sebastian Schuster <http://sebschu.com>`_. 
Please contact him if you run into issues or have feature requests to integrate proliferate
into your web-based experiments.

