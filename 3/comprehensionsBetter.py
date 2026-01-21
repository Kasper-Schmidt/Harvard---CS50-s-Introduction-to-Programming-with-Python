import re

def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    counts = {word: lowercase_words.count(word) for word in lowercase_words}
  
    save_counts(counts)




def get_words(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    return re.findall(r"[A-Za-zÆØÅæøå0-9]+", text)


def save_counts(counts: dict[str, int], out_filename: str = "counts.txt") -> None:
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))

    with open(out_filename, "w", encoding="utf-8") as f:
        for word, count in items:
            f.write(f"{word}\t{count}\n")




main()