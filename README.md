# Paper Collecter

## What is this?
This is a paper collector to collect a list of journal papers from good venues.

## Why do I need this?
Previously I use RSS/Researcher-app to get the updated list of paper, but they have certain drawbacks. So I want to design my own.

## Dependency
run the following for python dependency.
```
python -m pip install -r requirements.txt
```

## How do I use this?
Run the following script to collect the data, which is saved to the folder meta/
```
python collect.py
```
Then run the following script to convert the metadata to `papers.md` file for reading.
```
python convert.py
```

## Folder structure
meta/: store the metadata of the collected papers.
donelist.txt: a list of DOIs that I have finished reading or not interested.

## Name shortcut
- TS: Transportation Science
- OR: Operations Research
- TITS: Transaction on Intelligent Transportation System
- TRB: Transportation Research Part B