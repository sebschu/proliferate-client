# Proliferate CLI client

A tool for managing experiments on [Proliferate](https://proliferate.alps.science). This tool makes it easy to create new experiments to be published on [Prolific](https://prolific.co) and to download data.

The behavior is similar to various versions of [Submiterator](https://github.com/sebschu/Submiterator) but is intended to be used with Proliferate and Prolific.

## Installation



You can install the package using pip:

```
git clone https://github.com/sebschu/proliferate-client
pip install -e proliferate-client/
```

Add environment variables in your Bash (or other shell) profile (e.g., `~/.bash_profile` on most Macs or `~/.profile` on Ubuntu and Debian). Add the following lines:

```
# PROLIFERATE
export PROLIFERATE_ACCESS_KEY="<API_ACCESS_KEY>"
export PROLIFERATE_SECRET="<API_SECRET>"
```

After adding those lines, make sure to run `source ~/.bash_profile` (or the equivalent file on other systems) to apply the changes you made.

## How to use proliferate

To create an experiment, first setup the config file. 


Give this config file a unique label as its name: `[LABEL].config`.


```
{
  "name": "Example experiment",
  "notes": "Something I want to remember about the example experiment",
  "completion_URL": "https://app.prolific.co/submissions/complete?cc=<COMPLETION_URL>",
  "conditions": [
    {
      "name": "condition1",
      "experiment_URL": "https://path.to.my.experiment/condition1",
      "participants": 10
    },
    {
      "name": "condition2",
      "experiment_URL": "https://path.to.my.experiment/condition2",
      "participants": 10
    }
  ]
}
```

Once you have setup the config file run the following command in the terminal:

```
proliferate posthit [LABEL]
```

Then publish the experiment on Prolific. Once the experiment has been published, you can monitor the progress with the following command:

```
proliferate info [LABEL]
```

And then when you want to get the results:


```
proliferate getresults [LABEL]
```
