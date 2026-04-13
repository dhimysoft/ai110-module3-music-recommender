# Model Card: VibeFinder 1.0

## Model Name
VibeFinder 1.0

## Goal / Task
This model suggests songs from a small catalog by comparing user preferences to song attributes. It predicts a ranked list of tracks most likely to match a user's desired vibe.

## Data Used
- Dataset size: 18 songs.
- Source: data/songs.csv.
- Features available: title, genre, mood, energy, tempo_bpm.
- Features currently used for scoring: genre, mood, energy.
- Limits: small catalog, no artist popularity, no user history, no collaborative data.

## Algorithm Summary
The recommender gives points for feature matches.
- Genre match: +1.0.
- Mood match: +1.0.
- Energy similarity: max(0, 1 - absolute energy gap).

Every song receives a total score plus reason strings. Songs are then sorted from highest to lowest score, and the top 5 are returned.

## Observed Behavior / Biases
The model tends to prefer songs that share the same genre because exact matching adds guaranteed points. This can reduce diversity and form a small filter bubble around one genre. Songs with uncommon moods or genres in the dataset may be disadvantaged. The model also depends heavily on energy scale alignment, which can over-reward numerically close songs even if they are stylistically different.

## Evaluation Process
I tested five profiles:
- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Adversarial: High energy + sad
- Adversarial: Unknown genre

I also ran a sensitivity experiment by changing weights:
- genre: 1.0 -> 0.5
- mood: 1.0 -> 1.0
- energy multiplier: 1.0 -> 2.0

Main finding: the energy-focused setup increased ranking of songs close in energy even when genre mismatch existed.

## Intended Use
- Educational demonstration of recommendation logic.
- Small offline simulations and explainable ranking demos.
- Intro-level experiments with feature weighting.

## Non-Intended Use
- Production recommendation for real users.
- High-stakes personalization decisions.
- Fairness-critical applications where demographic impacts must be audited.

## Ideas For Improvement
1. Add collaborative filtering signals from user interaction logs.
2. Introduce diversity constraints so top results are not dominated by one genre.
3. Include additional features (danceability, acousticness, popularity, recency) and tune weights with data.

## Personal Reflection
My biggest learning moment was seeing how a tiny set of simple rules can still feel like meaningful personalization. AI assistance was useful for code structure and debugging, but I had to manually verify weights and output behavior because plausible code is not always correct for my intent. I was surprised that changing only one weight (energy) significantly shifted rankings, which made the model feel both powerful and fragile. If I extend this project, I would add collaborative signals and a diversity-aware ranking stage so recommendations stay relevant without becoming repetitive.
