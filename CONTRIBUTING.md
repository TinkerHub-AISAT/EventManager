# Contributing to EventManager

Welcome to EventManager, We're excited to have you as a contributor. Here are some guidelines to help you get started and make your contribution as smooth as possible.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Code Contribution](#code-contribution)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Development Workflow](#development-workflow)
  - [Creating a Branch](#creating-a-branch)
  - [Making Changes](#making-changes)
  - [Testing](#testing)
  - [Committing Changes](#committing-changes)
  - [Opening a Pull Request](#opening-a-pull-request)
- [Acknowledging Contributors](#acknowledging-contributors)

## Code of Conduct

Please review and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). We expect all contributors to follow it to ensure a positive and inclusive community.

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug or issue with the bot, please [open an issue](https://github.com/TinkerHub-AISAT/EventManager/issues/new) on our GitHub repository. Be sure to include:

- Use the issue template provided
- A clear and descriptive title.
- A detailed description of the issue, including steps to reproduce.
- Label the issue appropriately
- Provide relevant information such as screenshots, logs, etc.
- Be respectful and constructive


### Suggesting Enhancements

Have an idea for an improvement or a new feature? We'd love to hear it! Please [open an issue](https://github.com/TinkerHub-AISAT/EventManager/issues/new) on our GitHub repository and provide:

- A concise and clear description of your idea or enhancement request.
- Any relevant context or use cases.

### Code Contribution

We welcome code contributions from the community. Here's how you can get started:

## Getting Started
To get started, you need to have Python 3, pip, and virtualenv installed on your machine. You also need to have a Firebase project with the following services enabled: Authentication, Firestore, and Storage. You need to download the Firebase SDK service account key and save it as firebase-key.json in the project folder.
### Prerequisites

Before you begin, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.10 or higher)
- [Firebase](https://firebase.google.com/docs/admin/setup)

### Setting Up the Development Environment

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine:
    ```shell
    git clone https://github.com/<your-namme>/EventManager.git
    ```
    for example:
    ```shell
    git clone https://github.com/TinkerHub-AISAT/EventManager.git
    ```
3. Create a virtual environment and install the project dependencies:

    ```shell 
    cd EventManager
    ```
    ```shell 
    python -m venv .venv
    ```
    ```shell 
    source .venv/bin/activate  # On Windows, use `.\.venv\Scripts\Activate.ps1`
    ```
    ```shell 
    pip install -r requirements.txt
    ```

4. Configure Firebase credentials. Refer to our documentation for instructions.

> The project will be available at <http://localhost:5000/>

## Development Workflow
### Creating a Branch
Before you start making changes, create a new branch for your feature or bug fix:

```shell
git checkout -b feature-FeatureName
```
if its a issue / bug:
```shell
git checkout -b issue-IssueName
```

### Making Changes
Make your code changes in the branch you created. Be sure to follow our coding style and conventions.

### Testing
Test your changes thoroughly to ensure they work as expected.

### Committing Changes
When you're ready to commit your changes, follow these guidelines for your commit messages:

- Use descriptive commit messages.
- Reference issue numbers if your commit relates to a specific issue.

### Opening a Pull Request
When you're ready to submit your changes, open a pull request (PR) on GitHub. Be sure to:

- Provide a clear and descriptive title for your PR.
- Include details of what your PR accomplishes.
- Mention the issue(s) your PR addresses (if applicable).
- Request a review from the maintainers.
- We will review your PR as soon as possible and provide feedback if needed.

## Acknowledging Contributors

We appreciate and acknowledge all the contributors and their work for this project. We credit them in the README.md file and thank them in the pull request comments. You can see the list of the contributors and their roles [here].
