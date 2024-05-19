
# Studify

## Overview
Studify is a centralized repository designed to assist students by providing easy access to study materials, including notes, archived lectures, and previous year question papers. This platform aims to support over 10,000 students in their academic endeavors by offering a user-friendly interface and a comprehensive resource library.

## Technologies Used
- **Python (Flask)**: Backend framework for server-side logic.
- **HTML/CSS**: Structure and styling of the web application.
- **Bootstrap**: Frontend framework for responsive design.
- **JavaScript**: Interactive elements and client-side logic.
- **Firestore**: NoSQL database for storing and retrieving study materials.

## Features
- **Study Materials**: Access and download a variety of study resources.
- **Archived Lectures**: View and revisit past lectures.
- **Previous Year Question Papers**: Find and utilize past examination papers for study reference.
- **User-Friendly Interface**: Intuitive design to facilitate easy navigation and resource access.

## Screenshots

### Home Page
![Home Page](https://raw.githubusercontent.com/0rajnishk/studify/main/screenshots/home_page.png)
*The landing page of Studify, where users can navigate to different sections such as notes, lectures, and question papers.*

### Notes Section
![Notes Section](https://raw.githubusercontent.com/0rajnishk/studify/main/screenshots/notes_page.png)
*Browse and download notes organized by subjects and topics.*

### Archived Lectures
![Archived Lectures](https://raw.githubusercontent.com/0rajnishk/studify/main/screenshots/archived_lectures.png)
*Access and view recorded lectures for revisiting important topics and concepts.*

### Question Papers
![Question Papers](https://raw.githubusercontent.com/0rajnishk/studify/main/screenshots/question_papers.png)
*Find previous year question papers to help with exam preparation.*


### Marks Calculator 
![Question Papers](https://raw.githubusercontent.com/0rajnishk/studify/main/screenshots/marks_calculator.png)
![Question Papers](https://raw.githubusercontent.com/0rajnishk/studify/main/screenshots/marks_page.png)
*Marks calculator help with Calculating marks*



## Getting Started

### Prerequisites
- Python 3.7+
- Flask
- Firestore credentials

### Installation

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/studify.git
    cd studify
    ```

2. Create a virtual environment and activate it
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Firestore
    - Obtain Firestore credentials and place the configuration file in the project directory.
    - Ensure the Firestore database is properly set up with collections for notes, lectures, and question papers.

5. Run the application
    ```bash
    python3 app.py
    ```

### Usage
- Open a web browser and navigate to `http://127.0.0.1:5000`.
- Browse through the different sections to access study materials, archived lectures, and question papers.

## Contributing
We welcome contributions to improve Studify! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your branch.
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please contact [your-email@example.com](mailto:your-email@example.com).

---

Thank you for using Studify! We hope it helps you achieve your academic goals.
