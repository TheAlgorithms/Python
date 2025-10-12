from sphinx_pyproject import SphinxConfig

project = SphinxConfig("../pyproject.toml", globalns=globals()).name
