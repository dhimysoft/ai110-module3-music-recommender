# Reflection Notes

## Profile Pair Comparisons

1. High-Energy Pop vs Chill Lofi
The pop profile surfaces brighter and faster tracks because its target energy (0.7) is much higher than lofi (0.2). The lofi profile consistently pulls low-energy songs like Coffee Rain and Slow Drift, which matches the intended calm vibe.

2. High-Energy Pop vs Deep Intense Rock
Both prefer medium-high to high energy songs, but pop leans toward happy tracks while rock/intense brings in heavier songs like Broken Amplifier and Iron Thunder. This makes sense because genre and mood constraints separate "danceable bright" from "aggressive powerful" outcomes.

3. Chill Lofi vs Deep Intense Rock
These two profiles produce the strongest contrast: lofi gets low-tempo, low-energy tracks while intense rock gets high-energy tracks near 0.9. The split validates that the energy feature has meaningful control over ranking direction.

## Additional Observation
When genre is unknown (opera), the model falls back to mood plus energy. This is useful for robustness, but it also shows the system cannot infer cross-genre taste without richer features.
