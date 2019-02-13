file = open("C:\\inetpub\\wwwroot\\reports\WebShowCase.html","wt")
file.write("""<html>
                <head><title>Keith Harrison's WebShowcase</title></head>
                <body bgcolor=#00cc66>
                  <h1>Welcome to Keith Harrison's Weeks 4-7 WebShowcase Blog</h1>
                  <h2>Hello and welcome to my WebShowcase! Please make yourself at home!</h2>
                  </br>
                  </br>
                  <p><h3><a href = "../index.html">Home Page</a></h3></p>
                  </br>
                  </br>
                  <p><h3>Here is a picture of a Samurai, the ancient warriors of Japan!</h3></p>
                  </br>
                  <img src = "samurai2.jpg" style="width:300px;height:300px;">
                  </br>
                  </br>
                  <p><h3>Title: Week 4 Blog Post</h3></p>
                  <p>Description: This is my week 4 blog post!</p>
                  <p><a href = "../python/createPage.zip">Here is the Python Script used to initially create this web page!</a></p>
                  </br>
                  </br>
                </body>
              </html>""")
file.close()                  
                  