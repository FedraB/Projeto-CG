# Basics of Computer Graphics

This project implements a 3D rendering pipeline that reads a triangular mesh of a 3D object from a text file, projects its vertices onto the screen using perspective projection, and rasterizes the resulting triangles using a scan-line algorithm. The output is displayed as a black-and-white visualization, with filled triangles painted white.

## Features
### Mesh Loading:

- Reads a triangular mesh from a text file.
- The file format specifies the number of vertices, the number of triangles, vertex coordinates (x, y, z), and the vertex indices for each triangle.

Example:
```
3 1
50.0000 0.0000 0.000
0 50 0
0 0 50
1 2 3
```

### Camera Parameters:

- Loads virtual camera parameters from a separate text file.
- Parameters include:
- Camera position (C)
- Direction vector (N)
- Up vector (V)
- Distance to the projection plane (d)
Horizontal and vertical scaling factors (hx, hy)

Example:
```
0 1 -0.66
0 -1 -1
6
2
2
0 -500 500
```

### Real-Time Update:

- Allows the user to modify camera parameters in the text file, reload them, and redraw the object without restarting the application.

### Rendering Pipeline:

- Converts object vertices from world coordinates to view coordinates.
- Applies perspective projection.
- Converts vertices to normalized coordinates and then to screen coordinates.
- Rasterizes the projected triangles using the scan-line algorithm.

### Visualization:

- White pixels represent the filled triangles on the screen.
- All other pixels are black.

## Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed 

### Usage
- Prepare the mesh and camera parameter files in the specified format.
- Run the application with:
```bash
python main.py
```
- Modify objects or the camera parameters as needed and reload them with a single key press on **'R'**

### Controls

-  to reload the camera parameters and re-render the object without restarting the program.
