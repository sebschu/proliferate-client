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


## Running an experiment

1. Create an experiment on [Prolific](https://app.prolific.co) and copy the completion URL.

2. In a new folder, create a file called `lacroix.config` with the following contents:

    ```
    {
      "name": "LaCroix study",
      "notes": "a study about LaCroix flavors",
      "completion_URL": "<INSERT COMPLETION URL HERE>",
      "conditions": [
        {
          "name": "regular",
          "experiment_URL": "https://stanford.edu/~sebschu/experiments/prolific-tutorial/experiment-cond-regular.html",
          "participants": 1
        },
        {
          "name": "tall",
          "experiment_URL": "https://stanford.edu/~sebschu/experiments/prolific-tutorial/experiment-cond-tall.html",
          "participants": 1
        }
      ]
    }
    ```
    (Make sure to paste your completion URL where it says `<INSERT COMPLETION URL HERE>`!)
    
    This will create a new experiment with two conditions called `regular` and `tall` with assignments for one participant each.
   
3. Post experiment

    ```
    proliferate post lacroix
    ```

4. Copy the "sandbox URL" into the Prolific experiment and make sure to check "I'll use URL parameters".

5. Test the experiment by clicking on Preview.

6. Complete the experiment. At the end you should be redirected to a Prolific URL.

7. Download the data.

   ```
   proliferate getresults --sandbox lacroix
   ```
   
   (The `--sandbox` parameter telles proliferate to download the sandbox data. When you are running an actual study, you can omit the `--sandbox` parameter to download participant's data.)
   

## Modifying an existing MTurk experiment to work with Proliferate

1. Include this snippet in `<head>` block of your experiment:
    ```
    <script src="https://proliferate.alps.science/static/js/proliferate.js"></script>
    ```
    
2. If you are using `mmturkey.js`, remove the `<script>` tag that imports it.

3. At the end of the experiment call `proliferate.submit(data)` where `data` is an object with participants' responses and any other information you want to record.

    If you are using the submiterator templates, this means replacing the following line with `proliferate.submit(data);`:
    
    ```
    setTimeout(function() {turk.submit(exp.data);}, 1000);
    ```
    
4. Optional but recommended

    1. Remove uniqueturker or any scripts like that — they won’t work and are not necessary.
    
    2. Participants on Prolific may not know what a HIT is. Use Prolific-lingo instead:
    
        | MTurk | Prolific  |
        |-------|-----------|
        | HIT   | Requester |    
        | Requester   | Researcher |    
        | Worker/Turker   | Participant |  



   
