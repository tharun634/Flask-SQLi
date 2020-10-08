# Flask-SQLi
A simple flask application which is prone to SQLi and a patch for it

- Exploit in action : [demo video](https://drive.google.com/file/d/1w5HswP9uUZESLwaoMwzL26hvT1D5uKul/view?usp=sharing "demo video")
- Payload used for injection : `' OR '"'='"`

## Steps to run the app
  - Install [Python](https://www.python.org/downloads/ "Python") 
  - Install the necessary pip modules 
  
 ` pip install Flask`

  `pip install Flask-MySQLdb`
  - Run the app.py from /Exploitable app and navigate to http://127.0.0.1:5000/login/ to inject the payload
  - Run the app.py from /Patched app and navigate to http://127.0.0.1:5000/login/ to inject the payload and see that it is not exploitable
  