import tkinter as tk
from tkinter import ttk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Chronomètre")
        
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.create_widgets()

    def create_widgets(self):
        # Affichage du temps
        self.time_display = ttk.Label(self.root, text="00:00:00", font=('Arial', 40))
        self.time_display.grid(row=0, column=0, columnspan=2)

        # Bouton Démarrer
        self.start_button = ttk.Button(self.root, text="Démarrer", command=self.start)
        self.start_button.grid(row=1, column=0)

        # Bouton Arrêter
        self.stop_button = ttk.Button(self.root, text="Arrêter", command=self.stop)
        self.stop_button.grid(row=1, column=1)

        # Bouton Réinitialiser
        self.reset_button = ttk.Button(self.root, text="Réinitialiser", command=self.reset)
        self.reset_button.grid(row=1, column=2)

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.time_display.config(text=self.format_time(self.elapsed_time))
            self.root.after(50, self.update_time)

    def format_time(self, elapsed_time):
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_display.config(text="00:00:00")
