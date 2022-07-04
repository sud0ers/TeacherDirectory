# Teacher-Directory
A client has requested we create a Directory app containing all the Teachers in a given school. 

Each teacher should have the following information
<ul>
  
<li>First Name</li>
<li>Last Name</li>
<li>Profile picture</li>
<li>Email Address</li>
<li>Phone Number</li>
<li>Room Number</li>
<li>Subjects taught</li>
</ul>  

Teachers can have the same first name and last name but their email address should be unique

A teacher can teach no more than 5 subjects

The directory should allow Teachers to filtered by first letter of last name or by subject.

You should be able to click on a teach in the directory and open up the profile page. From there you 
can see all details for the teacher.

An Importer will be needed to allow Teachers details to be added to the system in bulk. This should
be secure so only logged in users can run the importer.

The CSV attached contains a list of teacher who need to be uploaded as well as the filename for the 
profile image. Profile images are in the attached Zip file.
if an image is not present for the profile then you should use a default placeholder image.

You can use SQLite for the database backend for simplicity

