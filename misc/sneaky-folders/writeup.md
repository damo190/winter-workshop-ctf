# Title

## Authors
- @handle

## Category
- Misc

## Description
Felix has come up with an amazing way to organise his files and folders. He has
used ascii and binary to hide messages that he doesn't want others to see
and he only needs to remember a letter to find his hidden files. He has hidden 
a flag within in his folders and has been kind enough to give us his personal
key that he uses to remember where it is: 'c'. See if you can find the flag!

## Difficulty
- Medium

## Points
70

## Files
- filename: 'not suspicious folder.zip'

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Use the binary representation to traverse binary tree-like folders

### Walkthrough
1. The letter 'c' is represented as 01100011 in binary
2. By corresponding 'flag-in-here' folders to 1 and 'flag-not-in-here' folders to 0, we can traverse and find the flag

### Flag
`COMPCLUB{n!cE_b!N@rY_s3@RcH!n9_th3r3!!!}`
</details>
