from flask import Flask, redirect, url_for, render_template, request
import date


app = Flask(__name__)

items = ["Buy Food", "Cook Food", "Eat Food"]
workItems = []


@app.route("/", methods=["POST", "GET"])
def list():
    if request.method == "POST":
        listItem = request.form["newItem"]
        items.append(listItem)
        return redirect(url_for("list"))
    else:
        return render_template("index.html", listTitle=date.getDate(), listItems=items)


@app.route("/work", methods=["POST", "GET"])
def workList():
    if request.method == "POST":
        listItem = request.form["newItem"]
        workItems.append(listItem)
        return redirect(url_for("workList"))
    else:
        return render_template("index.html", listTitle="Work List", listItems=workItems)


if __name__ == '__main__':
    app.run(debug=True)
