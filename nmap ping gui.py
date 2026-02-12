import subprocess
import sys
import tkinter as tk

def get_website():
    return input('Enter the website to ping: ')

def get_tool_choice():
    print('Choose a tool:')
    print('1. ping')
    print('2. nmap')
    choice = input('Enter your choice (1 or 2): ')
    return 'ping' if choice == '1' else 'nmap'

def main():
	try:
		site = get_website()
		tool = get_tool_choice()
		
		if tool == 'ping':
			result = subprocess.run(['ping', site], capture_output=True, text=True)
		else:
			result = subprocess.run(['nmap', site], capture_output=True, text=True)
		
		print(result.stdout)
		if result.stderr:
			print(result.stderr, file=sys.stderr)
	except FileNotFoundError:
		print(f'{tool} not found. Install {tool} and ensure it is on your PATH.', file=sys.stderr)

if __name__ == '__main__':
	main()
