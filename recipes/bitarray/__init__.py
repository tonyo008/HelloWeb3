from pythonforandroid.recipe import CompiledComponentsPythonRecipe 


class BitarrayRecipe(CompiledComponentsPythonRecipe): 
    """Build bitarray"""

    version = "2.5.0"
    url = "https://files.pythonhosted.org/packages/66/3b/14b8c815be18397371fcafe1d981c4e8b470f6bf6052e284ddd9475f0d12/bitarray-{version}.tar.gz"
    
    name = "bitarray"

    call_hostpython_via_targetpython = False
    install_in_hostpython = True

recipe = BitarrayRecipe()
