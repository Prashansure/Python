import time

NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    badChar = [-1] * NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar

def search(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0

    comparisons = 0
    shifts = 0
    matches = 0

    start_time = time.perf_counter()  # ⏱️ start timer

    while s <= n - m:
        shifts += 1
        print("\n--- New shift s =", s, "---")
        j = m - 1

        while j >= 0 and pat[j] == txt[s + j]:
            comparisons += 1
            print(f"Match: pat[{j}] = '{pat[j]}' == txt[{s + j}] = '{txt[s + j]}'")
            j -= 1

        if j < 0:
            matches += 1
            print("✔ Pattern found at shift =", s)
            if s + m < n:
                shift = m - badChar[ord(txt[s + m])]
            else:
                shift = 1
            print("Shifting pattern by", shift)
            s += shift
        else:
            comparisons += 1
            print(f"✖ Mismatch: pat[{j}] = '{pat[j]}' != txt[{s + j}] = '{txt[s + j]}'")
            bc = badChar[ord(txt[s + j])]
            shift = max(1, j - bc)
            print(f"Bad char '{txt[s + j]}' last seen in pattern at index {bc}")
            print("Shifting pattern by", shift)
            s += shift

    end_time = time.perf_counter()  # ⏱️ end timer
    elapsed = end_time - start_time

    print("\n--- Stats ---")
    print("Total shifts (alignments tried):", shifts)
    print("Total character comparisons:", comparisons)
    print("Total matches found:", matches)
    print("Time taken (seconds):", elapsed)

def main():
    txt = input("Enter text: ")
    pat = input("Enter pattern: ")
    search(txt, pat)

if __name__ == '__main__':
    main()
