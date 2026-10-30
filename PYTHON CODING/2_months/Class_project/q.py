import time

NO_OF_CHARS = 256

def horspool_shift_table(pat):
    m = len(pat)
    shift = [m] * NO_OF_CHARS
    for i in range(m - 1):
        shift[ord(pat[i])] = m - 1 - i
    return shift

def horspool_search_debug_with_time(txt, pat):
    n = len(txt)
    m = len(pat)
    shift = horspool_shift_table(pat)

    comparisons = 0
    shifts = 0
    matches = 0

    print("Text   :", txt)
    print("Pattern:", pat)
    print("\n--- Start Searching (Horspool) ---")

    start_time = time.perf_counter()  # ⏱️ start timer

    i = m - 1
    step = 1
    while i < n:
        shifts += 1
        print(f"\nStep {step}: Align pattern ending at text index {i}")
        print("Text   :", txt)
        print("Pattern:", " " * (i - m + 1) + pat)

        k = 0
        while k < m:
            comparisons += 1
            if pat[m - 1 - k] == txt[i - k]:
                print(f"  Match: pat[{m-1-k}]='{pat[m-1-k]}' == txt[{i-k}]='{txt[i-k]}'")
                k += 1
            else:
                print(f"  Mismatch: pat[{m-1-k}]='{pat[m-1-k]}' != txt[{i-k}]='{txt[i-k]}'")
                break

        if k == m:
            matches += 1
            print(f"✔ Pattern found at index {i - m + 1}")

        bad_char = txt[i]
        jump = shift[ord(bad_char)]
        print(f"  Bad char at text[{i}] = '{bad_char}', shifting by {jump}")
        i += jump
        step += 1

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
    horspool_search_debug_with_time(txt, pat)

if __name__ == '__main__':
    main()
