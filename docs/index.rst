.. proliferate documentation master file, created by
   sphinx-quickstart on Wed Sep  9 13:43:10 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :hidden:
   :maxdepth: 3

   cli/index
   web-interface
   javascript-library
   data
   server
   other-features


proliferate Documentation
=======================================

proliferate is a tool that facilitates running JavaScript-based experiments on `Prolific <https://prolific.co>`_.
Unlike other crowdsourcing platforms such as Mechanical Turk, Prolific does not store participant data and therefore 
JavaScript-based experiments also require a server component to store the data. proliferate provides this data storage functionality
on a :doc:`server </server>` run by the `Stanford ALPS lab <http://alpslab.stanford.edu>`_ that is available to researchers from all institutions.

proliferate was originally developed to run Mechanical Turk experiments using `experiment templates <https://github.com/alpslab-stanford/experiment_template>`_ 
that are used by many labs at Stanford but it can also be used with any other experiment written in JavaScript.

It consists of three different components:

1. a :doc:`command line interface (CLI) </cli/index>` and a web interface for interfacing with the proliferate server
2. a :doc:`JavaScript library </javascript-library>` for submitting the data from your experiment and redirecting participants to the completion URL
3. a :doc:`server </server>` for collecting, storing, and downloading participant data

Getting started
---------------

1. Sign up for a `Prolific account <https://www.prolific.co/?ref=7ZLZW7GC>`_ and a `proliferate account <https://proliferate.alps.science/admin/signup>`_.

2. a. If you want to use the command line interface (CLI), follow the :ref:`setup instructions <cli-setup-instruction>` for the CLI and  :doc:`instructions on how to manage experiments </cli/managing-experiments>`.

   b. If you want to use the web interface, follow the :doc:`instructions on how to manage experiments using the web interface </web-interface>`.



Disclaimer
-------------

Please note that you are using the server at **your own risk**. It is hosted on a reliable
cloud computing provider, the server is thoroughly secured, and we are creating daily backups of all the data. 
Nevertheless, we **cannot** provide any guarantees about the availability of the server and the security of your data. 
You should always download all data from an experiment after running it and you should always backup your data!


Contact
----------------

proliferate was built and is maintained by `Sebastian Schuster <http://sebschu.com>`_. 
Please contact him if you run into issues or have feature requests to integrate proliferate
into your web-based experiments.



   

