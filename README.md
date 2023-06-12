# OFF THE SADDLE - A COLLECTION OF UK CYCLE CLIMBS.

## Author
Sashen Govender

## Project Overview
*  The OFF THE SADDLE blog is a platform for cyclist of all ablities to visit and find out more about some of the most exciting and challenging cycle climbs in The UK who are either chasing their next King of the Mountain / Queen of the Mountain title.

* You can view the deployed website [here](https://off-the-saddle.herokuapp.com/).

## TABLE OF CONTENTS

## UX

### Project Goal
* The aim of the project is to provides a platform that hosts a collection of the most popular or unique cycling climbs in the UK, so that users have more information to better prepare for hill cycling in The UK and share their experiences with other users.

### User Stories
* For admin users:
1. In order to **control and create the content for the blog** as an **admin user**, **I can access the admin panel using admin login details.**
2. In order to **maintain a friendly community atmospherefor the blog** as an **admin user**, **I can approve/remove comments.**
3. In order to **finish writing or publishing content later** as an **admin user**, **I can create sample / draft posts.**
4. In order to **maintain the blog content** as an **admin user**, **I can create, read, update and delete posts** using the admin panel.

Have the ability to maintain the blog content as an admin user, I can create, read, update and delete all posts.

* For sight users:
5. As a **site user**, I can register an account so that I can interact with the posts.
6. As a **site user**, I can view a list of climb posts so that I can select one that interests me.
7. As a **site user**, I can click on a post so that I can read the full write-up of each climb post.
8. As a **site user**, I can view the number of likes on each post so that I can see which climbs are most popular among visitors.
9. As a **site user**, I can like a post so that I can engage with the content.
10. As a **site user**, I can view all comments on a post so that I can read other users impressions.
11. As a **site user**, I can leave comments on a post so that I can share my own thoughts or experience.
12. As a **site user**, I can edit and delete my comments on a post so that I can customise or remove my thoughts if desired.
13. As a **site user**, I can return to safety of the blog home page, so that I am diverted away from any loading errors should they arise.

## DESIGN CHOICES

### Colors
- The colours chosen are expected to be easily viewed and readable. Lighter backgroung with darker text.
- The headings, icons and body text are darker to ensure clear contrast and readability for the user across the site.

### Typography
- The body text and headings uses the font of Oswald with a secondary font of sans-serif.
- This font for the body text was adopted from one of my previous cycling projects.

### Images/Icons
- The icons were chosen to provide clear understanding of each climb and its characteristics such as distance, surface, elevation gain and so on.
- Each summary card has the same information structure with all icons standard throughout the site.

### Animations
- The navbar, social icons and buttons across the site have a subtle grow effect when hovered over by the user.
- All links have a color change and underlined effect when hovered for clear distinction from the body text.

### Responsiveness
- The website was designed mobile-first using flexbox to ensure responsiveness throughout the website.
- The standard grid from Bootstrap was used to achieve this.

## WIREFRAMES
Below you will find explanations and screenshots of the intended outcome of the pages, with some deviations in the final product.

### Climb List
- The climb list page was designed using cards to show a quick summary of each climb write-up.
- The user has the ability to click and find out more about each climb.

<img width="746" alt="Screenshot 2023-01-27 at 20 20 37" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/08851663-d128-420b-8805-631d4aa9feae">

### Climb Detail
- Each blog post provides details about the climb such as difficulty, surface, distance and elevation gain.
- The registered user can also comment, like and include their segment time for each climb.

<img width="697" alt="Screenshot 2023-01-27 at 20 20 15" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/5105e486-ec15-485f-bdb2-7e9ed9ea0e0b">


## APP FEATURES / STRUCTURE

### Navigation
- The users will see a home, login/logout & register button when visiting the site. 
- There is a hover state on each of the navigation items for better user experience.
- For mobile devices, the navigation will toggle to a hamburger menu.

### Climb List
- The users will have a list of posts with a title, excerpt and summary card associated with each climb.
- The image and title are linked, so users may click on either and be taken to the climb.
- There is a hover state on the title to show the user they can click on the post.
- This summary card is later repeated in each climb detail post for continuity across the site.

[INSERT SCREENSHOTS HERE]

### Climb Detail
- Each climb post has an article about the climb.
- The structure of each post is consistent, starting with the card at the top and excerpt from the climb list and then the main content.

[INSERT SCREENSHOTS HERE]

### Likes
- Should a user not be logged in, they will see the below information:

[INSERT SCREENSHOTS HERE]

- Should the user be logged in, they will be able to like the post:

[INSERT SCREENSHOTS HERE]

- The user is then able to easily return to the home page using the go back button or clicking the bicycle logo at the top of the page.

### Comments
- If a post doesn't have any comments, the user will see the below if not logged in:

[INSERT SCREENSHOTS HERE]

- A logged in user, will be encouraged to share their experience if they have completed a featured climb.

[INSERT SCREENSHOTS HERE]

- The user will be able to edit their comment and RideTime using a form and be alerted using a message that disappears after several seconds.
- The user will be able to delete their comment after being prompted and allowed to go back if desired or will proceed and receive a success message:

[INSERT SCREENSHOTS HERE]

[INSERT SCREENSHOTS HERE]

- A logged in user, will be encouraged to input their RideTime for the climb segment if they have completed it.

[INSERT SCREENSHOTS HERE]

### Register 
- The user will be able to easily sign up as a user using the below form.
- Should user already be registered, there is a link to easily navigate to login instead

[INSERT SCREENSHOTS HERE]

### Login/Logout 
- The users can easily sign in using the below form with an option to 'remember me' if desired.
- If a user hasn't registered, there is a link to easily navigate to sign up instead.

[INSERT SCREENSHOTS HERE]

- The user is prompted with a message before logging out:

[INSERT SCREENSHOTS HERE]

- The user will receive a message that disappears after 3 seconds to say they have logged in/logged out:
[INSERT SCREENSHOTS HERE]

### Footer
- The footer links directly to the social media pages of the cycle climb blog.
- There is a subtle hover state on each icon for better user experience.

### Error 404/403/500
- There are error pages in place in case a user is taken to a restricted area or the page does not exist.
- If the user clicks the home button they will be taken back to the blog list page.

[INSERT SCREENSHOTS HERE]

### Features for Future Development
- Once the site contains many lists of posts it will be less time consuming to all the user to use the search bar to quickly search for a climb by area to find a climb that interests them.
- Users will benefit from being able to 'save' blog posts so that users can plan future rides in specific regions.
- Users will be able to see where their RideTime for a climb segment is ranked according to other users on the same climb in a leaderboard for this blog.
- Comments that are in pending state can be added so users are aware they are awaiting approval from the admin.
- Give users the ability to filter according to climb difficulty so that users can find the climbs that may be appropriate for me.
- Give users the abilitiy to favourite/save a climb I am interested in so that users can easily find ideas for future outings.
- Give users the ability to rate blog posts on a scale of 1-5 so that users can give feedback about which posts I find valuable.


## DATA MODEL
- A relational database was designed between climb and comment model with a link to Django user authorisation.
- The comment model was based off 'I think, therefore I Blog' walkthrough project.
- The Climb model was customised according to the data needed for the Off The Saddle blog concept.
- This included 2 choice fields for climb difficulty and climb surface.
- For climb length and elevation gain, this was represented as a decimal field.
- For KOM and QOM, this was represented by a TimeField
<img width="373" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/cb6f4b2e-0f6e-4a61-a7e9-7131e26c8aa0">


- [X] C - Site users can create/register an account to interact with the climb posts.
- [X] R - Site users can open and read the climb posts and read comments from other users.
- [X] U - Site users can like a post, updating the details and analytics for a post.
- [X] D - Site users can retract their like if desired on a climb post.

<img width="367" alt="image" src="https://github.com/SashG91/Off-The-Saddle/assets/97494070/573bbdaa-a148-479d-a829-306f01c336bb">


- [X] C - Site users can create comments using a form on each climb post.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their comments via a form.
- [X] D - Site users are able to delete their comments.

## TESTING

Please refer to the (TESTING.md) file for all testing performed.

## DEPLOYMENT PROCESS
**Step 1:** Open a new app in Heroku, choose a unique name and region.
**Step 2:** Login to ElephantSQL, access the dashboard and create a new instance (input a name, select a region).
**Step 3:** Return to the dashboard and copy the database URL:
[INSERT SCREENSHOT HERE]

**Step 4:** Create env.py file (ensure it is included in .gitignore file) and add environment the below variables. Paste the URL from above:
[INSERT SCREENSHOT HERE]

**Step 5:** Include a secret key in the variables:
[INSERT SCREENSHOT HERE]

**Step 6:**
Include the below code to settings.py file:
[INSERT SCREENSHOT HERE]

**Step 7:** Link the database in settings.py and migrate then push to GitHub:
[INSERT SCREENSHOT HERE]

**Step 8:** In Heroku, add three config vars:
[INSERT SCREENSHOT HERE]

**Step 9:** Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py (see screenshot above) & to Heroku config vars:
[INSERT SCREENSHOT HERE]

**Step 10:** Add cloudinary to installed apps in settings.py, add static/media file settings:
[INSERT SCREENSHOT HERE]

**Step 11:** Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:
[INSERT SCREENSHOT HERE]

**Step 12:** Create a Procfile, then commit and push to GitHub:
[INSERT SCREENSHOT HERE]

**Step 13:** Connect GitHub account in Heroku, connect and deploy branch. Open app and check:
[INSERT SCREENSHOT HERE]


## TECHNOLOGIES USED

## Languages
- HTML, CSS, JavaScript, Python

## Frameworks
- Django, Bootstrap

## Databases
- sqlite3, ElephantSQL

## Programs
- GitPod
- GitHub
- Cloudinary
- Crispy Forms
- Heroku
- Balsamiq

## Libraries and packs
- Font Awesome
- Django allauth
- Django Crispy Forms
- Summernote
- gunicorn
- psycopg2
- Favicon

## CREDITS
- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted with the basic setup and structure for this project.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The Stockbook Project by Massimo Ranalli assisted with the setup of the edit/delete functions for comments as well as the messaging alerts.
- The blog content was written with help from the following websites [here](https://www.pedalsure.com/blog/5-hardest-climbs-in-the-uk) and [here](https://cyclinguphill.com/100-climbs/shibden-wall/)

## MEDIA
- The fonts were chosen with guidance from
- The colors for the website was generated using 
- The climb images were sourced using cyclinguphill.com and pedalsure.
- The icons for the favicon, footer, about page and location headings were taken from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor Malia for always helping and going above and beyond with providing feedback and support throughout the project process.
- The Code Institute Slack community for tips, guidance and motivation.
- The tutors at Code Institute for their patience and support.
