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

Part B4 to B7: Constructors, Methods, Inheritance, and Relationships
1. Cross-checking each constructor against the UML, all of the important attributes were placed in the correct class. To recall, here are the classes and their attributes:

- `SpatialObject`: `geometry`
- `Parcel`:
    - `parcel_id`: str (new)
    - `area`: float
    - `zone`: str
- `Building`:
    - `building_id`: str (new)
    - `height`: float
    - `usage`: str
- `Road`:
    - `road_id`: str (new)
    - `length`: float
    - `type`: str
- `Household`:
    - `household_id`: str
    - `num_people`: int
    - `income`: float
    - `tenure_type`: str

2. All queries specific to a domain class are placed accordingly: `compute_area()` for `Parcel`, `get_height()` for `Building`, `get_length()` for `Road`, and `calculate_total_income()` for `Household`. A common method `describe()` is also included for printing the object contents.

3. `Parcel`, `Building`, and `Road` all inherit from `SpatialObject`, and each call `super().__init__(geometry)` to instantiate this. The base methods `distance_to()` and `intersects()` were no longer rewritten in the domain classes.

4. Relationships were implemented in two ways. First, associations/aggregations were encoded as attributes, either as single values or as lists (depending on which class has one or zero-to-many of another class). Here are the relational attributes per domain class (* = included as a parameter in the constructor method):
- `Parcel`:
    - `buildings`: list[`Building`]
    - `adjacent_roads`: list[`Road`]
- `Building`:
    - `parcel`: `Parcel`*
    - `households`: list[`Household`]
- `Road`:
    - `adjacent_parcels`: list[`Parcel`]
- `Household`
    - `building`: `Building`*

The attributes with the asterisk (*) seem to pertain to situations where one class can only be linked to one instance of another class. A `Building` can only be located on one `Parcel`, while a `Household` can only live in one `Building`.