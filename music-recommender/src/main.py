from src.recommender import load_songs, recommend_songs


def _print_recommendations(profile_name, user_profile, songs, weights=None, heading=None):
    """Print ranked recommendations for one profile."""
    print("\n==============================")
    if heading:
        print(heading)
    print(f"Profile: {profile_name}")
    print("User Profile:", user_profile)

    top_songs = recommend_songs(user_profile, songs, k=5, weights=weights)

    if not top_songs:
        print("No songs found.")
        return

    print("\nTop Recommendations:\n")

    for index, song in enumerate(top_songs, start=1):
        title = song.get("title", "Unknown Title")
        score = song.get("score", 0.0)
        reasons = song.get("reasons", [])
        reason_text = ", ".join(reasons) if reasons else "no matching reasons"

        print("-" * 40)
        print(f"{index}. {title} -- Score: {score:.2f}")
        print(f"   Reasons: {reason_text}")


def main():
    """Run baseline and experiment recommendation scenarios."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy", "energy": 0.7},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill", "energy": 0.2},
        ),
        (
            "Deep Intense Rock",
            {"genre": "rock", "mood": "intense", "energy": 0.9},
        ),
        (
            "Adversarial: High energy + sad",
            {"genre": "edm", "mood": "sad", "energy": 0.95},
        ),
        (
            "Adversarial: Unknown genre",
            {"genre": "opera", "mood": "happy", "energy": 0.4},
        ),
    ]

    for profile_name, user_profile in profiles:
        _print_recommendations(profile_name, user_profile, songs)

    # Experiment: down-weight genre and up-weight energy sensitivity.
    experiment_weights = {"genre": 0.5, "mood": 1.0, "energy": 2.0}
    _print_recommendations(
        "Experiment: Energy-Focused Pop",
        {"genre": "pop", "mood": "happy", "energy": 0.7},
        songs,
        weights=experiment_weights,
        heading="EXPERIMENT RUN (energy-focused weights)",
    )


if __name__ == "__main__":
    main()