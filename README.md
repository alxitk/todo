# To-Do App
> Simple and stylish task manager with tags and deadlines

A Django-based web application for managing tasks.
Users can create, edit, delete and mark tasks as done/undone.
Tasks support tags making it easier to organize your workflow.

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

```shell
git clone https://github.com/yourusername/todo.git
cd todo

# create virtual environment
python -m venv .venv
source .venv/bin/activate  # on Linux/macOS
.venv\Scripts\activate     # on Windows

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# start server
python manage.py runserver
```
Now open http://127.0.0.1:8000 in your browser

## Features

Main functionality to organize your tasks:
* Create, update and delete tasks
* Mark tasks as Done / Not Done
* Add tags
* Set deadlines to stay on track
* Manage tags (create, update, delete)
UI Features:
* Modern responsive design with sidebar
* Dark / Light theme toggle
* Mobile-friendly navigation with burger menu

## Contributing

If you’d like to contribute, please follow these steps:
	1.	Fork the repository
	2.	Create a feature branch (git checkout -b feature/my-feature)
	3.	Commit your changes (git commit -m "feat: add my new feature")
	4.	Push to the branch (git push origin feature/my-feature)
	5.	Open a Pull Request

Guidelines
	•	Follow Conventional Commits for commit messages.
	•	Keep code style consistent (project uses Black and Flake8).
	•	Make sure tests pass before submitting a PR.

If there are bigger contributions (e.g. refactoring or new modules), please open an issue first to discuss it.

For more detailed rules, check CONTRIBUTING.md (if available).

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Repository: https://github.com/alxitk/todo
- Issue tracker: https://github.com/alxitk/todo/issues
- Related projects:
  - https://github.com/alxitk/Task-Management
