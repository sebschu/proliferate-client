.. raw:: html

    <h1>Command-line interface (CLI)</h1>
    
    <h4>Table of contents</h4>

.. toctree::
   :maxdepth: 3


   command-line-interface


.. _cli-setup-instruction:

Setup instructions
--------------------

Windows
^^^^^^^^^^^^^

1. Open the Command Prompt (e.g., press Windows+R to open the *Run* box, type "cmd", and click OK).

2. Make sure that pip is installed by running ``pip --version``. (To run a command, type the command in the Command Prompt window and press the return key.)

   If you get an error message, make sure that Python 3 and pip are installed. We recommend using the `Anaconda <https://www.anaconda.com/products/individual>`_ Python distribution.
   
3. Make sure that Git is installed by running ``git --version``. 

   If you get an error message, make sure that Git is installed. You can download Git for Windows from `here <https://git-scm.com/download/win>`_. 


4. Install the command line interface by running the following two commands:

    .. code-block:: bash

        git clone https://github.com/sebschu/proliferate-client
        pip install -e proliferate-client
        
5. Go to https://proliferate.alps.science/admin/api to look up the API key and API secret of your proliferate account. 

   (If you don't have a proliferate account yet, you can ceate one `here <https://proliferate.alps.science/admin/signup>`_.)

6. Open the Start Search, type in "env", and choose "Edit the system environment variables".

7. Click the "Environment Variables..." button.

8. Set the following two environment variables:

    .. code-block:: text
    
       PROLIFERATE_ACCESS_KEY: <API key from step 5>
       PROLIFERATE_SECRET: <API secret from step 5>

9. Click OK to save variables.

10. Open a new Command Prompt (see step 1).

11. Test if the proliferate CLI has been successfully installed:

   .. code-block:: bash
   
        proliferate

    
MacOS
^^^^^^^^^^^^^^

1. Open the Terminal.

2. Make sure that pip is installed by running ``pip --version``. (To run a command, type the command in the Terminal window and press the return key.)

   If you get an error message, make sure that Python 3 and pip are installed. We recommend using the `Anaconda <https://www.anaconda.com/products/individual>`_ Python distribution.

3. Make sure that Git is installed by running ``git --version``. 

   If you get an error message, make sure that Git is installed. Look at the `git website <https://git-scm.com/download/mac>`_ for instructions on how to install git on MacOS. 

4. Install the command line interface by running the following two commands:

    .. code-block:: bash

        git clone https://github.com/sebschu/proliferate-client
        pip install -e proliferate-client
        
5. Go to https://proliferate.alps.science/admin/api and click on "Copy environment variables" to copy the environment variables. 

   (If you don't have a proliferate account yet, you can ceate one `here <https://proliferate.alps.science/admin/signup>`_.)
   
6. Open your ``.bash_profile`` script:

   .. code-block:: bash
   
       open ~/.bash_profile

7. Paste the environment variables into the end of this file and save it.

8. Load the environment variables:

   .. code-block:: bash
   
      source ~/.bash_profile

9. Test if the proliferate CLI has been successfully installed:

   .. code-block:: bash
   
        proliferate



Linux
^^^^^^^^^^^^^^

1. Open the Terminal.

2. Make sure that pip is installed by running ``pip --version``. (To run a command, type the command in the Terminal window and press the return key.)

   If you get an error message, make sure that Python 3 and pip are installed. We recommend using the `Anaconda <https://www.anaconda.com/products/individual>`_ Python distribution.

3. Make sure that Git is installed by running ``git --version``. 

   If you get an error message, make sure that Git is installed. Look at the `git website <https://git-scm.com/download/linux>`_ for instructions on how to install git on Linux. 

4. Install the command line interface by running the following two commands:

    .. code-block:: bash

        git clone https://github.com/sebschu/proliferate-client
        pip install -e proliferate-client
        
5. Go to https://proliferate.alps.science/admin/api and click on "Copy environment variables" to copy the environment variables. 

   (If you don't have a proliferate account yet, you can ceate one `here <https://proliferate.alps.science/admin/signup>`_.)
   
6. Open your ``.bashrc`` script with a text editor such as nano: (this is how the file is usually called on Ubuntu and Debian systems; on other distributions this file may have a different name such as `~/.profile`)

   .. code-block:: bash
   
       nano ~/.bashrc

7. Paste the environment variables into the end of this file and save it.

8. Load the environment variables:

   .. code-block:: bash
   
      source ~/.bashrc

9. Test if the proliferate CLI has been successfully installed:

   .. code-block:: bash
   
        proliferate


Managing experiments
--------------------

Posting an experiment
^^^^^^^^^^^^^

