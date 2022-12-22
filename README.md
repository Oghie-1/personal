<h2> This is a Personal Django Website Project Deployed on GCP<h2>
<hr>
<p>Built a personal website using Django, SQL, Bootstrap, and CSS. This website is built using the Django web framework, which is a powerful and popular    open-source web framework written in Python. The website uses a SQL database to store data and Bootstrap and CSS to style and layout the website's pages.</p>
<h3>Prerequisites<h3>
  <ul>
    <li>Python 3<li>
    <li>Django 2.2 or higher</li>
    <li>GCP account and project</li>
    <li>Google Cloud SDK installed and set up on your local machine</li>
  </ul>

<h3>Installation</h3>
<hr>
<h4>Clone the repository:<h4>
    git clone https://github.com/oghie-1/personal.git
    <p>Change into the project directory:</p>
    <p>cd personal</p>
 
<h3>Set up a Cloud SQL instance for the project's database:<h3>
    <p>Go to the Cloud SQL page in the GCP Console.
        Click the "Create instance" button.
        Follow the prompts to create a new Cloud SQL instance.
        Configure the Django project to use the Cloud SQL instance as its database:
        In the DATABASES setting in the Django settings file (usually settings.py), set the HOST, NAME, USER, and PASSWORD values to match your Cloud SQL             instance.</p>
<br>
<h3>Deploy the project to GCP App Engine:<3>
    <p>gcloud app deploy</p>

