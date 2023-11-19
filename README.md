# Event Listing Platform

This is a web application that allows users to register and view events in their area, and admins to add and manage events using Firebase and Flask.

## Features

- User authentication and authorization
- Event creation and editing 
- Event listing and filtering 
- Event details and registration 
- Admin dashboard and analytics 

## Installation

To run this project, you need to have Python 3, pip, and virtualenv installed on your machine. You also need to have a Firebase project with the following services enabled: Authentication, Firestore, and Storage. You need to download the Firebase SDK service account key and save it as firebase-key.json in the project folder.

To install the project, follow these steps:

- Clone the project from GitHub:

```bash
git clone https://github.com/TinkerHub-AISAT/EventManager.git
```


- Create and activate a virtual environment:

```bash
cd EventManager
python -m venv .venv
source .venv/bin/activate
```

- Install the required packages:

```bash
pip install -r requirements.txt
```

- Set the environment variables:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

- Run the Flask server:

```bash
flask run
```

The project will be available at http://localhost:5000/

## Usage

To use the project, you need to register as a user or an admin. You can use the following credentials for testing purposes:

- User: user@test.com / password
- Admin: admin@test.com / password

As a user, you can:

- View the list of events in your area
- Filter the events by category, date, or keyword
- View the details of an event and register for it
- View your profile and the events you registered for

As an admin, you can:

- Add, edit, and delete events
- Upload images for the events
- View the list of users and the events they registered for
- View the dashboard and the analytics of the events

## Contribution

This project is open source and welcomes contributions from anyone. If you want to contribute to this project, please follow these steps:

- Fork the project from GitHub
- Create a new branch with a descriptive name
- Make your changes and commit them with a clear message
- Push your branch to your forked repository
- Create a pull request to the main repository
- Wait for the review and feedback

## Contributors

This project is created and maintained by:

- Your name (your GitHub username)
- Other contributors (their GitHub usernames)

## License

This project is licensed under the MIT License. See the LICENSE file for more details..
