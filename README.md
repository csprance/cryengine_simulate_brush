# cryengine_simultate_brush
> Python script to simulate physics on a brush in CRYENGINE.

## Installation
* Copy the simulatebrush.py file to Editors/Scripts
* Copy the user_values folder to Editor/Scripts
* Copy the simulate_brush_shelf to Editor/Scripts/Shelves

# How to use
* Select a brush
* Click the SimBrush shelf button or run the script from the Python Scripts pane
    * This is will add a special material to the object and convert it to a RigidBodyEx and simulate it
* Once the model has simulated click the SimBrush button again to convert it back to a brush
* Undoing a simulation results in about 3-4 undos so you must undo it multiple times (or alternatively just move the brush and simulate it again rather than undoing.)