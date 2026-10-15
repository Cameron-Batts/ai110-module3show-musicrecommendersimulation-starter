# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Baseline results for three user profiles.

```text
Loaded songs: 18

Profile: High-Energy Pop
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8}

1. Sunrise City | Score: 3.98
   Because: genre match (+2.00); mood match (+1.00); energy similarity (+0.98)
2. Neon Heartbreak | Score: 2.94
   Because: genre match (+2.00); energy similarity (+0.94)
3. Gym Hero | Score: 2.87
   Because: genre match (+2.00); energy similarity (+0.87)
4. Rooftop Lights | Score: 1.96
   Because: mood match (+1.00); energy similarity (+0.96)
5. Midnight Verse | Score: 0.99
   Because: energy similarity (+0.99)

Profile: Chill Lofi
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35}

1. Library Rain | Score: 4.00
   Because: genre match (+2.00); mood match (+1.00); energy similarity (+1.00)
2. Midnight Coding | Score: 3.93
   Because: genre match (+2.00); mood match (+1.00); energy similarity (+0.93)
3. Focus Flow | Score: 2.95
   Because: genre match (+2.00); energy similarity (+0.95)
4. Spacewalk Thoughts | Score: 1.93
   Because: mood match (+1.00); energy similarity (+0.93)
5. Coffee Shop Stories | Score: 0.98
   Because: energy similarity (+0.98)

Profile: Deep Intense Rock
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9}

1. Storm Runner | Score: 3.99
   Because: genre match (+2.00); mood match (+1.00); energy similarity (+0.99)
2. Electric Grief | Score: 2.96
   Because: genre match (+2.00); energy similarity (+0.96)
3. Gym Hero | Score: 1.97
   Because: mood match (+1.00); energy similarity (+0.97)
4. Brass Parade | Score: 0.98
   Because: energy similarity (+0.98)
5. Neon Heartbreak | Score: 0.96
   Because: energy similarity (+0.96)
```


## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



