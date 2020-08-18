import sys
import webbrowser

from googlesearch import search
from time import gmtime, strftime

if __name__ == "__main__":
    print("Googling .... \n\n")
    file_name = 'result-'+strftime("%Y-%m-%d_%H-%M-%S", gmtime())+'.html'

    with open(file_name, 'a+') as file:
        file.write("<ul>\n")
        for result_url in search(query=sys.argv[1], stop=int(sys.argv[2])):
            print("[*][*] => {0}".format(result_url))
            file.write("<li><a href={0}>{0}</a></li>\n".format(result_url))
        file.write("</ul>")

    webbrowser.open(file_name)
