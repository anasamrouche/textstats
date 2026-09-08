def word_count(text: str) -> int:
    """Number of whitespace-separated tokens in `text`."""
    split_text = text.split(" ")
    return len(split_text)


def char_frequencies(text: str) -> dict[str, int]:
    """Count of each character, ignoring whitespace and case."""
    insensitive_text = text.lower()
    char_count = {}
    for char in insensitive_text:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count


def longest_word(text: str) -> str:
    """The longest token. Raises ValueError on empty input."""
