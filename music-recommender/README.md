# Music Recommender Simulation

A simple CLI-first music recommender that scores songs by matching user preferences against song features.

## Features Used

- genre
- mood
- energy

## How It Works

1. Load songs from `data/songs.csv`.
2. Score each song using weighted rules:
	- genre match
	- mood match
	- energy similarity
3. Rank songs from highest to lowest score.
4. Print top recommendations with score reasons.

## Run

```bash
cd music-recommender
python -m src.main
```
