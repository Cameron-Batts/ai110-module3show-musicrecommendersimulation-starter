"""Run the music recommender with three different taste profiles."""

from pathlib import Path
from src.recommender import load_songs, recommend_songs


def main() -> None:
    """Load the catalog and print explained recommendations for each profile."""
    csv_path = Path(__file__).resolve().parents[1] / "data" / "songs.csv"
    songs = load_songs(csv_path)
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
        },
    }

    for name, preferences in profiles.items():
        print(f"\nProfile: {name}")
        print(f"Preferences: {preferences}\n")

        recommendations = recommend_songs(preferences, songs, k=5)

        for rank, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"{rank}. {song['title']} | Score: {score:.2f}")
            print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()
