<h1 align="center">Habitual Living E-Commerce Website</h1>

The sites purpose was also to demonstrate the speed and convenience of buying online, with nice back end store builder features that makes the website a viable business tool.
[View the live project here.] https://habitual-living.herokuapp.com 

<h2 align="center"><img src="https://github.com/Benjamin144/habitual_living/blob/master/josephroberts.png"></h2> 

## Table of Contents
* [User Experience Design (UX)](#User-Experience-Design)
    * [My Strategy](#Strategy)
        * [My Goals](#Goals)
        * [User stories](#User-Stories)
    * [The Scope](#Scope)
    * [The Structure](#Structure)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframes)
        * [Database Design](#Database-Design)
        * [Security](#Security)
    * [The Surface Plane](#The-Surface-Plane)
        * [Design](#Design)
            * [Colour Scheme](#Colour-Scheme)
            * [Typography](#Typography)
            * [Imagery](#Imagery)
    * [Differences to Design](#Differences-to-Design)
- [Features](#Features)
    * [Existing Features](#Existing-Features)
    * [Future Features](#Features-Left-to-Implement)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Test Strategy](#Test-Strategy)
    * [Test Results](#Test-Results)
    * [Isses and Resolutions](#Issues-and-Resolutions-to-issues-found-during-testing)
* [Deployment](#Deployment)
    * [Project Creation](#Project-Creation)
    * [GitHub Pages](#Deployment-To-Heroku)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

****

## User Experience Design
### **Strategy**

My focus here is to lure buyers into purchasing a particular variety of product types for home environment.
The site is the foundation of a whole bigger enterprise as far as eccomerce sites go, but demonstrates the ease of use well.

#### Site Goals
* To eventually fashion buyers into buying products not always readily avaiable in general stores. 
* Using the website would be readily convenient where customers can expect regular updates to the products

#### User stories

* First Time Visitor Goals - Standard 'Just looking'

*   1. Standard Access window shopper ||  I want to easily view what I am buying so to make a purchase based on a product that I might not have known before visiting the site.
*   2. Standard Access window shopper ||  I want to easily visualize a products description to get a good understanding of what to expect from my purchase.  
*   3. Standard Access window shopper ||  I want to be able to differentiate between exotic items, and then decide on wether it's worth buying for the price
*   4. Standard Access window shopper ||  If I was to buy the product then there would need to be some way of seeing the generated amout of all my potential products
        
* A subscribed users Goals - Exclusive 'Ok I have signed up...now what'?

*   1. Exclusive Access subscribers   ||  I want to have exclusive membership to take advantage of any offers available
*   2. Exclusive Access subscribers   ||  Can I store my purchases in a shopping bag and come back to it later...I will need my own user profile, can I recover my account 
*   3. Exclusive Access subscribers   ||  Will I be notified as to wether I have joined as a subscriber. I really like the itinery of products

* Frequent User Goals - 'Not a bad place to shop to be fair'...

*   1. As a returning shopper ||  How easy is it for mr to find the items I need? - is there a system to make the process of finding the product easy, category, price..
*   2. As a returning shopper ||  I understand the product genre, if only I can find away to search what I need across abroad range of categories
*   3. As a returning shopper ||  if the produt wasn't available would theree be a way to leave feedback?

### **The Scope**

**Regular Tech Gadgets uploaded:**
* Creates, Reads, Updates Deletes.
* Log in/out protocols
* Stored item accessable by profiles
* Site works well on all screen sizes.
* Backend Django Admin for easy of use updating product set
* Defensive Design.

![POI_Importance and Difficulty](TBA.jpg)

### **The Structure Plane**

User Story:
> Site users are under no illusion that they are joining on to an eccomerce website offering

Branding:
* The brand of the website is in the name Habitual Living which is the site logo. Infact it is visable throughout to give off a strong engaged prescence.
* The Logo will always navigate back to the Home Page and displays Website purpose which is 'Ideas For Your Perfect Home'
* It has a pleasant, clean look and feel as a modern welcoming introduction with an eye catching red :orange: hover over :Red: button to entice one into the site 

Viewpoint:
> The site is easy to use ad designed for maximum efficiency with convenient buttons and nav links making for a pleasant experience

Mandatories:
* Navigational items, such as buttons and links are consistent and menus are available at all times.

Actuals:

Nav bars are always avaiable and once used will direct the site user to their page of choice. They might be intrigued at first by the navlink names.
They have immediate options to access a shopping bag regardless of whether they were subscribed. It's a handy way of luring the customer to eventually buy something
Beside the shopping trolley icon the user can choose to log, join by registering a subscription or simply leave a comment *not developed at the time of writing this*
There is a handy search bar above a marketing banner to help the user decide what to buy!
If you were switching to view the Site on a mobile, then you would be able to use a nice collapsable nav bar which is made accessable via the hamburger styles icon,
on the top left hand side of your device. Here you have different visual approach where the nav items are cascaded downwards on the LHS. 
Again the shopping bag and links to the product pages remain intact.

As far as navigation goes it flows like.....

* 'Habitual-Living'- (BrandLogoHome) 
* 'All products'   - (BreaksToFourAreas)    - 'Price'           - 'Rating'              - 'Category',         - 'All_Products',
* 'Luxury'         - (BreaksToFourAreas)    - 'Gourmet_Spa'     - 'Living_Space',       - 'Outdoor',          -'All_Luxury',
* 'Essentials'     - (BreaksToThreeAreas)   - 'Lighting_Sound', - 'Security_Data',      - 'All_Essentials',
* 'Exclusives'     - (BreaksToFourAreas)    - 'Discovery',      - 'Offers', 'Deals',    - 'All Exclusives',
* 'SearchField'    - (AddToBag)             -  (Toast),         - 'Secure_Checkout',    - 'Checkout',         -  'Complete_Order',   -  (Toast) 'Success', 
* 'My Account'     - (Subscribe)            -  'Sign Up',       - (Toast),              - 'Verify_Email'
* 'Sign In'        - (UserNameOrEmail)      -  'Home',
* 'Shopping Bag'   - (FullAccess)
* 'Products'       - (AddToBag)             -  (Toast),         - 'Secure_Checkout',    - 'Checkout',          - 'Complete_Order',   -  (Toast) 'Success', 
* 'Latest Deals'   - (Home)

Visuals

* Works accoss all screen sizes with zero horizontal push/pull back
* Media images are rendered well within the contstraints of their max width
* Dynamic [Bootstrap4] popout cards contain images of products, quantity & description
* Visually appealing 'mobile 1st' rsponsive design
* Neutral color schemes for eye comfort, prolonging screen time.

Operations

* Add profile pages, when logging in to account (after verification, fictional based development)
* Users can add product, update quantities, delete quantities.
* Superusers can maintain the site admin by adding, removing ad updating products and prices via both front and back end.
* When user signs up they can verify their credentials by recieving email in to their personal account thanks to 'STRIPE' webhooks.(fictional based development)
* A users purchase information can also be sent to the users inbox in like manner (fictional based development)
* Viable toast notifications avaiable as a visual communicator to users to inform them of various points of action on their journey throughout the site
* Defensive measure measures in place to prevent user accessing superuser admin privaledges

### **The Skeleton Plane**
#### Wireframes

**Final Wireframes**
(Images TBA)

**Original Design Wireframes**
(Images TBA)

#### Database Design
Django admin visuals:

#### Security

Database connection details are set up in environ.os settings for development, [True] 
and won't go through version control, the stored SECRET_KEYS in Gitpods workspace ENV correspond to those that are stored in the Heroku config variables. 


### **The Surface Plane**
### Design
#### Colour Scheme
Mainly Light gray, dark gray, black, orange, red, white yellow
I have used the color properties #73767a; #f54b48; #283342; #aab7c4; #3f4952 #f8f8f8; #7397a7; #000; #fff;  Black; White; across the site with
#6c757d; #28a745; #ffc107; #17a2b8; #f8f9fa; #343a40 as convenience colours from ['boostrap4']
Some of the Psychological properties of colours text in the project was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours) 
#F7EC36; #F7EC36; #FAAC42; #ec110d; #dc3545 

#### Typography
Nunito is used as the only font as it is 'a well balanced sans serif typeface'. provided by [GoogleFonts] - https://fonts.google.com/specimen/Nunito?preview.text_type=custom#glyphs

#### Imagery
The Landing page hosts a background image by 'Samantha Gades' '/media/samantha-gades-BlIhVfXbi9s-unsplash.jpg' taken from'['unsplash']

****
## Features

### Existing Features

* User notifications.
* Sign in / Sign out back end verification.
* Product set easy accessable
* Create feedback allowing all users to leave comments (under development).
* Profile page showing basic user information and events created by the user with modification ability.
* Mobile responsive design.


### Features Left to Implement

A feature to be included in the next release will allow users the ability to upload their own custom event posters. 
These will be displayed in the materialize collapsible elements along with the event information.

Admin login will be implemented in the next release to allow admin users to delete any events that may be inappropriate.
****
## Technologies
* [HTML](https://en.wikipedia.org/wiki/HTML)
	* This project uses HTML as the main language used to complete the structure of the Website.
* [CSS](https://en.wikipedia.org/wiki/CSS)
	* This project uses custom written CSS to style the Website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    * JavaScript is used along with [stripe](https://www.stripe.com/) for the email real time notification webhooks. 
    * [jQuery](https://jquery.com/) is used for the following: 
        * Mobile side nav
        * Displaying Success/Fail message verifying contact form status.
        * Scrollup Materialize elements.
        * To populate downdrops on select elements.
* [Python](https://www.python.org/)
    * This projects core was created using Python, the back-end logic and the means to run/view the Website.
    * Python Modules used (These can be found in the requirements.txt project file):
        Package             Version
        ------------------- -------
    *    asgiref             3.3.1
    *    boto3               1.17.40
    *    botocore            1.20.40
    *    dj-database-url     0.5.0
    *    Django              3.1.7   
    *    django-allauth      0.44.0
    *    django-countries    7.1
    *    django-crispy-forms 1.11.2
    *    django-storages     1.11.1
    *    gunicorn            20.1.0
    *    jmespath            0.10.0
    *    oauthlib            3.1.0
    *    Pillow              8.1.2
    *    postgres            3.0.0
    *    psycopg2-binary     2.8.6
    *    psycopg2-pool       1.1
    *    PyJWT               2.0.1
    *    python3-openid      3.2.0
    *    pytz                2021.1
    *    requests-oauthlib   1.3.0
    *    s3transfer          0.3.6
    *    sqlparse            0.4.1
    *    stripe              2.56.0

* [Django](https://www.djangoproject.com/)
    * MongoDB was used to create the document based databases(collections) used as data storage for this project.
* [Materialize](https://materializecss.com/)
    * The Materialize framework was used through the website for layout and responsiveness.
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used throughout the project to import the *Inter* and *Bevan* fonts.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website.
* [Git](https://git-scm.com/)
	* Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Heroku](https://dashboard.heroku.com/apps)
    * Heroku was used to deploy the live website.
* [TinyJPG](https://tinyjpg.com/)
	* TinyJPG/TinyPNG is used to reduce the file sizes of images before being deployed to reduce storage and bandwith.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [balsamiq Wireframes](https://balsamiq.com/wireframes/)
	* This was used to create wireframes for 'The Skeleton Plane' stage of UX design.
* [Font Awesome](https://fontawesome.com/)
    * All the Icons displayed throughout the website are Font Awesome icons.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon 
* [Techsini](http://techsini.com/multi-mockup/index.php)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README

****
## Testing

### Test Strategy
#### **Summary**
Testing is required on all features and user stories documented in this README. 
All clickable links must redirect to the correct pages. All forms linked to Django
must be tested to ensure they insert all given fields into the correct collections.

HTML Code must pass through the [W3C HTML Validator](https://validator.w3.org/#validate_by_uri).

CSS Code must pass through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

JavaScript code must pass through the [JSHint Validator](https://jshint.com/).

Python Code must pass through [PEP8 Validator](http://pep8online.com/)
#### **High Level Test Cases**
![Test Cases](readme_images/test_cases.JPG)

#### **Access Requirements**
Tester must have access to Django in order to manually verify the insertion 
of records to users and events collections.

#### **Regression Testing**
All features previous tested during development in a local environment must be regression 
tested in production on the live website.

#### **Assumptions and Dependencies**
Testing is dependent on the website being deployed live on Heroku.

#### **Out of Scope**
Only test cases listed under High Level Test Cases will be performed as part of this 
testing effort.

### Test Results

Full test results can be found [here](TESTING.md)TBA

****
## Deployment

### Project Creation
To create this project I used the CI Gitpod Full Template by navigating 
[here](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking the 'Use this template' button.

I was then directed to the create new repository from template page and entered in my desired repo name, then 
clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

The following commands were used for version control throughout the project:

* git add *filename* - This command was used to add files to the staging area before committing.

* git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

* git push - This command is used to push all committed changes to the GitHub repository.


### Deployment to Heroku

**Create application:**
1. Navigate to Heroku.com and login.
1. Click on the new button.
1. Select create new app.
1. Enter the app name.
1. Select region.

**Set up connection to Github Repository:**

1. Click the deploy tab and select GitHub - Connect to GitHub.
1. A prompt to find a github repository to connect to will then be displayed.
1. Enter the repository name for the project and click search.
1. Once the repo has been found, click the connect button.

**Set environment variables:**

Click the settings tab and then click the Reveal Config Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (database name you want to connect to)
4. key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and 
    dbname that you set up in the link).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).

**Enable automatic deployment:**
1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Run Locally

**Note: The project will not run locally with database connections unless the user sets up an [env.py](https://pypi.org/project/env.py/) file configuring IP, PORT, 
MONGO_URI, MONGO_DBNAME and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository 
for security purposes.**

1. Navigate to the GitHub [Repository](https://github.com/Benjamin144/Habitual-Living).
1. Click the Code drop down menu.
1. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1. Open your developement editor of choice and open a terminal window in a directory of your choice.
1. Use the 'git clone' command in terminal followed by the copied git URL.
1. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:
> pip install -r requirements.txt

### Fork Project 

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point 
for your own idea. - Definition from [Github Docs](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).

1. Navigate to the GitHub Repository you want to fork.
1. On the top right of the page under the header, click the fork button.
    
    ![Fork](readme_images/fork.JPG)
1. This will create a duplicate of the full project in your GitHub Repository.

****
## Credits

Background image - Taken from [unsplash](https://unsplash.com/) - '/media/samantha-gades-BlIhVfXbi9s-unsplash.jpg'


### Code

[Stack Overflow](https://stackoverflow.com/questions/35843675/link-to-a-specific-location-in-a-flask-template) - The code used to navigate 
to a specific section of a page using Flask templates was taken from here.

[Stack overflow](https://stackoverflow.com/questions/5272433/html5-form-required-attribute-set-custom-validation-message) - The code used to 
create custom error messages on invalid form inputs was copied and modified from this stack overflow post.

[Stack overflow](https://stackoverflow.com/questions/38964113/how-can-i-create-a-navbar-with-center-aligned-links-using-materialize) - The CSS 
used to center the nav bar was gotten from this stack overflow post. 

[W3Schools](https://www.w3schools.com/tags/tag_figcaption.asp) - The figure and caption code on the home page images was done by following 
a W3Schools tutorial.

JavaScript Validation function in scripts.js was code from course material for Task Manager App on the LMS. 

### Acknowledgements

I'd like to give special thanks to the the following people for their help with my project:
* Code Tutor James for providing me information on how to troubleshoot AWS Bucket policy and 404 + variable settings.
t

****
























### Skeleton

-   ### Design
    -   #### Colour Scheme
        -   I have used the colours #73767a; #f54b48; #283342; #aab7c4; #3f4952 #f8f8f8; #7397a7; #000; #fff;  Black; White; across the site with
            #6c757d; #28a745; #ffc107; #17a2b8; #f8f9fa; #343a40 as convenience colours from ['boostrap4']
            -   Some of the Psychological properties of colours text in the project was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours) - #F7EC36; #F7EC36; #FAAC42; #ec110d; #dc3545 
            
}
    -   #### Typography
        -   'nunito' fonts are the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. 
            I used Mitr as it is a sans serif styled font and it has a friendly feel iwhich I wanted to bring out in the site design layout, whilst nunito is known for being an easy to read font and rythmic 
            according to 'Google Fonts both are all relevant to readability, legibility, and overall texture in programming so I deemed them appropriate to use on this website.
    -   #### Imagery
        -   By  Samantha Gades url[/media/samantha-gades-BlIhVfXbi9s-unsplash.jpg'] took inspiration from the clean subtle look and ideal Home Life for some suited the overall look and feel of the website
 

[Landing Page](https://github.com/Benjamin144/My-Resume/blob/master/Landing.png)  <!--Heroku deployment links --> ??? https://habitual-living.herokuapp.com/ 

[About, Skills](https://github.com/Benjamin144/My-Resume/blob/master/Skills.png) <!--Heroku deployment links -->

[Contact](https://github.com/Benjamin144/My-Resume/blob/master/Contact.png) <!--Heroku deployment links -->

### Surface

My site has a modern, clean look and feel, using several background images on individual pages to create a "treat" throughout the website I use plenty of colours for my icons, fonts and other elements.

<p align="right">
  <a href="joseph-roberts-habitual-living--fourth-milestone-project">Back to Top :arrow_heading_up:</a> 
</p>

## Features

-   Responsive on all device sizes

-   Interactive elements

Most of the Features within my Portfolio are using the Bootstrap Front-end Component Libary
I have also used Animate.css which is a library of ready-to-use, cross-browser animations for use in your web projects. Great for emphasis, home pages, sliders, and attention-guiding hints.

My intention is to add my own live projects for my partners in business.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
3. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
5. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [Gimp:](https://www.gimp.org/)
    - Photo editing tool was used to resize some of the product images acros the project.
8. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.

    <p align="right">
  <a href="joseph-roberts-habitual-living--fourth-milestone-project">Back to Top :arrow_heading_up:</a> 
</p>

### Media

-   All Images were created by the Joseph Roberts.

## Testing

I have tested my portfolio using Chromes developer tools, and Browserstack
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.


-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the person.

        1. Upon entering the site, users are met with a solid deep bl ue navigation bar to go to explore a choice of three other pages. Beneath the nav bar the user is impacted by a dynamic full width background image that bears my full animated name and 
           job title. The user can click simultaneously switch between arrow and job title once clicked on scrolls down to the lower extremities of the page.  
        2. Once there the user will quickly understand the purpose of the website which really is pre marketing a call to action, considering me as a potential employee, candidate or collaborator.
        3. The user is free to scroll back up or back down the page to the footer, to see the details on how to stay in touch with me or choose to delve deeper into the website if still interested. With a handy 'back to the top' feature to save excessive scrolling.

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to aid the user in making simple traditional choices when navigating around the site and the use of catchy imagery has been chosen to maintain interest, throughout their journey.
           Each nav bar item is featured to keep the user engaged as much as possible with delayed hover/time effect. The logo in the top right hand corner is non desript and it's purpose is to lead the user to the homepage when on other pages of the site.
        2. In keeping with the home page style of presentation, I have kept the style very basic and honest with alot of white-space with symbolism. The idea behind this is to help the user push through the site as quickly as possible, only focussing in on what is necessary at the time of reading.
           I have therefore minimized my profile to a modal button where again the user can breifly access it or stay interested.
        3. When the user clicks on the Skills Page, they are met with more bold inviting images and quote to keep the user further engaged. Purpose being that it may help the user to focus on the content and information they were seeking. 
           The use of the carousel is to further confirm the skillset on offer by me as a Front end web developer and how I would rate myself.
        4. The user will be spending most of their time on this page, I have added a portfolio dropdown nav-item here so the user can see further examples of my learning of differing web development presentations.
           On the final Contact Page the user can easily scroll down to a section where they have an option to get in touch with me 
        

    3. As a First Time Visitor, I want to look for testimonials to understand what their users think of them and see if they are trusted. I also want to locate their social media links to see their following on social media to determine how trusted and known they are.
        1. Once the new visitor has read the About Us and What We Do text, they will notice the Why We are Loved So Much section.
        2. The user can also scroll to the bottom of any page on the site to locate social media links in the footer.
        3. At the bottom of the Contact Us page, the user is told underneath the form, that alternatively they can contact the organisation on social media links below which highlights the links to them.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the...................

        1. ...............................................................................................................................................
        2. ...............................................................................................................................................

    2. As a Returning Visitor, ...........................................................................................................................

        1. ...............................................................................................................................................
        2. ...............................................................................................................................................
        3. ...............................................................................................................................................
        4. ...............................................................................................................................................
        5. ...............................................................................................................................................

    3. As a Returning Visitor, ...........................................................................................................................

        1. ...............................................................................................................................................
        
-   #### Frequent User Goals

    1. As a Frequent User, ...............................................................................................................................

        1. ...............................................................................................................................................

    2. As a Frequent User, ...............................................................................................................................

        1. ...............................................................................................................................................



### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iphone6 iPhone7, iPhone 8 iPhoneX, iPad, iPad Pro and Pixel 2XL
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-  Running Heroku login from my developer environment will only work with <heroku login -i> command
-  Then run command <heroku config:set DISABLE_COLLECTSTATIC=1 --app habitual-living>
-  Unresolved bug with toast after signing in new user did not notify successful sign in or sign out.


### Deployment

## Heroku Deployment

The site is deployed published at https://habitual-living.herokuapp.com/ from my Herokuapp
My account is also connected to [https://github.com/Benjamin144/habitual-living] my Github page. When I navigate the the 'open app' buton in Heroku, the app loads normally without any problems.

When deploying to GitHub Pages with Heroku the following steps were taken...

1. I Logged in and created a new app on the Heroku platform by calling the new app Habitual Living for the EU region
2. I have then used the 'Postgres database' from within the resources tab of Heroku --provisioned under the free plan Hobby Dev - free
3. Addons included dj-database-url and psycopg2-binary were migrated and my json fixtures were also loaded into the project.
4. I was then allowed to create my superuser account to access the Django Admin pages.
5. By installing Gunicorn you can use it as the webserver and runs a Procfile to tell Heroku to create a web dyno to run Gunicorne to run this site.
6. The results after deploying to Heroku were

gitpod /workspace/Habitual-Living $ heroku config:set DISABLE_COLLECTSTATIC=1 --app habitual-living
Setting DISABLE_COLLECTSTATIC and restarting ⬢ habitual-living... done, v5
DISABLE_COLLECTSTATIC: 1
gitpod /workspace/Habitual-Living $ git add .
gitpod /workspace/Habitual-Living $ git commit -m "deploying to Heroku-2"
[master 4e6bfb3] deploying to Heroku-2
 3 files changed, 14 insertions(+), 7 deletions(-)
 create mode 100644 Procfile
gitpod /workspace/Habitual-Living $ git push
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 733 bytes | 733.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/Benjamin144/Habitual-Living.git
   f410265..4e6bfb3  master -> master
gitpod /workspace/Habitual-Living $ git push heroku master
fatal: 'heroku' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
gitpod /workspace/Habitual-Living $ heroku git:remote -a habitual_living
 ›   Error: Couldn't find that app.
 ›
 ›   Error ID: not_found
gitpod /workspace/Habitual-Living $ heroku git:remote -a habitual-living
set git remote heroku to https://git.heroku.com/habitual-living.git
gitpod /workspace/Habitual-Living $ git push heroku master
Enumerating objects: 1304, done.
Counting objects: 100% (1304/1304), done.
Delta compression using up to 16 threads
Compressing objects: 100% (482/482), done.
Writing objects: 100% (1304/1304), 17.57 MiB | 11.70 MiB/s, done.
Total 1304 (delta 664), reused 1290 (delta 657), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Building on the Heroku-20 stack
remote: -----> Determining which buildpack to use for this app
remote: -----> Python app detected
remote: -----> Installing python-3.6.13
remote: -----> Installing pip 20.1.1, setuptools 47.1.1 and wheel 0.34.2
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting asgiref==3.3.1
remote:          Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
remote:        Collecting dj-database-url==0.5.0
remote:          Downloading dj_database_url-0.5.0-py2.py3-none-any.whl (5.5 kB)
remote:        Collecting Django==3.1.7
remote:          Downloading Django-3.1.7-py3-none-any.whl (7.8 MB)
remote:        Collecting django-allauth==0.44.0
remote:          Downloading django-allauth-0.44.0.tar.gz (572 kB)
remote:        Collecting django-countries==7.1
remote:          Downloading django_countries-7.1-py3-none-any.whl (792 kB)
remote:        Collecting django-crispy-forms==1.11.2
remote:          Downloading django_crispy_forms-1.11.2-py3-none-any.whl (112 kB)
remote:        Collecting gunicorn==20.1.0
remote:          Downloading gunicorn-20.1.0.tar.gz (370 kB)
remote:        Collecting oauthlib==3.1.0
remote:          Downloading oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)
remote:        Collecting Pillow==8.1.2
remote:          Downloading Pillow-8.1.2-cp36-cp36m-manylinux1_x86_64.whl (2.2 MB)
remote:        Collecting psycopg2-binary==2.8.6
remote:          Downloading psycopg2_binary-2.8.6-cp36-cp36m-manylinux1_x86_64.whl (3.0 MB)
remote:        Collecting PyJWT==2.0.1
remote:          Downloading PyJWT-2.0.1-py3-none-any.whl (15 kB)
remote:        Collecting python3-openid==3.2.0
remote:          Downloading python3_openid-3.2.0-py3-none-any.whl (133 kB)
remote:        Collecting pytz==2021.1
remote:          Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
remote:        Collecting requests-oauthlib==1.3.0
remote:          Downloading requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
remote:        Collecting sqlparse==0.4.1
remote:          Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
remote:        Collecting stripe==2.56.0
remote:          Downloading stripe-2.56.0-py2.py3-none-any.whl (204 kB)
remote:        Collecting requests
remote:          Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
remote:        Collecting defusedxml
remote:          Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
remote:        Collecting certifi>=2017.4.17
remote:          Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
remote:        Collecting urllib3<1.27,>=1.21.1
remote:          Downloading urllib3-1.26.4-py2.py3-none-any.whl (153 kB)
remote:        Collecting idna<3,>=2.5
remote:          Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
remote:        Collecting chardet<5,>=3.0.2
remote:          Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
remote:        Building wheels for collected packages: django-allauth, gunicorn
remote:          Building wheel for django-allauth (setup.py): started
remote:          Building wheel for django-allauth (setup.py): finished with status 'done'
remote:          Created wheel for django-allauth: filename=django_allauth-0.44.0-py3-none-any.whl size=897448 sha256=7b9359899d48520d1470614a04e3fe945b9474d58bc0a1a92a9be2c4311499cc
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-a5u4ldmq/wheels/1f/48/08/742600c525478888d4ec4d304491a0299df29d55b372410dfe
remote:          Building wheel for gunicorn (setup.py): started
remote:          Building wheel for gunicorn (setup.py): finished with status 'done'
remote:          Created wheel for gunicorn: filename=gunicorn-20.1.0-py3-none-any.whl size=78918 sha256=d14b60143e46396c34b975d819ba8f422e17cb3fe8d6b19bae4bf88bb5a93c41
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-a5u4ldmq/wheels/9a/86/37/cad4bc71746b420e17c4eb0f5c41cf7b5e653c1fdbda27d198
remote:        Successfully built django-allauth gunicorn
remote:        Installing collected packages: asgiref, dj-database-url, pytz, sqlparse, Django, defusedxml, python3-openid, oauthlib, certifi, urllib3, idna, chardet, requests, requests-oauthlib, PyJWT, django-allauth, django-countries, django-crispy-forms, gunicorn, Pillow, psycopg2-binary, stripe
remote:        Successfully installed Django-3.1.7 Pillow-8.1.2 PyJWT-2.0.1 asgiref-3.3.1 certifi-2020.12.5 chardet-4.0.0 defusedxml-0.7.1 dj-database-url-0.5.0 django-allauth-0.44.0 django-countries-7.1 django-crispy-forms-1.11.2 gunicorn-20.1.0 idna-2.10 oauthlib-3.1.0 psycopg2-binary-2.8.6 python3-openid-3.2.0 pytz-2021.1 requests-2.25.1 requests-oauthlib-1.3.0 sqlparse-0.4.1 stripe-2.56.0 urllib3-1.26.4
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 72.5M
remote: -----> Launching...
remote:        Released v6
remote:        https://habitual-living.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/habitual-living.git
 * [new branch]      master -> master

7. You can then click on the Deploy tab in the Heroku menu bar and choose 'connect to GitHub' search for the repository at Github then connect that way.
8. I have enabled automatic deploys to automatically update Heroku
9. I have set DEBUG to 'True' under 'DEVELOPMENT' in local gitpod enviro/workspace settings.
10. All configs were pushed to Github and successfully deployed to Heroku.

## AWS S3 Deployment

1. Static files are stored in S3 o the Amazon Web Services bucket under Habitual-Living
2. I have editied the static website hosting and used the CORS config from [https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d90bfac64e564b41a177b65c34a63502/]
3. I have then used the AWS Policy generator to generate an S3 policy for Habitual-Living, with the GET object method. Then pasted in the ARN as <arn:aws:s3:::habitual-living>. 
    I then pasted in the policy into there bucket policy editor
4. I then accessed the access control list to and enabled the list for public access. 

## Amazon Identity & Access Management

1. I have created a group in IAM called [manage-habitual-living]for the site users.
2. I have also created an access policy giving the group access to the s3 bucket I created by importing a pre built policy supplied by AWS, namely[AmazonS3FullAccess]. In so doing I only want access to items within the habitual-living ARN.
3. All s3 actions are allowed with all actions now within the bucket because of this IAM policy update.
4. Now that this policy has been created, I have attached that policy to the S3 group......
5. I have also assigned a user to to the group named [habitual-living-staticfiles-user] with programmatic access keys, where the security policies are also attached.

### GitHub Pages

The project has been linked to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Benjamin144/habitualliving)

2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.


 git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY


7. Press Enter. Your local clone will be created.


 git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
Cloning into `CI-Clone`...

 Unpacking objects: 100% (10/10), done.


Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

<!-- ### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process. -->

## Unresolved Issues

- When leaving the shopping bag area and navigating to the home page to register or use the items from the dropdown menu. I noticed that the links were not clickable until I refreshed or click on the brand logo.
-  verifing email from local host is broken
-  edit | delete in added view is broken 

## Resolved Issues

- Ensuring SECRET_KEY was not pushed through version control - used local Gitpod settings to store secret key, operational STOP/START workspace to set environ.objects
- Static images wouldn't load in browser window - Bucket policy from AWS S3 was not saved and code missing. Resolved this by injecting the code content into the code editoring bucket window policy and re-saved.
- Unable to see email verification view after registering email - added 'block inner_content' template to properly render page.

## Credits

### Code

-   The full-screen hero image code came from this [Google Images Back End Server post](https://google.com)

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [cz8780](lawrencemcdaniel.com/home) : Inspired by this absolute Legend of a Web developer

-   [Stackoverflow)](https://stackoverflow.com/questions/19827605/change-bootstrap-navbar-collapse-breakpoint-without-using-less) : Change bootstrap navbar collapse breakpoint without using LESS

-   [The Code Institute](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+CF101+2017_T1/courseware/1f0ccaac7a3e43d895c1beae5363f46c/79eac486cc0c4c9aa54cbe54d009287c/?child=last) 
                    Took inspiration from a series of Code Institute Tutorials - This was one of my favorites.

### Acknowledgements

-   My Mentor Dick Vlaanderen for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

-   The Code Institute Slack community for their ongoing support.

### Acknowledgements

-   I received inspiration for this project throughout the Code Institutes course material.
    The concept of having the website perform in such a way was a result of seeing book readers deep interest in this lifestyle.


