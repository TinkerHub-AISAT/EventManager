# Contributing to Event Listing Platform

Thank you for your interest in contributing to Event Listing Platform, a web application that allows users to register and view events in their area, and admins to add and manage events using Firebase and Flask. We welcome and appreciate any kind of contribution, whether it is code, documentation, design, feedback, or anything else. By participating in this project, you agree to abide by our [code of conduct](^1^) and respect our [license](^2^). You can also check our [roadmap](^3^) to see our current and future plans.

## Table of Contents

- [Contributing to Event Listing Platform](#contributing-to-event-listing-platform)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Contributing Workflow](#contributing-workflow)
  - [Reporting Issues and Feature Requests](#reporting-issues-and-feature-requests)
  - [Improving Code Quality and Style](#improving-code-quality-and-style)
  - [Acknowledging Contributors](#acknowledging-contributors)

## Getting Started

To get started, you need to have Python 3, pip, and virtualenv installed on your machine. You also need to have a Firebase project with the following services enabled: Authentication, Firestore, and Storage. You need to download the Firebase SDK service account key and save it as firebase-key.json in the project folder.

To set up the development environment, follow these steps:

- Clone the project from GitHub:

```bash
git clone https://github.com/your-username/event-listing-platform.git
```

- Create and activate a virtual environment:

```bash
cd event-listing-platform
virtualenv venv
source venv/bin/activate
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

The project will be available at <http://localhost:5000/>

## Contributing Workflow

To contribute to this project, follow these steps:

- Fork the project from GitHub
- Create a new branch with a descriptive name
- Make your changes and commit them with a clear message
- Push your branch to your forked repository
- Create a pull request to the main repository
- Wait for the review and feedback

## Reporting Issues and Feature Requests

To report issues and feature requests, use the [issue tracker](^4^) of this project. Please follow these guidelines:

- Use the issue template provided
- Label the issue appropriately
- Provide relevant information such as screenshots, logs, etc.
- Be respectful and constructive

## Improving Code Quality and Style

To improve the quality and style of the code, please follow these guidelines:

- Follow the [PEP 8](^5^) coding standards for Python
- Write clear and concise comments and docstrings
- Use [black](^6^) and [isort](^7^) to format the code
- Use [flake8] and [pylint] to check the code quality
- Use [pytest] and [coverage] to write and run tests
- Use [sphinx] and [readthedocs] to generate and host documentation

## Acknowledging Contributors

We appreciate and acknowledge all the contributors and their work for this project. We credit them in the README.md file and thank them in the pull request comments. We also reward them with badges and stickers. You can see the list of the contributors and their roles [here].
