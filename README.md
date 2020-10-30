<h1 align="center">Helpdesk-Micro</h1>

[View the live project here.](http://helpdesk-pengols.herokuapp.com/)

A primarily desktop focussed website, Helpdesk-Micro is designed for small internal IT teams to be able to log and manage Helpdesk tickets for their organisation.  Users are able to create tickets and add and delete updates.  They will also be able to add, edit and delete both end users and administrative users. The website is inaccessible without a login.

<h2 align="center"><img src="https://##"></h2>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want easily manage, create and complete IT Helpdesk calls for my organisation.
        2. As a First Time Visitor, I want.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want.
        2. As a Returning Visitor, I want.

    -   #### Frequent User Goals
        1. As a Frequent User, I want.
        2. As a Frequent User, I want.

-   ### Design
    -   #### Colour Scheme
        - ##### Navbar and buttons
            The site uses two primary, contrasting colours to help keep buttons and navbar defined and easily distinguishable.  
            ![Color](documentation/images/primary-color.PNG)

    -   #### Typography
        -   There are two primary fonts for the website - Press Start P2 & VT323. Sans Serif is used as the fallback font, in case for any reason, the fonts aren't being imported into the site correctly. Both Press Start P2 and VT323 are evocative of the fonts used in video games throughout the decade.  I have used Press Start P2 for buttons and titles and VT323 for larger pieces of text as it is easier to read.
    -   #### Imagery
        -   The background image is designed to be evocative of vector designs from the era. It has a nostalgic aesthetic and uses neon pink and purple from which the site takes design cues. The card images are chosen to reflect pop culture and technology from the decade.

   ### Wireframes

    -   Home Page Wireframe for Desktop & Mobile - [View](https://##)

    -   Game page Wireframe for Desktop - [View](https://##)

    -   Game page Wireframe for Mobile - [View](https://##)

## Features

-   Responsive on all device sizes.



-   Interactive JavaScript elements including modals, overlays and a gameboard.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [Flask:](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is a micro web framework written in Python.
1. [MongoDB Atlas:](https://www.mongodb.com/cloud/atlas)
    - MongoDB Atlas is a cloud database service.
1. [Materialize 1.0.0:](https://materializecss.com/getting-started.html)
    - Materialize was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Press Start P2' and 'VT323' fonts into the style.css file which is used on all pages throughout the project.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Materialize to make the navbar responsive.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Gitpod:](https://gitpod.io/)
    - Gitpod was used as the IDE for creating the project.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate the HTML and CSS of the project to ensure there were no syntax errors.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

The Esprima JavaScript Syntax Validator & JSHint were used to validate the JavaScript of the project.

-   [Esprima JavaScript Syntax Validator](https://esprima.org/demo/validate.html)
-   [JSHint](https://jshint.com/)

The Esprima JavaScript Syntax Validator & JSHint were used to validate the JavaScript of the project.

-   [ExtendsClass Python Syntax Checker](https://extendsclass.com/python-tester.html)
-   [PEP8 online](http://pep8online.com/)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want easily manage, create and complete IT Helpdesk calls for my organisation.

        1. Upon entering the site, after login, users are greeted with a clean and easily readable navigation bar and a list of all existing helpdesk tickets.

    2. As a First Time Visitor, I want to reminisce about the 80's.

        1. The site is deliberately styled with a retro feel to invoke nostalgic feelings for the user.
        2. The game cards contain images from the decade which should invoke those same nostalgic feelings.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to see if I can better my previous score.

        1. The victory modal that shows on the completion of the game gives the player a rating out of three stars enabling them to know if their score can be bettered.
        2. Total moves and total time are also shown on the victory modal so the player can aim to improve time taken and moves made on subsequent attempts.

    2. As a Returning Visitor, I want to find social links to the creator.

        1. A link to the creators GitHub is visible in the footer on all pages.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added difficulty levels.

        1. The user would already be comfortable with the website layout and can see if any difficulty levels have been added on navigating to the game page.

    2. As a Frequent User, I want to check to see if there are any new images, music or graphics.

        1. The user would already be comfortable with the website layout and new changes would be immediately visible.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Mozilla Firefox browsers for desktop.
-   The website was tested on Google Chrome, Safari, Samsung Internet and Amazon Silk on mobile devices.
-   The website was viewed on a variety of devices such as Windows Desktop, Windows Laptop, Samsung S8, Samsung S9, Samsung S3 tablet, Motorola G4, Amazon Fire, iPhone7, iPhone 8.
-   Frequent tests were undertaken after major code changes to ensure cross-browser and cross-device compatibility.
-   Friends and family members of ages ranging from 3 to 73, were asked to review the site and documentation to point out any bugs and/or user experience issues.
-   Google Lighthouse devloper tool in Google Chrome dev tools was used to ensure pages meet best practice.

### Known Bugs & Resolutions if Applicable

-   Incrementing ticketid was not repopulating from edit ticket submit.  Resolved by a disabled hidden text input in edit_ticket.html with _ticketid fields.


## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/pengols/HeeeyYooouGuuuys)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://pengols.github.io/HeeeyYooouGuuuys/index.html) in the "GitHub Pages" section.

### Forking the GitHub Repository

Forking the GitHub Repository allows a copy of the original repository in GitHub to be created.  The forked repository can be viewed or be changed without affecting the original repository, by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/pengols/HeeeyYooouGuuuys)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/pengols/HeeeyYooouGuuuys)
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
> Cloning into `pengols`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

- http://polyglot.ninja/auto-incrementing-ids-for-mongodb/ - increment _ticketid on each new inserted ticket

-   [w3schools.com](https://www.w3schools.com/howto/howto_css_modals.asp): For guidance on creating JavaScript modals. Code was modified to better fit my needs.

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [PortEXE Spooky Card Match Game](https://www.youtube.com/watch?v=3uuQ3g92oPQ) : For guidance on the logic of matching cards and the [Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle). Code was modified to better fit my needs.

-   [Marina Ferreira Memory Game](https://marina-ferreira.github.io/tutorials/js/memory-game/) : For guidance on creating new classes on card flip. Code was modified to better fit my needs.

### Content

-   All content was written by the developer.

### Content considered for future addition

-   Implement a scoreboard so users can track their best scores.
-   Implement a difficulty system with easy, medium and hard difficulty levels which increase number of cards on the board.

### Media

-   [Background Image](https://pixabay.com/users/iywbr-11282422/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3941721) by iywbr.


### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

-   Friends and family for testing and proofing.
