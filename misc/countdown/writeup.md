# Title

## Authors
- @felixc90

## Category
- Misc

## Description
Abiram, Felix and Paula have decided to host a new show called 3 out of 20
CompClub does Countdown and you have been invited to take part in the first
episode. There are two sections which you must complete.
Numbers Section:
Using the numbers 25, 1, 1, 3, 4, 2 only once with the basic order of operations addition, subtraction, multiplication, division, get as close as you can to the 
number 560.
Letters Section:
Find the English word that uses the most number of letters in the list [L, N, T,
E, I, E, R, H, A] where each letter is only used once.
The flag is in the format COMPCLUB{<WORD><NUMBER>} so if the correct word was
'example' and the closest number would be 570, then the flag would be
COMPCLUB{example570}.

## Difficulty
- Easy

## Points
60

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Use an anagram solver and maths.

### Walkthrough
1. Use an anagram solver to find the word heartline
2. (25 * 2 + 1) * (3 * 4 - 1) = 561

### Flag
`COMPCLUB{heartline561}`
</details>
