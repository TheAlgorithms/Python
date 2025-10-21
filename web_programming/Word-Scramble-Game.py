# ...existing code...
"""
Word Scramble — interactive CLI game
Features:
 - Difficulty levels (easy / medium / hard)
 - Multiple rounds per game based on difficulty
 - Hint system (reveal a letter)
 - Scoring with time bonus
 - Persistent top-10 high scores in high_scores.json
 - Beginner-friendly, well-commented, no external dependencies
"""

import json
import random
import time
from pathlib import Path
from datetime import datetime

# Files (stored in the same folder)
DATA_DIR = Path(__file__).parent
HIGH_SCORES_FILE = DATA_DIR / "high_scores.json"
STATS_FILE = DATA_DIR / "stats.json"

# Simple embedded word list (can be extended)
WORD_LIST = [
    "planet", "python", "scramble", "library", "function", "variable",
    "keyboard", "monitor", "developer", "network", "package", "module",
    "algorithm", "debug", "database", "container", "virtual", "iterate",
    "compile", "syntax", "object", "inheritance", "interface", "performance",
    "encryption", "protocol", "bandwidth", "repository", "branch", "commit",
    "feature", "engine", "cursor", "iterator", "lambda", "generator",
    "concurrency", "thread", "process", "serializer", "message", "payload"
]

# Optional categories to make the game more interesting — each category is a small subset
CATEGORIES = {
    "general": WORD_LIST,
    "programming": [w for w in WORD_LIST if w in (
        "python","function","variable","module","algorithm","debug","compile",
        "object","inheritance","interface","repository","commit","lambda","generator",
        "concurrency","thread","process"
    )],
    "networking": [w for w in WORD_LIST if w in (
        "network","protocol","bandwidth","packet" )],
}

# New extended categories
ANIMALS = [
    "elephant", "tiger", "penguin", "giraffe", "dolphin", "kangaroo", "alligator",
    "cheetah", "hedgehog", "raccoon", "squirrel", "porcupine", "butterfly", "octopus",
    "hummingbird", "flamingo"
]

MOVIES = [
    "inception", "gladiator", "titanic", "avatar", "interstellar", "matrix", "casablanca",
    "goodfellas", "amadeus", "psycho", "rocky", "alien", "jaws"
]

FOODS = [
    "pizza", "sushi", "taco", "lasagna", "pancake", "risotto", "casserole", "burger",
    "cupcake", "avocado", "blueberry", "spaghetti", "chocolate"
]

# merge into categories dict
CATEGORIES["animals"] = ANIMALS
CATEGORIES["movies"] = MOVIES
CATEGORIES["foods"] = FOODS

# Configuration by difficulty
DIFFICULTIES = {
    "easy": {"rounds": 8, "removal_hint": 0, "multiplier": 1.0, "max_time": 30},
    "medium": {"rounds": 6, "removal_hint": 1, "multiplier": 1.5, "max_time": 25},
    "hard": {"rounds": 4, "removal_hint": 2, "multiplier": 2.0, "max_time": 20},
}


def load_high_scores():
    """Load high scores from disk; return list of dicts."""
    if HIGH_SCORES_FILE.exists():
        try:
            with HIGH_SCORES_FILE.open("r", encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return []
    return []


def save_high_scores(scores):
    """Save high scores to disk (keep only top 10)."""
    scores = sorted(scores, key=lambda s: s["score"], reverse=True)[:10]
    with HIGH_SCORES_FILE.open("w", encoding="utf-8") as fh:
        json.dump(scores, fh, indent=2)


def load_stats():
    """Load simple player stats (games_played, best_streak)."""
    if STATS_FILE.exists():
        try:
            with STATS_FILE.open("r", encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return {"games_played": 0, "best_streak": 0}
    return {"games_played": 0, "best_streak": 0}


def save_stats(stats):
    try:
        with STATS_FILE.open("w", encoding="utf-8") as fh:
            json.dump(stats, fh, indent=2)
    except Exception:
        pass


def show_high_scores():
    scores = load_high_scores()
    if not scores:
        print("\nNo high scores yet. Be the first!\n")
        return
    print("\nTop scores:")
    for i, s in enumerate(scores, 1):
        when = s.get("date", "")
        print(f"{i}. {s['name']} — {s['score']} pts  ({when})")
    print()


def scramble_word(word):
    """Return a scrambled version of word that's not identical to original if possible."""
    if len(set(word)) == 1:
        # all same letter (rare) — return as-is
        return word
    letters = list(word)
    scrambled = word
    # try multiple times to avoid returning the same word
    for _ in range(10):
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled
    return scrambled  # fallback


def color(text, code):
    """Lightweight colored output using ANSI codes. Works on modern terminals."""
    return f"\x1b[{code}m{text}\x1b[0m"


def compute_score(word, elapsed, difficulty):
    """Compute score for a correct guess."""
    base = len(word) * 10
    mult = DIFFICULTIES[difficulty]["multiplier"]
    max_time = DIFFICULTIES[difficulty]["max_time"]
    # time bonus scales with how quickly the player answers (0-20)
    time_bonus = max(0, int((max_time - min(elapsed, max_time)) / max_time * 20))
    return int(base * mult + time_bonus)


def play_round(word, difficulty):
    """Play one scramble round. Returns points earned (0 if failed/skip)."""
    max_time = DIFFICULTIES[difficulty]["max_time"]
    scrambled = scramble_word(word)
    hint_mask = ["_"] * len(word)
    revealed_indices = set()
    attempts = 0

    print("\nScrambled:", " ".join(scrambled))
    print(f"(Type your guess, or 'hint', 'skip', 'quit'. Time suggested: {max_time}s)\n")

    start = time.perf_counter()
    while True:
        attempts += 1
        guess = input("Your guess > ").strip().lower()
        elapsed = time.perf_counter() - start

        if guess == "quit":
            return "quit", 0
        if guess == "skip":
            print(f"Skipped. Answer was: {word}")
            return 0
        if guess == "hint":
            # reveal one unrevealed letter in correct position
            unrevealed = [i for i in range(len(word)) if i not in revealed_indices]
            if not unrevealed:
                print("All letters already revealed.")
            else:
                i = random.choice(unrevealed)
                revealed_indices.add(i)
                hint_mask[i] = word[i]
                print("Hint:", " ".join(hint_mask))
            continue
        # check answer
        if guess == word:
            points = compute_score(word, elapsed, difficulty)
            print(color(f"Correct! +{points} pts (time: {int(elapsed)}s, attempts: {attempts})", '32'))
            return points
        else:
            # small helpful feedback
            same_positions = sum(1 for a, b in zip(guess, word) if a == b)
            print(f"Not quite. {same_positions} letter(s) in the correct position. Try again.")


def pick_word_by_difficulty_and_category(difficulty, category=None):
    """Pick a word influenced by difficulty and optional category (longer words for harder)."""
    if category and category in CATEGORIES:
        pool = CATEGORIES[category]
    else:
        if difficulty == "easy":
            pool = [w for w in WORD_LIST if 4 <= len(w) <= 6]
        elif difficulty == "medium":
            pool = [w for w in WORD_LIST if 5 <= len(w) <= 8]
        else:
            pool = [w for w in WORD_LIST if len(w) >= 6]
    if not pool:
        pool = WORD_LIST
    return random.choice(pool)


def celebratory_art():
    art = [
        "\n  ★ Congratulations! ★\n",
        "\n  (\_/)",
        "\n  ( •_•)",
        "\n  / >💥 You did it!\n"
    ]
    print(color('\n'.join(art), '35'))


def play_game():
    print(color("WELCOME TO WORD SCRAMBLE", '36'))
    print(color("------------------------", '36'))
    # choose difficulty
    while True:
        diff = input("Choose difficulty (easy / medium / hard) [medium]: ").strip().lower() or "medium"
        if diff in DIFFICULTIES:
            break
        print("Invalid choice.")
    # choose optional category
    print("Available categories:", ', '.join(CATEGORIES.keys()))
    cat = input("Pick category (or press Enter for mixed): ").strip().lower() or None
    if cat and cat not in CATEGORIES:
        print("Unknown category, using mixed words.")
        cat = None

    rounds = DIFFICULTIES[diff]["rounds"]
    print(f"Starting {rounds} rounds on {diff} difficulty. Good luck!\n")

    total_score = 0
    streak = 0
    best_streak = 0
    stats = load_stats()

    for r in range(1, rounds + 1):
        print(f"=== Round {r}/{rounds} ===")
        word = pick_word_by_difficulty_and_category(diff, cat)
        result = play_round(word, diff)
        if isinstance(result, tuple) and result[0] == "quit":
            print("Quitting game early.")
            break
        points = result
        if points > 0:
            streak += 1
            best_streak = max(best_streak, streak)
            # combo bonus for streaks: +5% per consecutive correct (rounded)
            combo_bonus = int(points * (0.05 * (streak - 1))) if streak > 1 else 0
            if combo_bonus:
                print(color(f"Combo! +{combo_bonus} bonus points for a streak of {streak}", '33'))
            points += combo_bonus
            total_score += points
            celebratory_art()
        else:
            streak = 0

    print("\nGame over. Total score:", total_score)
    # update stats
    stats["games_played"] = stats.get("games_played", 0) + 1
    stats["best_streak"] = max(stats.get("best_streak", 0), best_streak)
    save_stats(stats)


def main_menu():
    while True:
        print("Word Scramble — Main Menu")
        print("1) Play")
        print("2) Show High Scores")
        print("3) About / Instructions")
        print("4) Quit")
        choice = input("Select [1-4] > ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            show_high_scores()
        elif choice == "3":
            print("\nInstructions:")
            print("- Guess the original word from the scrambled letters.")
            print("- Commands during a round: 'hint' (reveals one letter), 'skip', 'quit'.")
            print("- Faster correct answers score more points.")
            print("- High scores are saved locally in high_scores.json.\n")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Bye.")
