from pythonforandroid.recipe import CythonRecipe 


class CytoolzRecipe(CythonRecipe): 
    """Build cytoolz"""

    version = "0.9.0"
    url = "https://github.com/pytoolz/cytoolz/archive/refs/tags/{version}.zip"
    name = "cytoolz"

    depends = ["setuptools"]


recipe = CytoolzRecipe()
