from gettext import find
from numpy import double


st = "This is a string with double    spaces"

doublespaces = st.find("  ")
print(doublespaces)
