from src.recommender import load_songs, recommend_songs


def main():
    songs = load_songs("data/songs.csv")

    profiles = [
        {"genre": "pop", "mood": "happy", "energy": 0.7},
        {"genre": "lofi", "mood": "chill", "energy": 0.2},
        {"genre": "rock", "mood": "intense", "energy": 0.9},
    ]

    for user_profile in profiles:
        print("\n==============================")
        print("User Profile:", user_profile)

        top_songs = recommend_songs(user_profile, songs, k=5)

        if not top_songs:
            print("No songs found.")
            continue

        print("\n🎵 Top Recommendations:\n")

        for index, song in enumerate(top_songs, start=1):
            title = song.get("title", "Unknown Title")
            score = song.get("score", 0.0)
            reasons = song.get("reasons", [])
            reason_text = ", ".join(reasons) if reasons else "no matching reasons"

            print("-" * 40)
            print(f"{index}. {title} -- Score: {score:.1f}")
            print(f"   Reasons: {reason_text}")


if __name__ == "__main__":
    main()