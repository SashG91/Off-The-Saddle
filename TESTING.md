# Off The Saddle - Testing Content

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/cacf57b9-dfcf-4248-8a4a-ddc932254382)

Testing was done throughout the build, with validations being checked often and accessibility suggestions implemented where possible. For outstanding defects and defects of note, please see below.

## Validation Testing
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, The HTML was checked by inspecting the page source and then running this through the validator.

- [Home Page](documentation/testing/home_page.png)
- [Climb Detail](documentation/testing/detail_page.png)
- [Edit Comment](documentation/testing/edit_page.png)
- [Sign up](documentation/testing/signup.png)
- [Login](documentation/testing/login.png)
- [Error 404](documentation/testing/error404.png)

**Take note:**
- The climb detail page had two warnings and two errors that were sourced to an issue with summernote and the rendering of the main blog content.
- None of the html issues were hardcoded and thus difficult to trace the root cause.
- Investigation of initial setup and configuration on the admin panel did not resolve the problem.
- The following articles were used to try rectify the issue [here](https://lists.w3.org/Archives/Public/www-validator/2011Aug/0011.html) and [here](https://stackoverflow.com/questions/12736598/element-name-gcsesearchbox-only-cannot-be-represented-as-xml-1-0).

### CSS
[W3C](https://validator.w3.org/) was used to validate the CSS.

- [static/css/style.css](documentation/testing/css.png)

### JavaScript
[JS Hint](https://jshint.com/) was used to validate the JavaScript.

- [static/js/script.js](documentation/testing/js.png)

### Python
[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python.

- [blog/urls.py](documentation/testing/blog-urls.png)
- [OFF_THE_SADDLE/views.py](documentation/testing/views.png)
- [OFF_THE_SADDLE/forms.py](documentation/testing/forms.png)
- [OFF_THE_SADDLE/urls.py](documentation/testing/urls.png)
- [OFF_THE_SADDLE/admin.py](documentation/testing/admin.png)

## Visual (UI) Testing: Cross Browser and Cross Device Testing
- The combination shown below of devices, browsers, and operating system were used to test the website. A range of screen sizes were checked to see if users would have the same experience across multiple devices and browsers. Priority was given to mobile devices and tablets as the blog was designed for a smaller size first.

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** | Passed 
|-----------------------------|------------------|---------|------------------|---------
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |Yes
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |Yes
| dev tools: Samsung S8+      | Chrome           | android | 360 x 740 px     |Yes
| real phone: iPhone 14 Pro   | safari           | iOs     | 390 x 844 px     |Yes
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |Yes
| real tablet: iPad           | Safari           | iOs     | 834 x 1075 px    |Yes
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |Yes
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |Yes
| browserstack                | Edge 113         | windows | 1440 x 672 px    |Yes

## Lighthouse
For the performance, accessibility, best practices and SEO of the site for mobile and desktop, [Page Speed](https://pagespeed.web.dev/) and the major pages were passed through the validation. 

**Desktop performance:**

- Home Page

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/bcded80b-7509-4c50-bf14-3f78943ed45e)

- Climb Detail

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/dd0b3405-911f-4b6e-ab5e-ef3c98d014a7)

- Edit Comment

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/00b8a585-2f26-481d-bcc9-0fbcb5d84c2a)

- Delete Comment

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/7e2a1e0c-08c5-47be-a836-cd447c84e821)

- Sign up

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/754ac454-83ae-4d00-b981-bbb6dfe3848a)

- Login

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/8b2ed13b-2634-41af-9c67-3de2e098c6e6)

**RESULTS:**
- Desktop performance was better than expected with speed index flagged as an area for improvement. 
- After investigating the issue [here](https://developer.chrome.com/docs/lighthouse/performance/time-to-first-byte/?utm_source=lighthouse&utm_medium=lr) it appears that Heroku might be causing a slower server response time or queries to the database using ElephantSQl could also be a factor.

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/99c114b6-0a32-4836-bf92-335df6cb36ce)

**Mobile performance:**

Home Page

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/42952b39-50c2-4e4e-aa31-6a231a50b5d1)

Climb Detail

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/76c28ecd-3b1c-4072-85ee-aecc6dbcb7b4)

Edit Comment

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/fa08129d-be56-4483-823f-2d6103557a87)

Delete Comment

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/89f1a674-9c53-44ef-831b-b3438635be45)

Sign up

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/9cb45565-0ae0-45f7-8936-86bc2c8ba21d)

Login

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/ab3a18e2-f3d7-42da-b1ae-08ab73a45a73)

**RESULTS:**
- Mobile performed well and had a different issue flagged with first contenful paint.
- This was caused by render blocking resources such as Cloudinary and Bootstrap.
- More investigations need to be done on how to rectify this after consulting the documentation [here](https://developer.chrome.com/docs/lighthouse/performance/render-blocking-resources/?utm_source=lighthouse&utm_medium=lr)

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/f803a9f9-fe6b-4560-ac91-fdf49e7c6877)

## Automated Testing
- Manual testing was done on user stories due to project time constraints.

## Manual Testing
- Each completed user story was tested with detailed steps of each feature [here](https://docs.google.com/spreadsheets/d/1iGQ1BSuya_-S_H4ncQ7NwuC3lc1k-G9Twlx2u8B5wZY/edit?usp=sharing). 
- These steps included validation of forms and any unhappy paths that a user might take.
- The matching user story is documented with the steps taken to fulfil it and a URL is provided for easier reference.
- You can see the corresponding screenshots of each feature as evidence in the README documentation.

**USER STORIES TESTED**
1. As an **admin user**, I can access the admin panel using admin login details so that I can control and create the content for the blog.
2. As an **admin user**, I can approve/remove comments, so that I can maintain a friendly community atmospherefor the blog.
3. As an **admin user**, I can create sample / draft posts, so that I can finish writing or publishing content later.
4. As an **admin user**, I can create, read, update and delete posts, so that I can maintain the blog content as an admin user. 
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

## Outstanding Defects
- There are no outstanding major defects that affect functionality of the site.
- The html validation for climb detail page remains unresolved and will be added to the next sprint as high priroty to fix. Please see above steps taken to rectify the issue.
- The below design was a css issue that wasn't resolved before the final deadline but doesn't affect the functionality of the site.

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/28801e3d-0eef-49be-bbc4-cb9a0c80e49d)

## Defects of Note
- The RideTime model relation between the comment and climb models was difficult to establish and issues arose with the foreign keys and calling rhe correct ids to save to the database and was thus removed for future features. More time and greater experience would allow for this addition to the site.
