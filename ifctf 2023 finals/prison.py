#!/usr/bin/env python3

def main():
	locals = {'__builtins__': {'__build_class__': __build_class__,}}

	blacklist = [
		'\'', '"', '(', '[', '{', '=', 
		'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
		'True', 'False', 'None', '...', 
		'+', '-', '*', '/', '%', '<', '>', '&', '|', '^', '~',
	]

	code = input()
	if not code.isascii() or any(word in code for word in blacklist):
		print("Blacklisted word detected, exiting ...")
		exit(1)

	exec(code, locals)

if __name__ == '__main__':
	main()
