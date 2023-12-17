import functools

@functools.total_ordering
class Hand:
    CARDS_ORDER = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.hand_value = None
        self.bid = int(bid)
        # Calculate hand type:
        counts = {}
        for card in self.cards:
            counts[card] = counts.get(card, 0) + 1
        
        # Add the number of jokers to the most common card
        to_add = counts.get("J", 0)
        counts.pop("J", None)
        try:
            max_key = next(iter(counts))
            for key in counts:
                if counts[key] > counts[max_key]:
                    max_key = key
            counts[max_key] += to_add
        except StopIteration:  # J was the only card
            counts["J"] = to_add

        if len(counts) == 1:
            self.hand_value = 6
        elif len(counts) == 2:
            if set(counts.values()) == set([4, 1]):
                self.hand_value = 5
            elif set(counts.values()) == set([3, 2]):
                self.hand_value = 4
        elif len(counts) == 3:
            if set(counts.values()) == set([3, 1, 1]):
                self.hand_value = 3
            elif set(counts.values()) == set([2, 2, 1]):
                self.hand_value = 2
        elif len(counts) == 4:
            self.hand_value = 1
        elif len(counts) == 5:
            self.hand_value = 0

    def __eq__(self, other):
        if self.cards == other.cards:
            return True
        return False

    def __lt__(self, other):
        if self.hand_value < other.hand_value:
            return True
        elif self.hand_value == other.hand_value:
            for own_card, other_card in zip(self.cards, other.cards):
                if self.CARDS_ORDER.index(own_card) > self.CARDS_ORDER.index(other_card):
                    return True
                elif self.CARDS_ORDER.index(own_card) < self.CARDS_ORDER.index(other_card):
                    return False
        return False

    def __repr__(self):
        return f'Hand("{self.cards}", hand_value={self.hand_value}, bid={self.bid})'

if __name__ == "__main__":
    with open("inputs/day7_input.txt") as file:
        hands = [Hand(*line.strip().split(" ")) for line in file.readlines()]

    winnings = 0
    ranked = list(sorted(hands))
    for rank, hand in enumerate(ranked, start=1):
        winnings += rank * hand.bid
    print(ranked)
    print(winnings)