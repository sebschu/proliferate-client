.. _cli-setup-instruction:

Setup instructions
=====================

Windows
---------------------

1. Download the `proliferate windows CLI <https://proliferate.alps.science/static/downloads/proliferate-client-windows.zip>`_.

2. Extract the downloaded folder somewhere on your computer. For example into your user directory.
        
3. Go to https://proliferate.alps.science/admin/api to look up the API key and API secret of your proliferate account. 

   (If you don't have a proliferate account yet, you can ceate one `here <https://proliferate.alps.science/admin/signup>`_.)

4. Open the Start Search, type in "env", and choose "Edit the system environment variables".

5. Click the "Environment Variables..." button.

6. Set the following two User variables:

    .. code-block:: text
    
       PROLIFERATE_ACCESS_KEY: <API key from step 3>
       PROLIFERATE_SECRET: <API secret from step 3>

7. Edit the ``Path`` variable and add the directory that you extracted in Step 2.

   For example, if you extracted the directory into your user directory 
   (and now have a folder ``proliferate`` in your user directory, add the following path
   to the ``Path`` variable:
   
   .. code-block:: text
   
       %USERPROFILE%\proliferate
      

8. Click OK to save variables.

9. Open the Command Prompt. (Open the Start Search, type in "cmd" and choose "Command Prompt".)

9. Test if the proliferate CLI has been successfully installed by running the following command: 
   (To run a command, type the command in the Command Prompt window and press the return key.)

   .. code-block:: bash
   
        proliferate


   You should see the following output:
    
   .. code-block:: bash
   
        usage: proliferate [-h]
                           {post,posthit,getresults,info,push,update,pull,clone} ...
                           label

        Interface with Proliferate.

        positional arguments:
          label                 You must have a label that corresponds to the
                                experiment you want to work with.This will be the
                                beginning of the name of the config file (everything
                                before the dot). [label].config.

        optional arguments:
          -h, --help            show this help message and exit

        subcommands:
          {post,posthit,getresults,info,push,update,pull,clone}
            post (posthit)      post new experiment
            getresults          download results (use --sandbox to download sandbox
                                results.)
            info                display details and status of experiment
            push (update)       update experiment on Proliferate server
            pull                download configuration from Proliferate server
            clone               clone experiment from Proliferate server

   .. note:: 
   
       You may get one or several notifications from Windows Defender when you
       first run proliferate. You can safely ignore these notifications.
   

MacOS
--------------------

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


   You should see the following output:
    
   .. code-block:: bash
   
        usage: proliferate [-h]
                           {post,posthit,getresults,info,push,update,pull,clone} ...
                           label

        Interface with Proliferate.

        positional arguments:
          label                 You must have a label that corresponds to the
                                experiment you want to work with.This will be the
                                beginning of the name of the config file (everything
                                before the dot). [label].config.

        optional arguments:
          -h, --help            show this help message and exit

        subcommands:
          {post,posthit,getresults,info,push,update,pull,clone}
            post (posthit)      post new experiment
            getresults          download results (use --sandbox to download sandbox
                                results.)
            info                display details and status of experiment
            push (update)       update experiment on Proliferate server
            pull                download configuration from Proliferate server
            clone               clone experiment from Proliferate server

 

Linux
-------------------------

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

   
   You should see the following output:
    
   .. code-block:: bash
   
        usage: proliferate [-h]
                           {post,posthit,getresults,info,push,update,pull,clone} ...
                           label

        Interface with Proliferate.

        positional arguments:
          label                 You must have a label that corresponds to the
                                experiment you want to work with.This will be the
                                beginning of the name of the config file (everything
                                before the dot). [label].config.

        optional arguments:
          -h, --help            show this help message and exit

        subcommands:
          {post,posthit,getresults,info,push,update,pull,clone}
            post (posthit)      post new experiment
            getresults          download results (use --sandbox to download sandbox
                                results.)
            info                display details and status of experiment
            push (update)       update experiment on Proliferate server
            pull                download configuration from Proliferate server
            clone               clone experiment from Proliferate server
