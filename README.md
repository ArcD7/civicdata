# CivicDataLab Assignment
The goal is to create a website where users can upload their data (.csv files) and can download other datasets from the database.

## API Endpoints available
- Fetch all datasets :- [name](url)
- Upload dataset :- [name](url)
- Information about a dataset along with file download:- [name](url)

## How to run the code locally?
- Clone the repository.
- Create a virtual environment and install the dependencies using the command
  ```
  pip3 install -r requirements.txt
  ```
- In the civicdata/settings.py file change the db setting to your postgres server.
  > We are using postgres as a database here
- Run the commands `python3 manage.py makemigrations` and `python3 manage.py migrate`.
- Run the command `python3 manage.py runserver` to start a local server.
- Go to **http://127.0.0.1:8000** and your website is up and running.

## The process 
- The main objective of the app is to let users upload their open data (one or many files) along with some metadata such as name, description and tags.
- Since a user may upload multiple files we need to maintain tables which will hold the data such as name, description, tags and another table which holds the details about the files that were uploaded by the user.
  - We have two tables, 
    - `ResourceIndex`, which holds the data such as name, description, tags.
    - `FileManagement`, which manages the files uploaded by the user. 
      > This table has *resource_id* of ResourceIndex as a _Foreign Key_ to have a one-to-may relationship b/w them. 
- *How each API works?*
  - _Fetch all datasets_ - Works by querying on table `ResourceIndex` which fetches all the rows from it and is then rendered as a list.
  - _Upload dataset_ - It makes use of django forms to retrieve the data from the user and then add it to the `ResourceIndex` table and each file is added to the `FileManagement` table.
  - _Information about a dataset along with file download_ 
    - _Information about a datase_ - It queries the table `ResourceIndex` on column `name` and sends the data to the template to be rendered.
    - _File Download_ - It queries the `FileManagement` table and then combines the files in a *.zip* file and sends it to the user.
