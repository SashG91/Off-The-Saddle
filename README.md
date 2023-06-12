# OFF THE SADDLE - A COLLECTION OF UK CYCLE CLIMBS.

<img width="951" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/8602322f-8b39-409d-9c1e-e44302f67a02">

## Author
Sashen Govender

## Project Overview
*  The OFF THE SADDLE blog is a platform for cyclist of all ablities to visit and find out more about some of the most exciting and challenging cycle climbs in The UK who are either chasing their next King of the Mountain / Queen of the Mountain title or looking for something new and exciting.

* You can view the deployed website [here](https://off-the-saddle.herokuapp.com/).

## TABLE OF CONTENTS
- [OFF THE SADDLE - A COLLECTION OF UK CYCLE CLIMBS.](#off-the-saddle---a-collection-of-uk-cycle-climbs)
  * [Author](#author)
  * [Project Overview](#project-overview)
  * [TABLE OF CONTENTS](#table-of-contents)
  * [UX](#ux)
    + [Project Goal](#project-goal)
    + [User Stories](#user-stories)
  * [DESIGN CHOICES](#design-choices)
    + [Colors](#colors)
    + [Typography](#typography)
    + [Images/Icons](#images-icons)
    + [Animations](#animations)
    + [Responsiveness](#responsiveness)
  * [WIREFRAMES](#wireframes)
    + [Climb List](#climb-list)
    + [Climb Detail](#climb-detail)
  * [APP FEATURES / STRUCTURE](#app-features---structure)
    + [Navigation](#navigation)
    + [Climb List](#climb-list-1)
    + [Climb Detail](#climb-detail-1)
    + [Likes](#likes)
    + [Comments](#comments)
    + [Register](#register)
    + [Login/Logout](#login-logout)
    + [Footer](#footer)
    + [Error 404/403/500](#error-404-403-500)
    + [Features for Future Development](#features-for-future-development)
  * [DATA MODEL](#data-model)
  * [TESTING](#testing)
  * [DEPLOYMENT PROCESS](#deployment-process)
  * [TECHNOLOGIES USED](#technologies-used)
    + [Languages](#languages)
    + [Frameworks](#frameworks)
    + [Databases](#databases)
    + [Programs](#programs)
    + [Libraries and packs](#libraries-and-packs)
  * [CREDITS](#credits)
  * [MEDIA](#media)
  * [ACKNOWLEDGEMENTS](#acknowledgements)


## UX

### Project Goal
* The aim of the project is to provide a platform that hosts a collection of the most popular or unique cycling climbs in the UK, so that users have more information to better prepare for hill cycling in the region and share their experiences with other users.

### User Stories
- An agile approach was used to develop the project, developing small units of work in the form of user stories.
- These were managed and documented using a kanban style board on GitHub projects.
- The project board with the user stories can be found [here](https://github.com/users/SashG91/projects/3/views/1).

**For admin users:**

1. As an **admin user**, **I can access the admin panel using admin login details** so that I can **control and create the content for the blog**.
2. As an **admin user**, **I can approve/remove comments**, so that I can **maintain a friendly community atmospherefor the blog**.
3. As an **admin user**, **I can create sample / draft posts**, so that I can **finish writing or publishing content later** as an **admin user**.
4. As an **admin user**, **I can create, read, update and delete posts**, so that I can **maintain the blog content** as an **admin user**. 

**For sight users:**

5. As a **site user**, I can register an account so that I can interact with the posts.
6. As a **site user**, I can view a list of climb posts so that I can select one that interests me.
7. As a **site user**, I can click on a post so that I can read the full write-up of each climb post.
8. As a **site user**, I can view the number of likes on each post so that I can see which climbs are most popular among visitors.
9. As a **site user**, I can like a post so that I can engage with the content.
10. As a **site user**, I can view all comments on a post so that I can read other users impressions.
11. As a **site user**, I can leave comments on a post so that I can share my own thoughts or experience.
12. As a **site user**, I can edit and delete my comments on a post so that I can customise or remove my thoughts if desired.
13. As a **site user**, I can return to safety of the blog home page, so that I am diverted away from any loading errors should they arise.
14. As a **site user**, I can navigate to the social media links of the blog site, so that I can engage further with the community.
15. As a **site user**, I can safely login and logout of my account, so that I can keep my information safe.

## DESIGN CHOICES

### Colors
<img width="406" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/1180c083-76d7-4d0c-bf45-0f963fae4a8b">

- The colours chosen are expected to be easily viewed and readable. 
- The above color palette inspired the look and feel of the website.
- Lighter background used with darker text for accessibility purposes.
- The headings, icons and body text are darker to ensure clear contrast and readability for the user across the site.

### Typography
- The body text and headings uses the font of Oswald with a secondary font of sans-serif.
- This font for the body text was adopted from one of my previous cycling projects using Quicksand.
- Inspiration for this choice was drawn from [fontpair](https://www.fontpair.co/all).

### Images/Icons
- The icons were chosen to provide clear understanding of each climb and its characteristics such as distance, surface, elevation gain and so on.
- Each summary card has the same information structure, built using Bootstrap cards with all icons standard throughout the site.

### Animations
- All links have a color change and underlined effect when hovered for clear distinction from the body text.

### Responsiveness
- The website was designed mobile-first using flexbox to ensure responsiveness throughout the website.
- The structure of the nav bar and footer from Bootstrap allows for seemless transition from mobile to desktop view.

## WIREFRAMES
Below you will find explanations and screenshots of the intended outcome of the pages, with some deviations in the final product.

### Climb List
- The climb list page was designed using Bootstrap cards to show a quick summary of each climb write-up.
- The user has the ability to click and find out more about each climb.

<img width="746" alt="Screenshot 2023-01-27 at 20 20 37" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/08851663-d128-420b-8805-631d4aa9feae">

### Climb Detail
- Each blog post provides details about the climb such as difficulty, surface, distance and elevation gain.
- The registered user can also comment, like and include their segment time for each climb.

<img width="697" alt="Screenshot 2023-01-27 at 20 20 15" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/5105e486-ec15-485f-bdb2-7e9ed9ea0e0b">

## APP FEATURES / STRUCTURE

### Navigation

<img width="533" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/56a18874-3cc8-4078-b106-21b6f167c238">

<img width="390" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/b35743d8-d231-4287-91cf-d190744e1184">

- The users will see a home, login/logout & register button when visiting the site. 
- There is a hover state on each of the navigation items for better user experience.
- For mobile devices, the navigation will toggle to a hamburger menu.
- The user is able to easily return to the home page at any time using the bicycle logo at the top of the page.

### Climb List

<img width="279" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/cd2a1016-d43b-474a-83bf-6552f551cb7a">

- The users land on the home page and have a list of posts available with a title, excerpt and summary card associated with each climb.
- The image and title are linked, so users may click on either and be taken to the climb.
- There is a hover state on the title to show the user they can click on the post.
- This summary card is later repeated in each climb detail post for continuity across the site.

### Climb Detail

<img width="617" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/9aa8fc0b-9bce-4ec7-972d-d2c9c24325de">

- Each climb post has an article about providing more information if desired.
- If a user is logged in, they are able to interact with the post by commenting about their experience or liking the post.
- The structure of each post is consistent, starting with the card at the top and excerpt from the climb list and then the main content.

### Likes

<img width="188" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/31c8f78d-12d9-40cc-b947-b77d4d5bbb51">

<img width="179" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/36913130-82e8-406e-b9ba-a5bc054d0265">

- If a user is logged in, they can like the post (or unlike) and also see the climb likes count from other users.

### Comments

<img width="376" alt="Screenshot 2023-06-12 at 20 12 22" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/96661aaf-c2ba-4383-afa5-203222b5b240">

- For logged in users, a custom form with two fields is visible below the post to add their own experience of the ride and their time taken to finish.
- This allows users to engage with each other and share their experiences.

<img width="384" alt="Screenshot 2023-06-12 at 20 12 04" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/2cdd7043-59ec-4bc8-a698-9de01814c0d7">

- The user will be able to edit their comment and ride time and be alerted using a message.

<img width="407" alt="Screenshot 2023-06-12 at 20 11 21" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/c3359077-722e-4270-a45c-4c9a020c7025">

- The user will be able to delete their comment after being prompted and allowed to go back if desired or will proceed and receive a success message:

<img width="519" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/8437793a-62fa-43de-931e-0ce3953aee75">

- For posts without contributions, users will be encouraged to do so and have quick access to the sign up page via the provided links.
- If users are not logged in, they cannot make contributions to the posts.

### Register 

<img width="801" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/4613cfb4-92b3-49ac-86ca-b0ef1c5f7c7d">

- The user will be able to easily sign up using the below form built using Django allauth.
- Should user be registered, there is a link to easily navigate to login instead.

### Login/Logout 

<img width="897" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/e133e828-1a3e-44ab-bb81-36d599eec84d">

<img width="339" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/60eb79e4-5d67-4f01-9b00-dd9e30840202">

<img width="969" alt="Screenshot 2023-06-12 at 20 19 06" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/9c2e0db6-a258-4727-9a1d-c80dea16bcdd">

- The users can easily sign in with an option to 'remember me' if desired.
- If a user hasn't registered, there is a link to easily navigate to signup instead.
- The user is prompted with a message before logging out.
- The user will receive a message that disappears after 3 seconds to say they have logged in/logged out:

### Footer

<img width="690" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/5b0f7478-2b99-4156-8438-a6f714481916">

- The footer links directly to the social media pages of the cycle climb blog.
- It is responsive and includes additional information about the site owner.

### Error 404/403/500

<img width="1439" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/cfe6f7a8-af9f-47f9-b0b8-930f89272460">

- There are error pages in place in case a user is taken to a restricted area or the page does not exist.
- If the user clicks the home button they will be taken back to the blog list main page.
- The messages are designed to be informative and related to the theme of the site. 

### Features for Future Development
- Build a ranking feature where users can see their ride time for a climb segment according to other users on the same climb.
- Filter posts according to climb difficulty so that users can find the climbs that may be appropriate for me.
- Let users favourite/save a climb so that users can easily find ideas for future outings.
- Build upon the contributions, allowing users to have more statistics about themselves in an online profile. This was planned for using a third model however due to time contraints, it was integrated into the comment model to be built upon.

## DATA MODEL
- A relational database was designed between climb and comment model with a link to Django user authorisation.
- The comment model was based off 'I think, therefore I Blog' walkthrough project, with an addition of a DurationField as customisation.
- The Climb model was customised according to the data needed for the Off The Saddle blog concept.
- This included 2 choice fields for climb difficulty and climb surface.
- For climb length and elevation gain, this was represented as a decimal field.
- For KOM and QOM, this was represented by a TimeField

<img width="383" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/6e96c7df-974e-4bd1-b229-1f5482f5096b">

- [X] C - Site users can create/register an account to interact with the climb posts.
- [X] R - Site users can open and read the climb posts and read comments from other users.
- [X] U - Site users can like a post, updating the details and analytics for a post.
- [X] D - Site users can retract their like if desired on a climb post.

<img width="376" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/920502f2-ea1e-412b-bf24-3980bbd71040">

- [X] C - Site users can add their contributions/experiences to each climb using a customised form.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their ride experiences via a form.
- [X] D - Site users are able to delete their contributions.

## TESTING

Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

## DEPLOYMENT PROCESS

ElephantSQL
- Login to ElephantSQL, access the dashboard and create a new instance (input a name, choose tiny turtle, select a region).
- Return to the dashcoard, copy the URL.

Heroku
- Open a new app in Heroku, choose a unique name and region.
- Go to settings and add a new config var of DATABASE_URLpython with the value of the URL from ElephantSQL.
- Add host name of the Heroku app name to ALLOWED HOSTS in settings.py:

<img width="819" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/c63d5687-f58b-4b75-b00b-f3f566651578">

GitHub/GitPod
- Create a new repository on GitHub, open a new workspace with GitPod.
- Install django pip3 install 'django<4python to install Django 3.2 the LTS (Long Term Support) version.
- Create a new project and run the server to see if the app has installed.
- Run migrations, create a super-user with a username, email and password.
- Install  pip3 install dj_database_url==0.5.0 psycopg2 and freeze requirements  pip freeze > requirements.txt
- Add  import os and import dj_database_url to settings.py
- Connect the new database, paste in the ElephantSQL URL (do not commit at this stage):

<img width="816" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/c8b30b4f-764a-46f4-adce-91436c10aeb1">

- Confirm that connection to external database is made , run python3 manage.py showmigrations then run python3 manage.py migrate
- Create a new superuser for the new database.
- Create an if else statement to setup development and external databases:

<img width="802" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/a4272ab3-3ef1-4b26-a8f6-68992dec846c">

- Install pip3 install gunicorn and run pip freeze > requirements.txt
- Create a Procfile in the root directory and include web: gunicorn project_name.wsgi:applications
- Generate a SECRET_KEY, add it to Heroku config vars section.
- Create env.py file (ensure it is included in .gitignore file) and add the SECRET_KEY & DATABASE_URL to environment variables:

<img width="349" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/6fcad834-fd44-4e5d-9558-09a11feca66c">

- Edit settings.py to the below:
<img width="318" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/8562aa1a-dbc6-4170-aa9a-a6eaa75bd512">

<img width="210" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/c7cccb48-389b-4465-a856-83426a9575a9">

<img width="428" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/94085572-300f-424a-99e6-a89f55a14347">

- Add, commit and push to GitHub.
- Go to Heroku, add DISABLE_COLLECT_STATIC = 1 to Heroku config vars.
- Connect the project to the GitHub repository using personal account login.
- Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py (see screenshot above) & to Heroku config vars:
[Uploading image.png…]()

- Add cloudinary to installed apps in settings.py, add static/media file settings:

<img width="258" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/b77e3802-d29b-4a69-a9b0-5b7289f84ebc">

<img width="592" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/918131e6-c105-4b4b-89dd-23ea07ea0ddf">

- Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:

<img width="518" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/0d875ffb-f1e1-4437-b124-cc861ad9253a">

<img width="198" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/04f81921-5f60-4801-8cff-1d3ef1a6969f">

- Go to settings in Heroku and perform a manual deployment and check for any issues.
- Go to Heroku settings, enable automatic deployments.


## TECHNOLOGIES USED

### Languages
- HTML, CSS, JavaScript, Python

### Frameworks
- Django, Bootstrap

### Databases
- sqlite3, ElephantSQL

### Programs
- GitPod
- GitHub
- Cloudinary
- Crispy Forms
- Heroku
- Balsamiq

### Libraries and packs
- Font Awesome
- Django allauth
- Django Crispy Forms
- Summernote
- gunicorn
- psycopg2
- Favicon

## CREDITS
- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted with the basic setup, inspiration and structure for this project.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The Stockbook Project by Massimo Ranalli assisted with the setup of the edit/delete functions for comments as well as the messaging alerts.
- The blog content was inspired and written with help from the following websites [here](https://www.pedalsure.com/blog/5-hardest-climbs-in-the-uk) and [here](https://cyclinguphill.com/100-climbs/shibden-wall/)
- Big thanks to Daisy Mc Girr and her article on how to secure views via [Codu](https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to_)
- The following Django documentation [here]((https://www.geeksforgeeks.org/durationfield-django-forms/)) assisted with using DurationField in my models and forms.
- I learned a lot from [Seaside Sewing](https://github.com/kera-cudmore/seaside-sewing) by Kera Kudmore on how to setup a solid testing structure and documentation.

## MEDIA
- The fonts were chosen with guidance from [Google Fonts](https://fonts.google.com/) and inspiration drawn from [fontpair](https://www.fontpair.co/all)
- The colours for the website was generated using [ColorSpace](https://mycolor.space/)
- The climb images were sourced using [Cycling Uphill](https://cyclinguphill.com/) and PedalSure.
- The icons for the favicon, footer, about page and location headings were utilised from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor Malia for always helping and going above and beyond with providing feedback and support throughout the project process.
- The Code Institute Slack community for tips, guidance and motivation.
- The tutors at Code Institute for their patience and support.
