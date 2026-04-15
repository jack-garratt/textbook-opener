# Textbook Opener

A Python based automation tool designed to streamline access to Pearson Active Learn textbooks. This application handles the login process and navigates directly to your digital books using the Playwright browser automation library.

 🚀 Features
---
- Automated Login: Securely enters your credentials and signs into the Pearson portal.

- One Click Navigation: Automatically selects the correct subject and book from your library.

- Custom Library: Manage your available textbooks through a simple config.yaml file.

- Modern GUI: A clean desktop interface built with customtkinter for easy interaction.

- Cookie Handling: Automatically rejects cookie prompts.

 🛠️ Installation (From Source Code)
 ---
### 1. Prerequisites
- Python 3.x
- Google Chrome

### 2. Setup
Clone the repository and install the necessary Python packages:

```Bash
pip install -r requirements.txt
```
### 3. Configuration
The application requires two configuration files in the root directory:

**.env** (Credentials)
Create a file named .env to store your login details:
```
EMAIL=your_email@example.com
PASSWORD=your_password
```

**config.yaml** (Textbooks)
Enter the details of your textbook in the format given where the subject and name is a subphrase from the website:

`Edexcel AS and A level Physics 2015` --> `Physics`

`Edexcel A level Physics ActiveBook 2` --> `ActiveBook 2`



🛠️ Installation (From .app)
---
### 1. Extraction
- Extract files from .zip

### 2. Configuration
The application requires two configuration files in the root directory:

**.env** (Credentials)
Edit the file named .env to store your login details:
```
EMAIL= "your_email@example.com"
PASSWORD= "your_password"
```

**config.yaml** (Textbooks)
Enter the details of your textbook in the format given where the subject and name is a subphrase from the website:

`Edexcel AS and A level Physics 2015` --> `Physics`

`Edexcel A level Physics ActiveBook 2` --> `ActiveBook 2`


📖 Usage
---
Launch the application:

```
python app.py
Select a textbook from the generated list.
```

The application will withdraw the GUI and launch a specialized Chrome instance to open your book.

Once the browser is closed, the application will exit.


 🗂️ Project Structure
---

app.py: The main GUI using customtkinter.

browser.py: Manages the Playwright browser and automation.

find_textbook.py: Handles reading the YAML configuration and selecting books.

login_page.py: Logic for credential entry.

navigator.py: Helper methods for clicking links, buttons, and entering text.

paths.py: Ensures consistent file pathing for configs.