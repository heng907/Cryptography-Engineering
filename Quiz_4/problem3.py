import random
from collections import defaultdict

# Define the naive shuffle algorithm
def naive_shuffle(cards):
    for i in range(len(cards)):
        n = random.randint(0, len(cards) - 1)
        cards[i], cards[n] = cards[n], cards[i]
    return cards

# Define the Fisher-Yates shuffle algorithm
def fisher_yates_shuffle(cards):
    for i in range(len(cards) - 1, 0, -1):
        n = random.randint(0, i)
        cards[i], cards[n] = cards[n], cards[i]
    return cards

# Function to simulate shuffling a million times and collect results
def simulate_shuffling():
    naive_results = defaultdict(int)
    fy_results = defaultdict(int)

    for _ in range(1000000):  # Run the simulation a million times
        # Naive shuffle
        deck = [1, 2, 3, 4]
        shuffled_deck = naive_shuffle(deck.copy())
        naive_results[tuple(shuffled_deck)] += 1

        # Fisher-Yates shuffle
        deck = [1, 2, 3, 4]
        shuffled_deck = fisher_yates_shuffle(deck.copy())
        fy_results[tuple(shuffled_deck)] += 1

    return naive_results, fy_results

# Execute the simulation
naive_outcomes, fy_outcomes = simulate_shuffling()

# Output the results
print("Naive algorithm results:")
for outcome, count in sorted(naive_outcomes.items()):
    print(f"{list(outcome)}: {count}")
    naive = 0
    naive = naive + count
naive % 24
print("The average number of suffle:", naive)
print("\nFisher-Yates shuffle results:")
for outcome, count in sorted(fy_outcomes.items()):
    print(f"{list(outcome)}: {count}")
    fy = 0
    fy = fy + count
fy % 24
print("The average number of suffle:", fy)