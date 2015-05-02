# returns a random wikipedia article by category, defined by argv[1]
# for (sub)categories with multiple words e.g. 'artificial trees'
# use an underscore between words e.g. 'artificial_trees'

import webbrowser
from sys import argv

category = argv[1]

webbrowser.open_new("https://en.wikipedia.org/wiki/Special:RandomInCategory/"+ argv[1])
