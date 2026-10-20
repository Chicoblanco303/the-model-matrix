
# The Model Matrix

## About the Project
The Model Matrix is a Python 3D graphics project built with Pygame and OpenGL. It displays a rotating 3D object composed of layered cubes in different shades of yellow.

## Features
- 3D cube rendering using OpenGL triangles
- Four nested cube layers with different yellow shades
- Continuous 3D rotation
- Keyboard controls for moving the object
- Pygame window running at up to 60 FPS

## Controls

| Key | Action |
|---|---|
| W | Move up |
| A | Move left |
| S | Move down |
| D | Move right |
| Close window | Exit the program |

## Technologies Used
- Python
- Pygame
- PyOpenGL
- OpenGL GLU

## Installation

Install the required packages:

```bash
python -m pip install pygame PyOpenGL PyOpenGL_accelerate
```

## How to Run
1. Install Python and the required packages.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

## Learning Objectives
- Working with 3D vertices and triangles
- Applying scaling, rotation, and translation
- Using OpenGL matrix transformations
- Handling keyboard input with Pygame
