# Music Blog
A Django-based blog platform for music enthusiasts to read and write about music trends, reviews, and news.

[**Live Demo**](https://musicfan-2690fdc67af7.herokuapp.com/)

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Contributing](#contributing)


## Overview
Music Blog is a Django-based web application that allows users to read and write blog posts about music. It features user authentication, post creation and editing, comment system and contact form.

The application uses Bootstrap for styling and Django's built-in authentication system for user management.

## Features
- User authentication (sign up, sign in, sign out)
- CRUD creation, reading, updating and deletion of data records
- Comment system for blog posts
- Responsive design using Bootstrap
- Contact form for user inquiries



### 6. Usage Instructions
To use the Music Blog application, follow these steps:

1. **Sign Up**: Create an account to start interacting with the blog.
2. **Sign In**: Log in to access additional features like creating blog posts and leaving comments.
3. **Create a Blog Post**: After signing in, you can create a new blog post from the user dashboard.
4. **Comment on Blog Posts**: Signed-in users can leave comments on blog posts.
5. **Admin Panel**: Access the [admin panel](https://musicfan-2690fdc67af7.herokuapp.com/admin/) with your superuser credentials to manage the site.
6. **Contact form**: Contact the team with a vaild email, signing is not required.

### User Stories
Here are the user stories for this project:

- **Modify or delete comment on a post**: As a user, I want to be able to edit or delete my comments on blog posts.
- **Read Contact Us messages**: As an admin, I want to be able to read and manage Contact Us messages.
- **Contact us form**: As a visitor, I want to be able to contact the site administrators.
- **Approve comments**: As an admin, I want to be able to approve or reject comments.
- **Create drafts**: As a user, I want to save blog posts as drafts before publishing them.
- **Manage posts**: As a user, I want to create, edit, and delete my blog posts.
- **Comment on a post**: As a user, I want to comment on blog posts.
- **View comments**: As a visitor, I want to see comments on blog posts.
- **View a post**: As a visitor, I want to read blog posts.

### Flowcharts

## Technologies Used

### Languages Used
- Python 3.7+
- HTML
- CSS
- JavaScript

## Frameworks and Libraries

- **[Django](https://www.djangoproject.com/)**: A high-level Python framework used to build robust web applications quickly.
- **[Bootstrap 5](https://getbootstrap.com/)**: A front-end framework for creating responsive and mobile-friendly websites.
- **[Font Awesome](https://fontawesome.com/)**: A large collection of icons and social logos for adding visual elements to your project.
- **[Google Fonts](https://fonts.google.com/)**: A service providing a wide variety of free fonts for web applications.
- **[Crispy Forms](https://django-crispy-forms.readthedocs.io/)**: A Django library for easier form handling and styling.
- **[Cloudinary](https://cloudinary.com/)**: A cloud-based platform for storing and managing images efficiently.
- **[jQuery](https://jquery.com/)**: A JavaScript library that makes it easy to manipulate the DOM and create interactive features.
- **[Git](https://git-scm.com/)**: A version control system for tracking changes and collaborating with others.
- **[ElephantSQL](https://www.elephantsql.com/)**: A cloud-based PostgreSQL database service for scalable data storage.
- **[GitHub](https://github.com/)**: A platform for hosting code repositories and collaborating with other developers.
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools/)**: A set of tools in Google Chrome for debugging and analyzing web applications.
- **[W3C HTML Validator](https://validator.w3.org/)**: A tool for ensuring your HTML code complies with web standards.
- **[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)**: A service for validating CSS to ensure it's correctly structured.
- **[JSHint](https://jshint.com/)**: A JavaScript linting tool to detect errors and code issues.
- **[PEP 8](https://peps.python.org/pep-0008/)**: The style guide for Python, providing best practices for clean and consistent code.



## Wireframes

## Flowcharts


### Entity-Relationship Diagram

## Testing

## How We Tested the Web Application

To ensure the reliability and quality of the Django web application, a comprehensive testing strategy was implemented. Here's how we tested the application to ensure it meets our standards for performance and functionality.

### Automated Testing
Django provides a built-in framework for automated testing, allowing us to create unit tests and integration tests. Automated testing helps us maintain code quality and quickly identify any issues.

- **Unit Tests**: These tests focused on individual components and functions within the application to ensure they behaved as expected in isolation. We wrote tests for critical business logic, models, and custom functions.

- **Integration Tests**: These tests verified the interactions between different components to ensure they worked together correctly. We tested relationships between Django models and the behavior of views when handling HTTP requests.

To run the automated tests, we used the following command:
```bash
python manage.py test


### Known Bugs

## Deployment

## Credits

## Acknowledgements
