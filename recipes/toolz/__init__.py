from pythonforandroid.recipe import CythonRecipe 


class ToolzRecipe(CythonRecipe): 
    """Build toolz"""

    version = "0.9.0"
    url = "https://github.com/pytoolz/toolz/archive/refs/tags/{version}.zip"
    name = "toolz"

    depends = ["setuptools"]


recipe = ToolzRecipe()
