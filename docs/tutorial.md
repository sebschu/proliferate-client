# Proliferate tutorial

## Installation

1. Open Terminal/command line

2. Run
    ```
    git clone https://github.com/sebschu/proliferate-client
    pip install -e proliferate-client
    ```
### Look up proliferate credentials

Go to: https://proliferate.alps.science/admin/api

### Setup environment variables

__Windows__

1. Open the Start Search, type in "env", and choose "Edit the system environment variables".

2. Click the "Environment Variables..." button.

3. Set the following two environment variables:
  
    1. `PROLIFERATE_ACCESS_KEY`:  `<API key from proliferate>`
    2. `PROLIFERATE_SECRET`: `<API secret from proliferate>`

4. Click OK to save variables.

5. Open a new command line window.

__MacOS/Linux__

1. Open the file `~/.bash_profile` (on most Macs) or `~/.profile` or `~/.bashrc` (on most Linux systems).

2. Click "Copy environment variables" at https://proliferate.alps.science/admin/api .

3. Paste the environment variables at the end of `~/.bash_profile` (or whatever your profile file is called) and save the file.

4. Run the following command:

    ```
      source ~/.bash_profile
    ```
    (or `source ` whatever the profile file is called.)
  
### Test proliferate

1. Run
    ```
    proliferate
    ```
 
2. You should see the following output:

   ```
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
   ```
