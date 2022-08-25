from pythonforandroid.recipe import PythonRecipe


class SetuptoolsRecipe(PythonRecipe):
    version = '42.0.2'
    url = 'https://pypi.python.org/packages/source/s/setuptools/setuptools-{version}.zip'
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = SetuptoolsRecipe()
