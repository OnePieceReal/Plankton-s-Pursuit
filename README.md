# Plankton's Pursuit - Game Setup Guide

## Overview
A Pygame-based arcade game where Plankton tries to steal the Krabby Patty secret formula while avoiding obstacles and projectiles from Mr. Krabs.
<img width="703" height="834" alt="image" src="https://github.com/user-attachments/assets/3659b795-6f74-4762-addf-3a59b94d1386" />

## Prerequisites

### Installing Python
- Python 3.x is required
- Download from: https://www.python.org/downloads/

### Installing Pygame

#### For Regular Python Installation:
```bash
pip install pygame
```

#### For Anaconda/PyZo Users:
```bash
conda install pygame
```
or if that doesn't work:
```bash
pip install pygame
```

#### Verify Installation:
```python
import pygame
print(pygame.ver)
```

## Game Setup

### Directory Structure
Organize your files as follows:

```
your_game_folder/
├── planktons_pursuit_simple.py
└── assets/
    ├── fullkrusty.PNG
    ├── nightcrustcrab.PNG
    ├── secretformula.PNG
    ├── trainshutterstock.PNG
    ├── police.PNG
    ├── boat1.PNG
    ├── boat2.PNG
    ├── boat3.PNG
    ├── car1.PNG
    ├── car2.PNG
    ├── truck.PNG
    ├── truck2.PNG
    ├── cement.PNG
    ├── reverseredcar.PNG
    ├── reversetruck1.PNG
    ├── reversecement.PNG
    ├── reversebluecar.PNG
    ├── reversetruck2.PNG
    ├── plankton.PNG
    ├── MrKrabs.PNG
    ├── patrick.PNG
    ├── spongebob.jpg
    ├── images.jpg
    ├── chumbucket.PNG
    └── SpongeBob_Production_Music_Twelfth_Street_Rag.ogg
```

### Setup Steps
1. Create a folder for your game
2. Place `planktons_pursuit_simple.py` in this folder
3. Create an `assets` subfolder
4. Move all image files (.PNG and .jpg) to the `assets` folder
5. Move the sound file (.ogg) to the `assets` folder

## Running the Game

### From Command Line:
```bash
cd path/to/your_game_folder
python planktons_pursuit_simple.py
```

### From PyZo/Spyder:
1. Open `planktons_pursuit_simple.py` in the IDE
2. Make sure the working directory is set to your game folder
3. Run the script (F5 or Run button)

## Game Controls
- **↑** Arrow: Move up
- **↓** Arrow: Move down
- **←** Arrow: Move left
- **→** Arrow: Move right

## Gameplay Features
- **Objective**: Guide Plankton to steal the secret formula
- **Obstacles**: Avoid cars, boats, trains, and police
- **Day/Night Cycle**: Every 8 seconds, affects obstacle behavior
- **Progressive Difficulty**: Speed increases with each level
- **Projectiles**: Dodge characters shot by Mr. Krabs

## Scoring System
- **Score**: +100 points for each formula collected
- **Deaths**: Tracked but don't end the game
- **Levels**: Increase difficulty progressively

## Troubleshooting

### Common Issues:

#### "No module named pygame" Error:
- Install pygame using the instructions above
- Make sure you're using the correct Python environment

#### Images Not Loading:
- Verify all images are in the `assets` folder
- Check file names are exactly as listed (case-sensitive)
- Ensure you're running from the correct directory

#### Sound Not Playing:
- Sound file is optional
- Check the .ogg file is in the `assets` folder
- Some systems may require additional audio libraries

#### Game Running Slow:
- Close other applications
- Try reducing the window size in the code
- Update graphics drivers

## Tips for PyZo/Anaconda Users
1. Set working directory to your game folder:
   - In PyZo: Tools → Current Working Directory
   - Or use: `os.chdir('path/to/game/folder')`

2. If pygame doesn't install with conda, use:
   ```bash
   conda install -c cogsci pygame
   ```

3. For Anaconda Navigator users:
   - Open Anaconda Prompt
   - Navigate to your environment
   - Install pygame using pip

## Game Modifications
Feel free to modify:
- Speed values in the classes
- Timer duration (line with `pygame.time.set_timer`)
- Score values
- Color schemes in the color constants section

## Credits
Original Game by: Jose John Mulloor and Timothy Dangus ("The Green Team")
Code Cleanup and Documentation: Updated for cross-platform compatibility

Enjoy playing Plankton's Pursuit!
