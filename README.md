# Git Project Initialization Automation 

### Command:
```bash
  'create < project_NAME >'
  'create < project_NAME > <l>'   - init for locally
```   

### Git Commands we are Automating:
```bash
  $ git init
  $ touch README.md
  $ git add .
  $ git commit -m "Initial commit"
  $ git branch -M main
  $ git remote add origin <remote repo link>
  $ git push -u origin main
 
``` 

### Setup:
```bash
git clone https://github.com/mohitkhedkar/Git-Automation.git
cd Git-Automation
pip install -r requirements.txt
touch .env
  -Then open the .env file and store your username, password, and desired file destination. 
    Use the provided format at the bottom of this README.
```

### ENV file format:
```bash
USERNAME="Username123"
PASSWORD="123456789"
FILEPATH="D:\projects"
```

### Contibutors
1. [Megha Pal](https://github.com/meghapal02).
2. [Niraj Patil](https://github.com/niraj2347).
3. [Mohit Khedkar](https://github.com/mohitkhedkar).
