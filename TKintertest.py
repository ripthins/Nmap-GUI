import subprocess
import sys
import tkinter as tk
from tkinter import scrolledtext, messagebox

def run_scan():
    site = entry.get().strip()

    if not site:
        messagebox.showwarning("Input Error", "Please enter a website or IP.")
        return

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, f"Scanning {site}...\n\n")

    try:
        result = subprocess.run(
            ['nmap', site],
            capture_output=True,
            text=True
        )

        output_box.insert(tk.END, result.stdout)

        if result.stderr:
            output_box.insert(tk.END, "\nErrors:\n")
            output_box.insert(tk.END, result.stderr)

    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "nmap not found.\nInstall nmap and ensure it is on your PATH."
        )

# Create main window
root = tk.Tk()
root.title("Nmap Scanner")
root.geometry("700x500")

# Input Label
label = tk.Label(root, text="website") # Change the label text to "website"
label.pack(pady=5)

# Entry box
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Scan Button
scan_button = tk.Button(root, text="Scan", command=run_scan)
scan_button.pack(pady=10)

# Output box (scrollable)
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD)
output_box.pack(expand=True, fill="both", padx=10, pady=10)

# Run GUI
root.mainloop()