import csv

GENRE_MATCH_POINTS = 1.0
MOOD_MATCH_POINTS = 1.0
ENERGY_WEIGHT = 1.0


def _convert_value(key, value):
    """Convert CSV values to numeric types when needed."""
    if value is None:
        return ""

    cleaned = value.strip()

    if key == "tempo_bpm":
        try:
            return int(float(cleaned))
        except ValueError:
            return cleaned

    if key in {"energy"}:
        try:
            return float(cleaned)
        except ValueError:
            return cleaned

    return cleaned


def load_songs(file_path):
    """Load songs from CSV into a list of dictionaries."""
    songs = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            song = {}
            for key, value in row.items():
                song[key] = _convert_value(key, value)
            songs.append(song)

    return songs


def score_song(user_prefs, song, weights=None):
    """Score one song for a user profile and return reasons."""
    active_weights = {
        "genre": GENRE_MATCH_POINTS,
        "mood": MOOD_MATCH_POINTS,
        "energy": ENERGY_WEIGHT,
    }

    if weights:
        active_weights.update(weights)

    score = 0.0
    reasons = []

    preferred_genre = user_prefs.get("genre")
    song_genre = song.get("genre")
    if preferred_genre and song_genre and preferred_genre == song_genre:
        genre_points = active_weights["genre"]
        score += genre_points
        reasons.append(f"genre match (+{genre_points:.1f})")

    preferred_mood = user_prefs.get("mood")
    song_mood = song.get("mood")
    if preferred_mood and song_mood and preferred_mood == song_mood:
        mood_points = active_weights["mood"]
        score += mood_points
        reasons.append(f"mood match (+{mood_points:.1f})")

    user_energy = user_prefs.get("energy")
    song_energy = song.get("energy")
    if user_energy is not None and song_energy is not None:
        energy_similarity = max(0, 1 - abs(song_energy - user_energy))
        weighted_energy_similarity = energy_similarity * active_weights["energy"]
        score += weighted_energy_similarity
        reasons.append(f"similar energy ({weighted_energy_similarity:+.1f})")

    return score, reasons


def recommend_songs(user_prefs, songs, k, weights=None):
    """Rank songs by score and return the top-k matches."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song, weights=weights)

        scored_song = song.copy()
        scored_song["score"] = score
        scored_song["reasons"] = reasons

        scored_songs.append(scored_song)

    ranked_songs = sorted(
        scored_songs,
        key=lambda current_song: current_song["score"],
        reverse=True,
    )

    return ranked_songs[:k]
