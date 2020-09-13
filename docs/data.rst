Data processing
=======================================

proliferate automatically converts your experiment data into multiple CSV files
that can be easily loaded into R or other statistical analysis packages.

As explained in the :doc:`/javascript-library` documentation, your experiment
submits participant data as a `JSON <https://www.json.org/>`_ object. proliferate
stores this data as a JSON object but automatically converts the data when you download
it via the command line interface or the web interface.

To demonstrate how this works, consider the following simple JSON object with data
from 5 trials as well as information about the subject:

.. code-block:: json

    {
      "trials": [
        {
          "stimulus": "horse",
          "reaction_time": 235,
          "correct_answer": 1
        },
        {
          "stimulus": "rabbit",
          "reaction_time": 219,
          "correct_answer": 0
        },
        {
          "stimulus": "raccoon",
          "reaction_time": 177,
          "correct_answer": 1
        },
        {
          "stimulus": "bear",
          "reaction_time": 364,
          "correct_answer": 1
        },
        {
          "stimulus": "sloth",
          "reaction_time": 271,
          "correct_answer": 1
        }
      ],
      "subject_information": {
        "native_language": "English",
        "other_languages": "Spanish, French",
        "age": 30,
        "problems": "One image didn't load",
        "comments": "Great experiment!",
        "condition": "animals"
      }
    }

In this made-up example, the experiment stores the stimulus, the participant's reaction time
and whether they gave the correct answer to a comprehension question. This information
is stored in the ``trials`` variable as a list of objects.

The information about the subject is stored in the ``subject_information`` variable as 
an object.

proliferate will create a separate CSV file for each variable at the highest level of the JSON object.
In this example it would therefore create two CSV files: ``<experiment_name>-trials.csv`` and 
``<experiment_name>-subject_information.csv``.

For lists (such as ``trials``), proliferate will create one row for each element in the list. The columns in the 
CSV file correspond to the variables of each trial (``stimulus``, ``reaction_time``, and ``correct_answer`` in this example).  
Given that there are 5 elements in the ``trials`` list, proliferate would add 5 rows for each participant 
to  ``<experiment_name>-trials.csv``. For objects (such as ``subject_information``) proliferate adds one row per participant.
The CSV again contains one column for each variable in the object (``native_language``, 
``other_languages``, ``age``, ``problems``, ``comments``, and ``condition`` in this example). 
proliferate also automatically adds three columns to each CSV, a anonymous participant ID (``workerid``),
the name of the condition (will be generally ``condition1`` except when you implement different conditions 
in different experiments as described here TODO), and an ``error`` column that shows errors if they occur 
during the data export (e.g., missing data from individual participants).

Special files
---------------

proliferate also creates an additional CSV file named ``<experiment_name>-workerids.csv``
which contains a mapping between the Prolific participant IDs and the anonymous IDs 
used in all other CSV files. You can use this file to map responses to the Prolific 
IDs (for example, if you want to pay some participants a bonus depending on their performance).
For privacy reasons, this file should never be published along with your dataset.

If your experiment data JSON object contains exactly one list of objects (such as 
``trials`` in the example above), proliferate will also create a CSV file named 
``<experiment_name>-merged.csv`` that contains one line for each trial and also 
contains all the information from all the other variables (e.g., all the 
information stored in ``subject_information``).


.. note::

   Make sure that the data format is consistent across participants. proliferate
   extracts the structure of the data from one participant and then assumes that the
   data from all other participants follows the same structure.