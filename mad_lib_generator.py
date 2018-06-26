"""
The Goal: Inspired by Summer Son's Mad Libs project(1) with Javascript. The
program will first prompt the user for a series of inputs a la Mad Libs. For
example, a singular noun, an adjective, etc. Then, once all the information
has been inputted, the program will take that data and place them into a
premade story template. You'll need prompts for user input, and to then print
out the full story at the end with the input included.

Concepts to keep in mind:
- Strings
- Variables
- Concatenation
- Print

1 http://suyeon-son.com/sandbox/mad-libs.html
"""


adjective = str(raw_input("Pick an adjective: "))
noun = str(raw_input("Pick a noun: "))
animal = str(raw_input("Pick an animal: "))
noise = str(raw_input("Pick a noise: "))

print("""
{adjective} Macdonald had a {noun}, E-I-E-I-O
and on that {noun} he had an {animal}, E-I-E-I-O
with a {noise} {noise} here
and a {noise} {noise} there,
here a {noise}, there a {noise},
everywhere a {noise} {noise},
{adjective} Macdonald had a {noun}, E-I-E-I-O.""".format(
    adjective=adjective, noun=noun, animal=animal, noise=noise))
