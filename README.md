<h1>Website for an auto parts store from Europe</h1>
<p>The site was made from scratch. The data for the database was taken from the site <a href="https://bamper.by /" target="_blank">bamper.by </a>. As a front, so that the site could be viewed without pain in the eyes, I used Bootstrap 5. There are many plans for this project. For example, create a bot in Viber that will access the site API so that the client can specify the spare part he needs, and when the spare part appears in the database, notify the client about it.</p>
<br>
<h2>Done at the moment:</h2>
<p>- Data from the site has been parsed</p>
<p>- Django project was created and configured (initially)</p>
<p>- Created database tables on Postgres (without the products themselves)</p>
<p>- The admin panel is configured</p>
<p>- DRF is enabled</p>
<p>- Docker Is connected</p>
<br>
<h2>In the plans:</h2>
<p>- Increase DRF functionality</p>
<p>- Load at least 10% of spare parts</p>
<br>
<h1 margin="auto">How to install project with Docker?</h1>

1.   First of all, you need to clone the github repository:

    git clone https://github.com/VladYura/RD_Motors.git

2.   Go to the directory where you cloned the project in the terminal:

    cd /path/to/RD_Motors

3.   Run the app:

    docker compose up -d --build

***Now you can visit site on URL: http://localhost:8000***

***To go to the admin panel, write in the search bar:***

    http://localhost:8000/admin/

***Administrator Data:***

> user: admin

> password: admin
