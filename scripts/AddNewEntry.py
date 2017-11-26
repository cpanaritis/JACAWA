#!/usr/bin/env python
import cgi
import csv
import requests
import json
print "Content-type: text/html\n\n"

form = cgi.FieldStorage()
def IDgenerator(dob, fname, lname):
    
    dob = dob.split("/")
    
    dob[0] = dob[0][2:]
    
    fname = list(fname)
    lname = list(lname)
    
    
    
    ID = dob[2] + dob[1] + dob[0] + str(ord(fname[0])-65) + str(ord(fname[1])-65) + str(ord(fname[2])-65) + str(ord(lname[0])-65) + str(ord(lname[1])-65) + str(ord(lname[2])-65)
    
    return ID
dob = form["DOB"].value
year = dob.split("/")[0]
fName = form["fname"].value
lName = form["lname"].value
phone = form["phone"].value
email = form["email"].value
destination = form["destination"].value
image = form["image"].value
#image = ID+".jpg"
hs = form["health"].value
ID = IDgenerator(dob, fName, lName)
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
city = j['city']
filename = year+".csv"
f = open(filename, 'a')
f.write(ID + ", " + dob + ", "+fName + ", "+ lName + ", " + phone +", "+ email +", "+ city + ", " + destination +", " + image + ", "+ hs +"\n")
f.close()
success = """ <!DOCTYPE html>
    <html lang="en" >
    <head>
    <meta charset="UTF-8">
    <title>Search Form</title>
    <link href='https://fonts.googleapis.com/css?family=Titillium+Web:400,300,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
    <link rel="stylesheet" href="../css/style.css">
    </head>
    
    <body>
    <img class="altLogo" src = "../Logo/Jacawa.svg" alt="logo"/>
    <div class="form">
    <div class="tab-content">
    <div id="search">
    <h1>User Added! Search for an Exisiting Refugee</h1>
    
    <form action="./search.py" method="post">
    
    <div class="top-row">
    <div class="field-wrap">
    <label>
    First Name<span class="req">*</span>
    </label>
    <input type="text" name="fname" required autocomplete="off" />
    </div>
    
    <div class="field-wrap">
    <label>
    Last Name<span class="req">*</span>
    </label>
    <input type="text" name="lname" required autocomplete="off"/>
    </div>
    </div>
    
    <div class="bottom-row">
    
    <div class="field-wrap">
    <label>
    DOB (yyyy/mm/dd)<span class="req">*</span>
    </label>
    <input type="DOB" name="DOB" required autocomplete="off"/>
    </div>
    </div>
    
    <button type="submit" class="button button-block"/>Search</button><br>
    </form>
    <form action="../new_refugee.html" method="post">
    <button type="submit" class="button button-block"/>New Entry</button><br>
    </form>
    <form action="../index.html" method="post">
    <button type="submit" class="button button-block"/>Exit</button>
    </form>
    </div>
    
    <div id="login">
    </div>
    
    </div><!-- tab-content -->
    
    </div> <!-- /form -->
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    
    <script  src="../js/index.js"></script>
    </body>
    </html>
    """
print success
