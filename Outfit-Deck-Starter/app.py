"""Outfit Deck - a beginner-friendly Python/Tkinter prototype."""

import json
import random
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageTk


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "outfits.json"
IMAGE_DIR = BASE_DIR / "images"

APP_BG = "#F7F0F3"
CARD_BG = "#FFFDFE"
TEXT = "#2D2529"
ACCENT = "#B85C7A"
ACCENT_DARK = "#873F59"
MUTED = "#75666D"


class OutfitDeckApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Outfit Deck")
        self.root.geometry("920x760")
        self.root.minsize(820, 700)
        self.root.configure(bg=APP_BG)

        self.outfits = self.load_outfits()
        self.matches = list(self.outfits)
        self.current_index = 0
        self.current_photo = None

        self.weather_var = tk.StringVar(value="Any")
        self.occasion_var = tk.StringVar(value="Any")

        self.build_interface()
        self.show_current_outfit()

    def load_outfits(self):
        """Read the editable outfit list from outfits.json."""
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                outfits = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Missing file", "outfits.json could not be found.")
            self.root.destroy()
            return []
        except json.JSONDecodeError:
            messagebox.showerror(
                "Formatting problem",
                "outfits.json contains a formatting error. Check commas and quotation marks.",
            )
            self.root.destroy()
            return []

        return outfits

    def build_interface(self):
        """Create the visible parts of the application."""
        header = tk.Frame(self.root, bg=APP_BG)
        header.pack(fill="x", padx=36, pady=(24, 10))

        tk.Label(
            header,
            text="OUTFIT DECK",
            font=("Helvetica", 28, "bold"),
            fg=TEXT,
            bg=APP_BG,
        ).pack()

        tk.Label(
            header,
            text="Choose the weather and occasion, then let your wardrobe decide.",
            font=("Helvetica", 13),
            fg=MUTED,
            bg=APP_BG,
        ).pack(pady=(5, 0))

        filter_frame = tk.Frame(self.root, bg=APP_BG)
        filter_frame.pack(pady=10)

        self.add_dropdown(
            filter_frame,
            label="Weather",
            variable=self.weather_var,
            values=["Any", "Hot", "Mild", "Cold", "Rainy"],
            column=0,
        )
        self.add_dropdown(
            filter_frame,
            label="Occasion",
            variable=self.occasion_var,
            values=["Any", "University", "Casual", "Work", "Night out"],
            column=1,
        )

        tk.Button(
            filter_frame,
            text="Find my outfit",
            command=self.find_matches,
            font=("Helvetica", 12, "bold"),
            fg="white",
            bg=ACCENT,
            activebackground=ACCENT_DARK,
            activeforeground="white",
            relief="flat",
            padx=22,
            pady=10,
            cursor="hand2",
        ).grid(row=1, column=2, padx=12, pady=(2, 0))

        card = tk.Frame(
            self.root,
            bg=CARD_BG,
            highlightbackground="#E5D4DB",
            highlightthickness=1,
        )
        card.pack(fill="both", expand=True, padx=55, pady=12)

        self.image_label = tk.Label(card, bg=CARD_BG)
        self.image_label.pack(pady=(20, 12))

        self.name_label = tk.Label(
            card,
            text="",
            font=("Helvetica", 21, "bold"),
            fg=TEXT,
            bg=CARD_BG,
        )
        self.name_label.pack()

        self.tags_label = tk.Label(
            card,
            text="",
            font=("Helvetica", 12),
            fg=MUTED,
            bg=CARD_BG,
        )
        self.tags_label.pack(pady=(5, 2))

        self.counter_label = tk.Label(
            card,
            text="",
            font=("Helvetica", 11),
            fg=MUTED,
            bg=CARD_BG,
        )
        self.counter_label.pack(pady=(0, 12))

        nav = tk.Frame(card, bg=CARD_BG)
        nav.pack(pady=(0, 18))

        self.make_nav_button(nav, "← Previous", self.previous_outfit).grid(
            row=0, column=0, padx=7
        )
        self.make_nav_button(nav, "Surprise me", self.random_outfit).grid(
            row=0, column=1, padx=7
        )
        self.make_nav_button(nav, "Next →", self.next_outfit).grid(
            row=0, column=2, padx=7
        )

        tk.Label(
            self.root,
            text="",
            font=("Helvetica", 10),
            fg=MUTED,
            bg=APP_BG,
        ).pack(pady=(0, 16))

    def add_dropdown(self, parent, label, variable, values, column):
        group = tk.Frame(parent, bg=APP_BG)
        group.grid(row=0, column=column, rowspan=2, padx=9)

        tk.Label(
            group,
            text=label,
            font=("Helvetica", 11, "bold"),
            fg=TEXT,
            bg=APP_BG,
        ).pack(anchor="w", pady=(0, 4))

        dropdown = ttk.Combobox(
            group,
            textvariable=variable,
            values=values,
            state="readonly",
            width=16,
            font=("Helvetica", 12),
        )
        dropdown.pack()

    def make_nav_button(self, parent, text, command):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 11),
            fg=ACCENT_DARK,
            bg="#F4E6EB",
            activebackground="#EBCFD9",
            relief="flat",
            padx=16,
            pady=8,
            cursor="hand2",
        )

    def find_matches(self):
        """Filter outfits using the selected weather and occasion."""
        weather = self.weather_var.get()
        occasion = self.occasion_var.get()

        self.matches = [
            outfit
            for outfit in self.outfits
            if (weather == "Any" or weather in outfit["weather"])
            and (occasion == "Any" or occasion in outfit["occasions"])
        ]

        if not self.matches:
            messagebox.showinfo(
                "No match yet",
                "No outfits match both choices. Try changing one of the filters.",
            )
            self.matches = list(self.outfits)

        self.current_index = 0
        self.show_current_outfit()

    def show_current_outfit(self):
        if not self.matches:
            return

        outfit = self.matches[self.current_index]
        self.current_photo = ImageTk.PhotoImage(self.load_image(outfit))
        self.image_label.configure(image=self.current_photo)
        self.name_label.configure(text=outfit["name"])
        self.tags_label.configure(
            text=f"Weather: {', '.join(outfit['weather'])}  •  "
            f"Occasion: {', '.join(outfit['occasions'])}"
        )
        self.counter_label.configure(
            text=f"Outfit {self.current_index + 1} of {len(self.matches)}"
        )

    def load_image(self, outfit):
        """Load an outfit photo or create a placeholder when it is missing."""
        image_path = IMAGE_DIR / outfit["image"]

        if image_path.exists():
            try:
                image = Image.open(image_path)
                image = ImageOps.exif_transpose(image).convert("RGB")
                image.thumbnail((430, 430), Image.Resampling.LANCZOS)
                canvas = Image.new("RGB", (430, 430), "#EFE7EA")
                x = (430 - image.width) // 2
                y = (430 - image.height) // 2
                canvas.paste(image, (x, y))
                return canvas
            except OSError:
                pass

        placeholder = Image.new("RGB", (430, 430), "#EADDE2")
        draw = ImageDraw.Draw(placeholder)
        try:
            title_font = ImageFont.truetype("Arial.ttf", 30)
            small_font = ImageFont.truetype("Arial.ttf", 18)
        except OSError:
            title_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        title = outfit["name"]
        subtitle = f"Add {outfit['image']} to the images folder"
        title_box = draw.textbbox((0, 0), title, font=title_font)
        subtitle_box = draw.textbbox((0, 0), subtitle, font=small_font)
        draw.text(
            ((430 - (title_box[2] - title_box[0])) / 2, 180),
            title,
            fill=ACCENT_DARK,
            font=title_font,
        )
        draw.text(
            ((430 - (subtitle_box[2] - subtitle_box[0])) / 2, 230),
            subtitle,
            fill=MUTED,
            font=small_font,
        )
        return placeholder

    def next_outfit(self):
        if self.matches:
            self.current_index = (self.current_index + 1) % len(self.matches)
            self.show_current_outfit()

    def previous_outfit(self):
        if self.matches:
            self.current_index = (self.current_index - 1) % len(self.matches)
            self.show_current_outfit()

    def random_outfit(self):
        if self.matches:
            self.current_index = random.randrange(len(self.matches))
            self.show_current_outfit()


if __name__ == "__main__":
    window = tk.Tk()
    app = OutfitDeckApp(window)
    window.mainloop()
