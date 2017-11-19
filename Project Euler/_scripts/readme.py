"""Generates the README file."""

from glob import glob
import re
from urllib.request import urlopen
import html2text
from bs4 import BeautifulSoup

INTRODUCTION = """
# Project Euler
Problems are taken from https://projecteuler.net/.

Project Euler is a series of challenging mathematical/computer programming 
problems that will require more than just mathematical insights to solve. 
Project Euler is ideal for mathematicians who are learning to code.

Here the efficiency of your code is also checked.
We try to provide all the best possible solutions.

## Contribution

In order to contribute, it is highly recommended, that you follow the PEP08
standard, as this is used for educational purposes. Altough it is
not strictly required, make sure that your solution can run in Python 2 and 3,
preferably Python 3.

Create a new folder or add a solution file with the already established pattern.
In the future, there will be an automatic performance evaluation of each solution,
therefore stick as closely to the standard as possible.

UnitTests in the docstring of functions, which are used to solve the problem, are
highly appreciated.

### Updating README.md

To update the README.md (problem description), make sure that you have all of the
requirements installed.

    pip3 install -r _scripts/requirements.txt
    python3 _scripts/readme.py

There is no need to refresh the other problems, if no changes to the website
were made.


"""

def scrape_problem(problem):
    """Scrapes the problem from the website."""
    response = urlopen("https://projecteuler.net/problem=" + str(problem))
    html = str(response.read()).replace("\\n", "").replace("\\r", "")
    soup = BeautifulSoup(html, "lxml")

    for exponent in soup.find_all("sup"):
        html = html.replace(str(exponent), "^(" + exponent.text + ")")
    soup = BeautifulSoup(html, "lxml")

    title = "# Problem " + str(problem)
    subtitle = "## " + soup.find_all("h2")[0].text
    description = str(soup.find_all("div", class_="problem_content")[0])

    markdown = html2text.HTML2Text()
    description = markdown.handle(description).replace("\\xc3\\x97", "x")\
                                              .replace("\\xe2\\x86\\x92", "->")\
                                              .replace("\\xe2\\x88\\x92", "-")

    text = (
        title + "\n" +
        subtitle + "\n" +
        description
    )
    return text

def get_problem_file_name(problem):
    """Returns a uniform file name for a problem."""
    return "../Problems/problem" + str(problem) + ".md"

def get_solved_problems():
    """Returns the index of all solved problems."""
    problems = []
    paths = glob("../*")
    regex = re.compile("^../Problem [0-9]+")

    for path in paths:
        if regex.match(path):
            problems.append(int(path.replace("../Problem ", "")))

    return list(set(problems))

def add_title_level(markdown):
    """Adds an indentation level to all markdown titles."""
    lines = markdown.split("\n")

    for i in range(0, len(lines)):
        if lines[i].startswith("#"):
            lines[i] = "#" + lines[i]
    return "\n".join(lines)

def main():
    """Gets called when the file is executed."""
    problems = get_solved_problems()
    readme = ""

    readme += INTRODUCTION
    problem_descriptions = ""
    table_of_content = "## Table of Content\n"

    for problem in problems:
        description = ""
        try:
            with open(get_problem_file_name(problem)) as file:
                description = "".join(file.readlines())
        except FileNotFoundError:
            print("Problem " + str(problem) + " not found, scraping")
            description = scrape_problem(problem)
            with open(get_problem_file_name(problem), 'w') as file:
                file.write(description)

        problem_descriptions += add_title_level(description)
        table_of_content += ("- [Problem " + str(problem) + "]("
                             + "#problem-" + str(problem) + ")\n")

    readme += table_of_content + "\n\n"
    readme += problem_descriptions

    with open("../README.md", 'w') as file:
        print("Writing README.md..")
        file.write(readme)

if __name__ == "__main__":
    main()
