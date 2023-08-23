import tkinter
import json

main = tkinter.Tk()
main.geometry("600x500")
main.title("socialnet")

with open("nodes.json", "r") as json_file:
    data = json.load(json_file)
print(data)

def savenode(event, obj, x, y):
    if event.keysym == "Return":
        print("saving")
        res = obj.get()
        entry = {
            "name": str(res),
            "x": x,
            "y": y
        }
        print(entry)
        data.append(entry)
        with open("nodes.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

def createnode(click):
    print(click.x,click.y)
    textinput = tkinter.Entry(main)
    textinput.pack()
    textinput.bind("<Return>", lambda event, entry=textinput, x=click.x, y=click.y: savenode(event, entry, x, y))
    
main.bind("[", createnode)

main.mainloop()
