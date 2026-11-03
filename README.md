# Outfit-deck

Outfit Deck is an interactive Python application that recommends an outfit according to the user’s selected weather and occasion. It was created as part of a UTS Creative Coding project to explore how structured data, conditional logic and interface design can transform a personal wardrobe into an interactive recommendation system.

The project aims to reduce outfit decision fatigue through a simple and personalised experience using photographs from my own wardrobe.

Table of Contents

Features

Technologies

How It Works

Project Structure

Installation

How to Use the App

Editing the Outfit Data

Known Limitations

Future Development

Learning Resources

Author

Features

Filters outfits according to weather and occasion

Includes Hot, Mild, Cold and Rainy weather options

Includes University, Casual, Work and Night out occasions

Provides an Any option to browse a wider selection

Displays an outfit photograph and its matching categories

Includes Previous and Next navigation

Includes a Surprise Me button for random selection

Stores outfit information separately in an editable JSON file

Uses 12 original wardrobe photographs

Technologies

Outfit Deck was developed using:

Python 3

Tkinter for the graphical user interface

Pillow for loading and resizing images

JSON for storing outfit information

Visual Studio Code as the development environment

A Python virtual environment for managing dependencies

Tkinter is included with most Python installations. Pillow is the main external package required by the project.

How It Works

Each outfit is stored in outfits.json with four key pieces of information:

{
  "name": "Hot Casual Outfit",
  "image": "outfit_05.jpg",
  "weather": ["Hot"],
  "occasions": ["Casual"]
}

When the user selects a weather condition and occasion, the program retrieves both selections and checks them against every outfit in the dataset.

An outfit is added to the matches list only when both selected conditions are satisfied. Selecting Any allows that category to bypass its usual filtering condition. The program then displays the first matching outfit and resets the current index to zero.

Project Structure

Outfit-Deck/
├── app.py
├── outfits.json
├── requirements.txt
├── README.md
├── images/
│   ├── outfit_01.jpg
│   ├── outfit_02.jpg
│   ├── outfit_03.jpg
│   ├── ...
│   ├── outfit_12.jpg
│   └── app_preview.png
└── .venv/

File explanations

app.py creates the interface and controls filtering, image display and navigation.

outfits.json stores the name, image filename, weather and occasion categories for each outfit.

requirements.txt lists the external Python package required to run the application.

images/ contains the wardrobe photographs and application preview.

.venv/ stores the project’s local Python environment. This folder may not be uploaded to GitHub.

Installation

1. Download the project

Download the repository as a ZIP file and extract it, or clone it using Git:

git clone <repository-url>

Replace <repository-url> with the URL of this GitHub repository.

2. Open the project folder

Open the complete Outfit-Deck folder in Visual Studio Code.

3. Create a virtual environment

On macOS or Linux:

python3 -m venv .venv

On Windows:

python -m venv .venv

4. Activate the virtual environment

On macOS or Linux:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

5. Install the required package

python3 -m pip install -r requirements.txt

Windows users may need to enter:

python -m pip install -r requirements.txt

6. Run the application

On macOS or Linux:

python3 app.py

On Windows:

python app.py

How to Use the App

Select a weather condition from the Weather menu.

Select an activity from the Occasion menu.

Press Find My Outfit.

The program will display a photograph that matches both selections.

Use Previous and Next to move between available matches.

Press Surprise Me to display a random outfit from the current matches.

Note: Previous, Next and Surprise Me only create a visible change when more than one outfit matches the selected filters. If the app displays “Outfit 1 of 1,” the buttons are functioning, but there are no additional matching outfits to display. Select Any and Any to browse the complete wardrobe.

Application Preview



The example above shows Outfit Deck returning a Hot Casual recommendation based on the selected weather and occasion.

Editing the Outfit Data

New outfits can be added by placing a .jpg photograph in the images folder and adding a corresponding object to outfits.json.

For example:

{
  "name": "New Outfit",
  "image": "outfit_13.jpg",
  "weather": ["Mild", "Hot"],
  "occasions": ["University", "Casual"]
}

The image filename must exactly match the filename written in the JSON data. Capitalisation, punctuation and file extensions must remain consistent.

Each JSON object must be separated by a comma. The complete collection must remain enclosed in square brackets.

Known Limitations

Weather information must be selected manually.

The app does not currently connect to live weather data.

Outfit categories must be edited manually in outfits.json.

Some filter combinations return only one matching outfit.

Personal preferences such as colour, formality and recently worn items are not recorded.

Incorrect JSON punctuation or missing image files can prevent an outfit from loading.

Future Development

Possible future improvements include:

Connecting the app to a live weather API

Allowing users to upload photographs through the interface

Adding clearer feedback when only one outfit matches

Disabling navigation buttons when they are not required

Allowing users to save favourite outfits

Recording recently displayed or worn outfits

Adding more wardrobe categories and recommendations

Validating JSON data and missing image files automatically

Project Status

The core prototype is complete and functional. It successfully filters the wardrobe data, displays outfit photographs and provides navigation between matching results.

The project was produced for educational purposes as part of a Creative Coding assessment.

Learning Resources

The following resources supported the development and documentation of the project:

Sweigart, A. (2025). Automate the Boring Stuff with Python (3rd ed.). No Starch Press.

Matthes, E. (2023). Python Crash Course (3rd ed.). No Starch Press.

Python Programming MOOC – Defining Functions

The Python Coding Book – Dealing With Errors and Bugs

JSON Cheat Sheet

How to Write a Good README for Your GitHub Project

Author

Created by Lucinda Wright for the UTS Creative Coding subject, 2026.

All outfit photographs included in the project are original and were used for educational purposes.
