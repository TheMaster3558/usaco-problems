from collections import Counter

n = int(input())
flats = input()
total = len(set(flats))

pokemons = Counter()
left, right = 0, 0
prev_left, prev_right = 0, -1
best = 10 ** 9

while left < n and right < n:
    if prev_right < right:
        pokemons[flats[right]] += 1
    elif prev_left < left:
        pokemons[flats[prev_left]] -= 1
        if pokemons[flats[prev_left]] == 0:
            del pokemons[flats[prev_left]]

    prev_left, prev_right = left, right

    if len(pokemons) < total:
        right += 1
    else:
        best = min(best, right - left + 1)
        left += 1



print(best)
