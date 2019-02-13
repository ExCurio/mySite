postTitle = raw_input("Title for this post: ")
postDesc = raw_input("Description for this post: ")
postFile = raw_input("Python Filename: ") #Filename should equal newPost.zip


def addPost(postTitle, postDesc, postFile):
      file = open("C:\\inetpub\\wwwroot\\reports\WebShowCase.html","a")
      file.write("""<p><h3>Title: """+postTitle+"""</h3></p>
      <p>Description: """+postDesc+"""</p>
      <a href="../python/"""+postFile+"""">Here is the Python script used for my blog post!</a></br>     
      <p></br></body></br></html>""")
      file.close()
      


addPost(postTitle, postDesc, postFile)