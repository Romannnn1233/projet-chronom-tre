import tkinter as tk
from stopwatch import Stopwatch

def main():
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
