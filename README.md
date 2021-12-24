# KOHA-Borrower-Backup

This is a simple script to log in and download the borrower.db file from your KOHA install for use in KOHA Offline.

With this script you can automate the download of your borrower.db file so if KOHA goes down, you can be content that you have the latest version of your borrower.db file without having to remember to update it manually.

It was written in python 3.10.1 and requires the following libraries:
- beautifulsoup4 4.10.0
- PyYAML 6.0
- requests 2.26.0

## Installation
- **Before Downloading** - Make sure you have Python 3 downloaded and installed. I wrote the program on python 3.10.1, but it doesn't do anything too fancy so I don't see any reason it wouldn't work in 3.8+. You can download python from https://www.python.org/downloads/
1. Download the latest release from the releases page
2. Extract the files to the desired location you want to run the script from. Please be aware of file permissions, if you extract it to a place the program won't have permission to read or write to, you will run into issues. Running the script from userspace (Something like "C:\Users\$USER\Documents" on Windows or "/home/$USER" on Linux) should be fine for most situations.
3. use pip to install the needed libraries, open a terminal and navigate to the directory you extracted the files to within the terminal, then run:
`pip install -r requirements.txt`
4. After pip finishes installing the required libraries, the script is ready to configure and run.

## Configuration
1. Open up `config.yml` in the text editor of your choice
2. Update the fields to match your KOHA installs information. For most installs, you will just need to replace the username, password, branch, and the base URLs (the bit before /cgi-bin/). 
- The KOHA user has to have access to the tools section that includes the borrowers.db file we're downloading, so make sure the user you're using can do that before adding it.
3. If your login form has extra fields, you should be able to add them to the form_input list, just make sure you indent the new lines with spaces, not tabs (YAML really hates tabs) and the names of the ids for the fields are used before the values (for example, say there was a check box that needed checked that had the ID "human_check" you would add the line `human_check: checked` after `register_id`
4. destination is the location and name the output file is given. The script will not create directories, so make sure the directory exists before running the script. It's a good idea to open this file in a text editor to make sure it's actually a database. If the login failed, it will instead show HTML, if it does this, check your login information, if everything looks correct, submit a ticket.
5. Once you have updated `config.yml` with the relevant information, save the file. You can now run the script. The simplest way to run it is by navigating to the directory the file is located in a terminal and running `python.exe borrowerbak.py` on windows or `python3 borrowerbak.py` on linux.
