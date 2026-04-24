# Project Title
GmE 205 - Laboratory Exercise 6

# How to set up the virtual environment
1. Create a folder on your computer and open it in your IDE (e.g., VS Code)
2. Open the terminal then create the virtual environment by running the following:
    ```
    py -m venv .venv
    .\.venv\Scripts\activate
    ```
3. Press ```Ctrl + Shift + P``` in VS Code, search for *Python: Select Interpreter*, then choose the interpreter inside the ```.venv``` folder
4. Install the required packages by running the following in the terminal:
    ```
    python -m pip install --upgrade pip
    pip install <package1> <package2>
    ```
5. (Recommended) List the installed packages via:
    ```
    pip freeze > requirements.txt
    ```

# How to run Python scripts

In the terminal, ensuring that ```(.venv)``` is present in the prompt, run the following:
    ```
    python <folder/script_name.py>
    ```

# Reflections
Part B2. `SpatialObject`
1. We created the base class `SpatialObject` as an abstraction of the geometric properties of its subclasses. This allows the subclasses (`Parcel`, `Road`, and `Building`) to focus more on their specific attributes and behaviors, while delegating the geometric behaviors to the base `SpatialObject` class.
2. There is no need to rewrite `distance_to()` in every subclass because this is a method pertaining to underlying geometric properties. In our design, anything geometric is under the purview of the base `SpatialObject` class.
3. As previously mentioned, this design "abstracts away" the geometric properties of the different subclasses into a shared base class `SpatialObject`, whose properties can be reused by each of the subclasses without needing a rewrite.