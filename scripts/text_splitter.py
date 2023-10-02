import PySimpleGUI as SG

splitted = ""
text = ""
SG.theme("DarkBlue4")
layout = [
    [SG.Text("Text for splitting"), SG.InputText(size=(20, 5), key="input")],
    [
        SG.Text("How many symbols in one part"),
        SG.InputText(size=(5, 1), key="symbols"),
        SG.Text("(Count on additional symbols for amount of parts)"),
    ],
    [SG.Checkbox("Do we add amount of parts?", key="split")],
    [SG.Button("Split")],
    [SG.Multiline(splitted, key="-logtext-", size=(None, 10), rstrip=False)],
    [
        SG.Button("Clear"),
        SG.Text(
            "                                                © @uahave.fun",
            text_color="dark blue",
            font=("Helvetica", 10),
            justification="right",
        ),
    ],
    [SG.Text("------------------------------------------------------")],
    [SG.Button("Close")],
]

window = SG.Window("Splitter", layout)

while True:
    event, values = window.read()
    if event in (None, "Close"):
        break
    if event == "Split":
        if values["input"] == "":
            SG.popup("Add text to split!")
            continue
        if values["symbols"].isdigit() is False:
            SG.popup("Symbols amount must be numeric only!")
            continue
        if values["symbols"] == "":
            SG.popup("Enter symbols amount!")
            continue
        if int(values["symbols"]) < 1:
            SG.popup("Enter symbols amount > 0!")
            continue
        if int(values["symbols"]) > len(values["input"]):
            SG.popup("Enter symbols amount less then whole text size!")
            continue
        if int(values["symbols"]) == len(values["input"]):
            SG.popup("Enter symbols amount less then whole text size!")
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
