# coa-virtual-assistant

Repo for exports and other related files for the COA implementation of Watson Virtual Assistant

This virtual assistant is currently oriented around providing resident information for COVID-19 response efforts.

Although the Watson Virtual assistant has a pretty fleshed out GUI for managing instances, it lacks version control or revision history. However, it does allow for exporting of 'skills' to JSON files which we can then store and do version control/diff checking on.

The flow will be something like:

1. Watson JSONs live in this repo
1. that JSON file is imported into Watson and deployed
1. changes made in Watson are exported back to the Github repo and committed

- If recomendations from Watson are implemented, entries created, etc. inside Watson, an export will need be prepared and committed to the repo

- The JSON files in the repo could also be edited directly, if a change is committed to a given branch on the repo, than that file needs to be imported to watson

![strat](https://user-images.githubusercontent.com/10539855/79008780-bb9e3180-7b23-11ea-9e50-369264f2a778.png)

## What is here

- JSON exports of the assistant and it's associated skills
- code needed to embed the widget on a website

## How to run

[Poetry](https://python-poetry.org/docs/) was used to set up this project, highly recommended for easy dependency/environment management

1. Clone this repo
1. Install Poetry if you haven't
1. Browse to the 'skill-sync' folder
1. Run `poetry install`
1. Run `poetry run python export_skill.py`
1. If everything works, you should see a new file in the 'exports' folder

### Links, other resources

Project owners:

Eric Sherman
eric.sherman@austintexas.gov

#### Trello Boarrd

https://trello.com/b/pOMHcXEB/emerging-tech
