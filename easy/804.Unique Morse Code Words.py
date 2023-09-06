# https://leetcode.com/problems/unique-morse-code-words/

from typing import List

def uniqueMorseRepresentations(words: List[str]) -> int:
    MORSE = {
		'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
		'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
		'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
		'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..',
	}

    return len(set(''.join(map(MORSE.get, word)) for word in words))


assert uniqueMorseRepresentations(["gin","zen","gig","msg"]) == 2
assert uniqueMorseRepresentations(["a"]) == 1
