import PySimpleGUI as PySG

splitted = ""
text = ""
PySG.theme("DarkBlue4")
layout = [
    [PySG.Text("Text for splitting"), PySG.InputText(size=(20, 5), key="input")],
    [
        PySG.Text("How many symbols in one part"),
        PySG.InputText(size=(5, 1), key="symbols"),
        PySG.Text("(Count on additional symbols for amount of parts)"),
    ],
    [PySG.Checkbox("Do we add amount of parts?", key="split")],
    [PySG.Button("Split")],
    [PySG.Multiline(splitted, key="-logtext-", size=(None, 10), rstrip=False)],
    [
        PySG.Button("Clear"),
        PySG.Text(
            "                                                © @uahave.fun",
            text_color="dark blue",
            font=("Helvetica", 10),
            justification="right",
        ),
    ],
    [PySG.Text("------------------------------------------------------")],
    [PySG.Button("Close")],
]

window = PySG.Window("Splitter", layout)

while True:
    event, values = window.read()
    if event in (None, "Close"):
        break
    if event == "Split":
        if values["input"] == "":
            PySG.popup("Add text to split!")
            continue
        if values["symbols"].isdigit() is False:
            PySG.popup("Symbols amount must be numeric only!")
            continue
        if values["symbols"] == "":
            PySG.popup("Enter symbols amount!")
            continue
        if int(values["symbols"]) < 1:
            PySG.popup("Enter symbols amount > 0!")
            continue
        if int(values["symbols"]) > len(values["input"]):
            PySG.popup("Enter symbols amount less then whole text size!")
            continue
        if int(values["symbols"]) == len(values["input"]):
            PySG.popup("Enter symbols amount less then whole text size!")
            continue
        es = [
            values["input"][i : i + int(values["symbols"])]
            for i in range(0, len(values["input"]), int(values["symbols"]))
        ]
        for i in es:
            if values["split"] is True:
                text = (
                    text
                    + str(es.index(i) + 1)
                    + "/"
                    + str(len(es))
                    + " "
                    + splitted
                    + i
                    + "\n"
                    + "\n"
                )
            else:
                text = text + splitted + i + "\n" + "\n"
        window["-logtext-"].update(text)
    if event == "Clear":
        window["-logtext-"].update("")
        text = ""
window.close()
