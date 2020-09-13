Managing experiments
--------------------



Creating an experiment
^^^^^^^^^^^^^^^^^^^^^^^^^

Before you can publish a study on Prolific, you'll have to create
an experiment on proliferate. This will not actually post your experiment (you
currently have to do that on Prolific) but this step is necessary to set up
the proliferate server for storing your data and for redirecting users to the
correct Prolific completion URL.

.. note:: 
   
   Before you can create an experiment, you will have to make sure that your JavaScript experiment
   is hosted somewhere publicly available under a ``https://`` URL. See the 
   :doc:`documentation of the JavaScript library </javascript-library>` for how 
   to set up a JavaScipt experiment. If you want to try out proliferate with
   an example experiment, you can use the following URL:
   ``https://stanford.edu/~sebschu/experiments/prolific-tutorial/experiment-cond-regular.html``




1. Create an study on `Prolific <https://app.prolific.co/studies/new>`_.

   Fill in the title and the description of the study in the "Study Details" section,
   select "I'll redirect them using a URL" in the "Study Completion" section,
   and then copy the completion URL that appears.
   
   Keep this window open since you'll need to go back to it later.
   
2. Create a configuration file called ``<experiment_name>.config`` of the following format: 
   (``<experiment_name>`` can be any label for your experiment.)

   .. code-block:: json
    
       {
         "name": "Name of your experiment",
         "notes": "Optional notes",
         "completion_URL": "The completion URL that you copied from Prolific",
         "experiment_URL": "The https:// URL to your experiment"
       }
    
   
   (Make sure to replace all the placeholders with the appropriate values for 
   your experiment.)
   
       
3. Create the experiment on proliferate: (Replace ``<experiment_name>`` with the label that you used in step 2.)

   .. code-block:: bash

       proliferate post <experiment_name>
  
   This should return information about the experiment such as the following:
   
   .. code-block:: text
   
       --------------------------------------------------------------------------------
       Successfully created experiment!
       Loading info...
       --------------------------------------------------------------------------------
       Name: Name of your experiment
       Notes: Optional notes
       Created at: 2020-09-11 06:54 PM
       Prolific completion URL: https://app.prolific.co/submissions/complete?cc=0815ABCD
         (Participants will be redirected to this URL after completing the experiment.
         Make sure that this URL matches the completion URL of your study on Prolific.)
       
       
       Study URL: https://proliferate.alps.science/experiment/43983215-a648-49fa-bf1a-1deff8f0e7c6
         (Use this URL to publish your study on Prolific.)
       
       Sandbox URL: https://proliferate.alps.science/experiment/43983215-a648-49fa-bf1a-1deff8f0e7c6/debug
         (Use this URL to test your experiment using the "Preview" function on Prolific.)
       
       Progress: 0 completed (0 started, 0 completed, 0 abandoned, ∞ requested)
       Experiment location: The https:// URL to your experiment
       --------------------------------------------------------------------------------

4. Test your setup using the Sandbox URL and the Prolific "Preview" function. 
   (Optional but recommended.) 

   a. Go back to the Prolific create form from step 1 and copy the **Sandbox URL** 
      into the "Study Link" section on Prolific.
   
   b. Click "Preview" at the bottom of the create form, and in the popup window, 
      click "Open study link in a new window". This should load your experiment in a new window.
   
   c. Go through the entire experiment. At the end of it you should be redirected 
      back to Prolific and it should say "Submission received".
   
   d. Make sure that your data was recorded by downloading the sandbox data:
   
       .. code-block:: bash

           proliferate getresults --sandbox <experiment_name>
           
      .. note:: 
      
          The ``--sandbox`` flag causes proliferate to download the debugging results. 
          To download the actual results, omit this parameter.
      
      If your data was properly recorded, this should download several CSV files with your data. 
      Make sure that all the data you need is present in the CSV files.
      If no data was recorded or some data is missing, check your experiment code and make sure
      that all data is recorded during the experiment and that all data is sent back to proliferate
      at the end of the experiment. See the :doc:`documentation of the JavaScript library  </javascript-library>` 
      for more information on how to implement an experiment
      with proliferate.
      
5. Publish your experiment.

  a. Go back to the Prolific create form from step 1 and copy the **Study URL** 
     into the "Study Link" section on Prolific.
  
  b. Make sure that you select "I'll use URL parameters" below the Study URL after you pasted the URL. 
     This should append several parameters of the form ``?PROLIFIC_PID=...`` to your study URL. If these paremeters are missing,
     select another option (e.g., "I'll add a question in my study") and then click again on "I'll use URL parameters".
     
  c. In the "Audience" section, select the pre-screening criteria that you want to use.
  
  d. In the "Study cost" section, choose the number of participants you would like to run, enter your estimate of how long the experiment will take, 
     and how much participants get paid for participating in your experiment. In the US, you should pay participants at least $15/hour.
     
  e. Click "Publish" to publish your experiment.
  
     At this point, participants will be able to access your experiment. You can then monitor how many participants have completed 
     or at least started your experiment, as described in the next section.



Monitoring an experiment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can monitor the progress of your experiment using the ``proliferate info`` command:

   .. code-block:: bash
   
      proliferate info <experiment_name>


This will return information about how many participants have started, completed or abandoned your experiment.

This command also prints all the URLs required for publishing an experiment on Prolific.


Downloading results
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can download results using the ``proliferate getresults`` command:

   .. code-block:: bash
   
      proliferate getresults <experiment_name>

This will download data from all participants as CSV files.

If you want to download the data from debugging the experiment with the Sandbox URL, add the ``--sandbox`` flag:

   .. code-block:: bash
   
      proliferate getresults  --sandbox <experiment_name>

See :doc:`Data processing </data>` for more information on how proliferate converts your experiment data into CSV files.


Other commands
^^^^^^^^^^^^^^^^^^^^^^^^

TODO

* ``proliferate clone <experiment_id> <experiment_name>``

* ``proliferate pull <experiment_name>``

* ``proliferate push <experiment_name>``


 


