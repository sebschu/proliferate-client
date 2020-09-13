.. _javascript-library:

JavasScript library
=======================================

The JavaScript library provides a function to submit the data to the proliferate 
server at the end of an experiment.

Loading the library
-----------------------

Add the following ``<script>`` tag within the ``<head>`` tag of your experiment HTML file to load the proliferate library:

.. code-block:: html

    <script src="https://proliferate.alps.science/static/js/proliferate.js" type="text/javascript"></script>

.. note::

    This library requires `jQuery library <https://jquery.com/>`_. If you are already using jQuery in your
    experiment, make sure to include the above ``<script>`` tag after loading jQuery. If you are not using
    jQuery, add the following ``<script>`` tag before loading the proliferate library:
    
    .. code-block:: html
    
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    
    
Submitting data
---------------------

To submit data at the end of the experiment, use the ``proliferate.submit`` function:

.. function:: proliferate.submit(data, [success_fct], [failure_fct])

    :param data: A JavaScript object containing all the data that needs to be submitted. See :doc:`/data` for details on how this object is stored and converted into CSV files when dowloading the data from proliferate.
    :param success_fct: An optional function with one argument that gets called if sending the data to the server succeeds. If not specified, participants will be automatically redirected to the Prolific completion URL after the data has been uploaded.
    :param failure_fct: An optional function with one argument that gets called if sending the data to the server fails. If not specified, participants receive an error message asking them to message the researcher to get compensated.


Experiment integration
------------------------

Where exactly in your code you want to call this function depends on the implementation of your experiment. Here are two examples on how
to setup the data submission.

If you are using the `Stanford experiment templates <https://github.com/alpslab-stanford/experiment_template>`_ replace the following line

.. code-block:: js

    setTimeout(function() {turk.submit(exp.data);}, 1000);

with 

.. code-block:: js

    proliferate.submit(exp.data);


------

If you are using `jsPsych <https://jspsych.org>`_ set the ``on_finish`` property in the ``init()`` call  to ``proliferate.submit``:

.. code-block:: js

    jsPsych.init({
      timeline: exp,
      on_finish: proliferate.submit
    });

