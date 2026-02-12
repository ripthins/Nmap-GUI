import subprocess
import sys
import tkinter as tk

def get_website():
    return input('Enter the website to ping: ')

def main():
	try:
		site = get_website()
		result = subprocess.run(['nmap', site], capture_output=True, text=True)
		print(result.stdout)
		if result.stderr:
			print(result.stderr, file=sys.stderr)
	except FileNotFoundError:
		print('nmap not found. Install nmap and ensure it is on your PATH.', file=sys.stderr)

if __name__ == '__main__':
	main()