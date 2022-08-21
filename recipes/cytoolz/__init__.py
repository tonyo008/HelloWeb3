from pythonforandroid.recipe import CythonRecipe 


class CytoolzRecipe(CythonRecipe): 
    """Build cytoolz"""

    version = "0.12.0-1"
    url = "http://mirror.archlinuxarm.org/aarch64/community/python-cytoolz-debug-{version}-aarch64.pkg.tar.xz"
    name = "cytoolz"

    depends: List[str] = ["setuptools"]


recipe = CytoolzRecipe()