# Off The Saddle - Testing Content

## Contents

## Validation Testing
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, The HTML was checked by inspecting the page source and then running this through the validator.

- [Home Page]()
- [Climb Detail]()
- [Edit Comment]()
- [Sign up]()
- [Login]()
- [Logout]()
- [Error 404]()

### CSS
[W3C](https://validator.w3.org/) was used to validate the CSS.

- [static/css/style.css]()

### JavaScript
[JS Hint](https://jshint.com/) was used to validate the JavaScript.

- [static/js/script.js]()

### Python
[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

- [blog/urls.py]()
- [OFF_THE_SADDLE/views.py]()
- [OFF_THE_SADDLE/forms.py]()
- [OFF_THE_SADDLE/urls.py]()
- [OFF_THE_SADDLE/admin.py]()

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

#### Desktop Results

**Desktop performance:
- [Home Page]()
- [Climb Detail]()
- [Edit Comment]()

**Mobile performance:
- [Home Page]()
- [Climb Detail]()
- [Edit Comment]()

## Automated Testing
- Manual testing was done on user stories due to project time constraints.

## Manual Testing
- Each completed user story was tested against the acceptance criteria, see the corresponding screenshots as evidence.
- This included reviewing each feature to check the usability, visual design and performance.

## Outstanding Defects
- There are no outstanding major defects.
- The below design was a css issue that wasn't resolved before the final deadline but doesn't affect the functionality of the site.

![image](https://github.com/SashG91/Off-The-Saddle/assets/97494070/28801e3d-0eef-49be-bbc4-cb9a0c80e49d)

## Defects of Note
- 
