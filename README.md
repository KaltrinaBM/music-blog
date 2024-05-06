# Music Blog
A Django-based blog platform for music enthusiasts to read and write about music trends, reviews, and news.

[**Live Version**](https://musicfan-2690fdc67af7.herokuapp.com/)

[**Repository GitHub Repo**](https://github.com/KaltrinaBM/music-blog)


![home](/static/images/musicblog.PNG)


## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Usage Instructions](#usage-instructions)
4. [User Stories](#user-stories)
5. [Technologies Used](#technologies-used)
6. [Design and Architecture](#design-and-architecture)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Overview
Music Blog is a Django-based web application that allows users to read and write blog posts about music. It features user authentication, post creation and editing, a comment system, and a contact form.

The application uses Bootstrap for styling and Django's built-in authentication system for user management.

## Features
- User authentication (sign up, sign in, sign out)
- CRUD (create, read, update, delete) operations for blog data
- Comment system for blog posts
- Responsive design using Bootstrap
- Contact form for user inquiries

![Contact Us](/static/images/contactform.PNG)

## Usage Instructions
To use the Music Blog application, follow these steps:

1. **Sign Up**: Create an account to interact with the blog.
2. **Sign In**: Log in to access additional features like reading blog posts and leaving comments.
3. **Comment on Blog Posts**: Signed-in users can leave comments on blog posts.
4. **Admin Panel**: Access the [admin panel](https://musicfan-2690fdc67af7.herokuapp.com/admin/) with your superuser credentials to manage the site.
5. **Contact Form**: Use the contact form to send messages to the team. A valid email is required, but signing in is not.

## User Stories
These user stories guided the development of this project:

- **Modify or delete comment on a post**: As a user, I want to update or delete my comments on blog posts.
- **Read Contact Us messages**: As an admin, I want to read and manage Contact Us messages.
- **Contact us form**: As a visitor, I want to contact the site administrators.
- **Approve comments**: As an admin, I want to approve or reject comments.
- **Create drafts**: As a admin, I want to save blog posts as drafts before publishing them.
- **Manage posts**: As a admin, I want to create, edit, and delete my blog posts.
- **Comment on a post**: As a user, I want to comment on blog posts.
- **View comments**: As a visitor, I want to see comments on blog posts.
- **View a post**: As a visitor, I want to read blog posts.

## Technologies Used

### Languages Used
- Python 3.7+
- HTML
- CSS
- JavaScript

### Frameworks and Libraries
- **[Django](https://www.djangoproject.com/)**: A high-level Python framework used to build robust web applications.
- **[Bootstrap 5](https://getbootstrap.com/)**: A front-end framework for creating responsive and mobile-friendly websites.
- **[Font Awesome](https://fontawesome.com/)**: A collection of icons and social logos for visual elements.
- **[Google Fonts](https://fonts.google.com/)**: A collection of free fonts for web projects.
- **[Crispy Forms](https://django-crispy-forms.readthedocs.io/)**: A Django library for simplifying form handling and styling.
- **[Cloudinary](https://cloudinary.com/)**: A cloud-based platform for storing and managing images.
- **[jQuery](https://jquery.com/)**: A JavaScript library for manipulating the DOM and creating interactive features.
- **[Git](https://git-scm.com/)**: A distributed version control system for tracking code changes and collaborating with others.
- **[ElephantSQL](https://www.elephantsql.com/)**: A cloud-based PostgreSQL database service.
- **[GitHub](https://github.com/)**: A platform for hosting code repositories and collaborating with other developers.
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools/)**: A set of debugging and analysis tools integrated into Google Chrome.
- **[W3C HTML Validator](https://validator.w3.org/)**: A tool for validating HTML to ensure compliance with web standards.
- **[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)**: A service for validating CSS code for correctness.
- **[JSHint](https://jshint.com/)**: A JavaScript linting tool for detecting errors.
- **[PEP 8](https://peps.python.org/pep-0008/)**: The official style guide for Python, providing best practices for coding in Python.


## Design and Architecture

### Flowcharts

The following flowchart was created to illustrate the application's structure and functionality.

![Flowchart](/static/images/flowchart.jpg)

### Wireframes

The following wireframe was created to display a visual guide of the website.

![Wireframe](/static/images/wireframe.jpg)

### Entity-Relationship Diagram (ERD)

The following table represents the attributes of the `ContactFormEntry` model, including the database key and validation information:

| Attribute       | Type                     | Description                                           | Validation                  |
|-----------------|--------------------------|-------------------------------------------------------|-----------------------------|
| `id`            | AutoField (Primary Key)   | Automatically generated unique identifier for each record.  | Unique, auto-incremented.  |
| `name`          | CharField(max_length=30)  | Name of the person submitting the contact form.       | Maximum 30 characters.     |
| `email`         | EmailField                | Email address for contact.                           | Valid email format.        |
| `subject`       | CharField(max_length=100) | Subject of the message (optional).                   | Maximum 100 characters.     |
| `message`       | TextField                 | Content of the message.                              | No specific validation.   |
| `phone_number`  | CharField(max_length=15)  | Contact phone number (optional).                     | Maximum 15 characters.     |
| `created_at`    | DateTimeField(auto_now_add=True) | Timestamp indicating when the form was submitted.   | Automatically generated.  |
| `read`          | BooleanField(default=False)| Flag indicating whether the message has been read.   | True/False.                |


## Testing

### Manual Testing
In addition to automated testing, I manually validated each page of the web application using the W3C Markup Validation Service to check for proper HTML structure, and CI Python Linter to ensure compliance with coding standards.

During the validation process, a few small warnings were detected, but they were promptly fixed to ensure compliance with web standards and code quality. These warnings were mostly minor issues that didn't affect functionality, but addressing them helps maintain a cleaner codebase and improves the user experience.

[W3C Markup Validation Service](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusicfan-2690fdc67af7.herokuapp.com%2F)

- **W3C Markup Validation**: Each page was tested by entering its URL into the W3C Markup Validation Service. The validation service checks for syntax errors, structural issues, and other potential problems in the HTML markup.
- ***Results***: All pages passed the validation with no errors detected, indicating that the HTML structure conforms to the W3C standards. This validation step helps ensure cross-browser compatibility and contributes to a consistent user experience.

![HTML homepage test](/static/images/test.PNG)

[CI Python Linter](https://pep8ci.herokuapp.com/) 

- **CI Python Linter**: Used to check the Python code for syntax errors and code style violations.
- ***Results***:
- No errors or style violations were found in the code.
- The code was checked and returned with no issues detected.

**Performance Testing with Lighthouse**

To ensure optimal performance, accessibility, and best practices, I tested the web application using [Lighthouse](https://developers.google.com/web/tools/lighthouse), a tool provided by Google Chrome. 

- ***Results***
Below are the results from the Lighthouse tests:

![Lighthouse Homepage Test](/static/images/lighthouse.PNG)

These screenshots demonstrate the outcomes of the performance and accessibility evaluations, showcasing the measures taken to ensure the web application's quality and compliance.

### Automated Testing

Django provides built-in support for automated testing, allowing for unit tests and integration tests. Automated testing helps maintain code quality and quickly identify issues.

While conducting integration tests, a bug was discovered in the 'Contact Us' form. The term 'Contact Us' was mentioned on the button leading to the form, but not within the actual form itself. This inconsistency could have caused confusion for users trying to understand the purpose of the form. The issue was identified during integration testing and was subsequently fixed by adding a clear title inside the form indicating that it was for 'Contact Us' inquiries.

To run the automated tests, use the following command:
```bash
python manage.py test
```

![Automated Testing](/static/images/testing.PNG)

### Further Testing
The Website was tested on Google Chrome and Internet Explorer.
The website was viewed on a variety of devices such as Desktop, Laptop, Andorid phones.
A large amount of testing was done to ensure that all functions are working as intended.
Family members were asked to review and play the game to point out any bugs and/or user experience issues.

### Known Bugs

#### Footer Position Issue
In certain situations, such as after submitting the contact form or when signing out, the footer may appear in the middle of the page instead of at the bottom.
The cause is likely related to CSS or layout issues, possibly due to flexbox configurations or page content dynamics.
This issue doesn't affect functionality but may disrupt the visual consistency of the page layout. Due to limited time, this issue will not be fixed. 

## Deployment

### Heroku Deployment
To deploy this Django project to Heroku from its [GitHub repository](https://github.com/KaltrinaBM/music-blog), the following steps were taken:

1. **Create a Heroku Account**: Log into your Heroku account or create a new one at [Heroku](https://www.heroku.com/).
2. **Create a New App**:
   - Click **New** in the top-right corner of the dashboard.
   - Select **Create new app** from the drop-down menu.
   - Enter a unique name for your app and choose your region.
   - Click **Create App**.
3. **Configure Settings**:
   - Go to the **Settings** tab.
   - Scroll down to **Config Vars** and click **Reveal Config Vars**.
   - Add a new variable with `PORT` as the key and `8000` as the value.
   - Click **Add**.
   - Scroll down to **Buildpacks** and click **Add buildpack**.
   - Select 'Python' and then 'Node.js'. **Ensure 'Python' is on top** of the buildpack list. If not, drag it to the top and save.
4. **Deploy from GitHub**:
   - Return to the **Deploy** tab and select 'GitHub' as the deployment method.
   - Connect your GitHub account and authorize Heroku to access your repositories.
   - Search for your repository by name and click **Connect**.
   - Choose a deployment method:  
     - Click **Enable Automatic Deploys** to automatically deploy when you push to GitHub.
     - Select the desired branch and click **Deploy Branch** for manual deployment.
5. **Deploy the App**:
   - After deploying, you should see a success message saying, "The app was successfully deployed."
   - Click **Open App** to view your deployed site.

## Credits

- Portions of this project were adapted from a Code Institute walkthrough project. Due to time constraints and personal challenges, these resources offered a valuable foundation. However, this adaptation does not include the custom model for the contact form, which was developed independently.

### AI Assistance
- **[ChatGPT](https://openai.com/blog/chatgpt/)**: Used for explanation and clarification of technical concepts, helping to understand Django structures and troubleshoot issues during project deployment.

### Other Resources
- **[Google](https://www.google.com/)**: An invaluable tool for researching solutions and finding documentation.
- **[W3Schools](https://www.w3schools.com/)**: A great resource for learning web technologies like HTML, CSS, and JavaScript.
- **[Stack Overflow](https://stackoverflow.com/)**: The community for resolving coding issues and getting answers to programming questions.

### Free Images
- A free-licensed image was obtained from Google, ensuring compliance with licensing terms.

### Acknowledgements
- Special thanks to Code Institute for their walkthrough project, which helped with certain parts of the project, excluding the custom contact form model.
- I also appreciate the support from my family and my mentor [Iuliia Konovalova](https://github.com/IuliiaKonovalova) who helped me through the project.
