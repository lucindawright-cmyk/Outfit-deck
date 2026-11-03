# Outfit Deck Starter Project

Outfit Deck is a small Python desktop application that suggests outfits from your own wardrobe based on the selected weather and occasion.

## What is already included

- Weather and occasion dropdown menus
- A button that filters the outfits
- Previous, next and random outfit buttons
- Twelve editable outfit entries
- Automatic image resizing
- Placeholder cards when a photograph has not been added yet

## What you need to install on a Mac

1. Python 3 from https://www.python.org/downloads/macos/
2. Visual Studio Code from https://code.visualstudio.com/download
3. The official Microsoft Python extension inside Visual Studio Code

## First-time setup

1. Unzip this project folder.
2. Open Visual Studio Code.
3. Select **File > Open Folder** and choose `outfit-deck-starter`.
4. In Visual Studio Code, select **Terminal > New Terminal**.
5. Type the following and press Return:

   ```bash
   python3 -m venv .venv
   ```

6. Then type:

   ```bash
   source .venv/bin/activate
   ```

7. Then install Pillow:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

8. Run the app:

   ```bash
   python3 app.py
   ```

## Add your photographs

1. Take or choose twelve outfit photographs.
2. Rename them `outfit_01.jpg` through to `outfit_12.jpg`.
3. Place them inside the `images` folder.
4. Run `python3 app.py` again.

## Change outfit names and categories

Open `outfits.json` in Visual Studio Code. Each outfit has:

- `name`: the name shown in the app
- `image`: the photo filename
- `weather`: one or more weather categories
- `occasions`: one or more occasion categories

Only use these weather labels: `Hot`, `Mild`, `Cold`, `Rainy`.

Only use these occasion labels: `University`, `Casual`, `Work`, `Night out`.

Be careful not to delete quotation marks, square brackets or commas.

## If something goes wrong

- If `python3` is not recognised, close and reopen Visual Studio Code after installing Python.
- If the app says Pillow is missing, activate the environment again with `source .venv/bin/activate`, then rerun the installation command.
- If an image does not appear, check that its filename exactly matches the name in `outfits.json`.
- To stop the app from the terminal, press Control + C.
