from pythonforandroid.recipe import CythonRecipe 


class ToolzRecipe(CythonRecipe): 
    """Build toolz"""

    version = "0.12.0-1"
    url = "http://mirror.archlinuxarm.org/armv7h/community/python-toolz-{version}-any.pkg.tar.xz"
    name = "toolz"

    depends = ["setuptools"]


recipe = ToolzRecipe()
