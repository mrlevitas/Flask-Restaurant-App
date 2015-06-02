To run the Restaurant Web App project:


1. Install Git, Virtualbox to run a VM, and Vagrant to configure and manage it.
   Instructions can be found here:
   https://www.udacity.com/wiki/ud197/install-vagrant

   This allows us to run the webapp from a VM where the ports have been forwarded and the application can run locally on localhost.

2. Make sure the cloned repository is located in GitHub\fullstack\vagrant\Flask-Restaurant-App so that vagrant recognizes the shared 
   folder between your VM and local machine

3. Navigate to the /vagrant/fullstack/Flask-Restaurant-App directory inside the vagrant environment

4. run database_setup.py to create the database

5. run lotsofmenus.py to populate the database

6. run restaurant_app.py and navigate to localhost:5000 in your browser