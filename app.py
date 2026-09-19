from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Complete Cloud Computing practical", "done": False},
    {"id": 2, "title": "Prepare for viva", "done": False}
]


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")

    if title:
        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "done": False
        }

        tasks.append(new_task)

    return redirect("/")


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks

    tasks = [task for task in tasks if task["id"] != task_id]

    return redirect("/")


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)