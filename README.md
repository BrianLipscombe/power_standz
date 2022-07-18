<h1 align="center"><img src="media/powerstandzlogo.png" /></h1>
<h1 align="center"><img src="media/readme_banner.png" /></h1>

This is Brian Lipscombe's fourth Milestone Project (Full Stack Frameworks with Django) at [Code Institute](https://codeinstitute.net). It was built using HTML5, CSS3, JavaScript, Python+Flask, MongoDB, Materialize, Gitpod, and deployed on the hosting platform Heroku. It is designed with Code Institute's Assessment Handbook Project Idea 0 in mind - Bring your own idea to life, based on providing value to users to address a specific real or imagined need.

The idea is to sell custom collectible device-charging stations that are inspired by popular film and TV concepts.

The app can be found on Heroku [here.]()

## User Experience (UX)

* User Stories

1. Radiology Employee Goals
    - Register a username and password.
    - Log in.
    - Add outpatient orders (from hard copies possibly in fax print-out basket), including modality, patient name, exam description, date, time, any pertinent comments, and indicate whether the exam is urgent or not.
    - Edit orders if any information changes.
    - Delete completed orders.

2. Owner Goals
    - Provide an app that can help the workflow of hospital orders.
    - Allow radiology employees to input, edit, complete, and manage outpatient orders more effeciently.
    - Ensure only registered staff members have access to the app and is only used within the radiology department to protect patient information.
    - Allow users to create new profiles after initial registration. 

* Design

1. Color Scheme

    - Black is used for each collapsible header because in some hospitals radiology teams wear black scrubs to be quickly differentiated from other hospital staff members.
    - White, with a bit transparency is used to add contrast against the black headers.
    - Red is used in the top navbar to mimic the hospital's red exterior signage.
    - Blues are used in some text and buttons to contrast the urgency of red, to bring a form of aesthetic balance.  

2. Imagery

    The background image was taken from the UCI Medical Center website [here](https://uci.edu/presidential-gateway/overview/_img/overview-future-hospital-1200x570.jpg) then modified using Adobe Photoshop.

3. Typography

    The fonts are kept basic for easy readability.

## Features

* Responsive on all device sizes.
* Interactive elements: Search bar, buttons, collapsible popout, and calendar date picker. 
* Ability to create, read, upadate, and delete orders.

## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

* [CSS3](https://en.wikipedia.org/wiki/CSS)

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

* [Python3](https://www.python.org/download/releases/3.0/)

* [MongoDB](https://www.mongodb.com/)

* [Heroku](https://signup.heroku.com/)

* [Font Awesome](https://fontawesome.com/)

* [Github](https://github.com/)

* [Gitpod](https://www.gitpod.io/)

* [Git](https://en.wikipedia.org/wiki/Git)

* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)

* [Balsamiq](https://balsamiq.com/)

## Testing

* Clicked on all navigation links to verify that they direct to the indicated page.

* Verified that the navigation menu shifts to and from the hamburger icon on the appropriate size screens. 

* Verified if the register button is clicked, register page allows user to register username and password.

* Verified that the log in button directs the user to the orders page within their profile to edit/add orders if their username and password are correct.

* If 'All Orders' button is clicked, user is directed to the orders page.

* Verified that the down arrows extend the collapsible and displays the details of each order when first clicked.

* Verified that the down arrows retract the collapsible details when clicked a second time. 

* Verified that the 'search' button retrieves order information that is relevant to, or matches the key terms the user searched for.

* Verified 'New Order' button links to the add task page.

* Verified that the new order input fields allow the user to choose or input the necessary information. 

* Verified that the 'complete/delete' buttons delete the orders.

* Verfied that the 'edit' buttons direct the user to the edit task page where orders can be edited.

* Verified that navigation elements work the same as all other pages.

## Responsiveness

* This project is confirmed to be responsive on all standard screen sizes using the devtools device toolbar.

## Browser Validation

* This project is confirmed to work with different browsers: Chrome and Internet Explorer. This project has also been tested using different mobile devices such as iphone, Android, and laptops, as well as on a desktop computer.

* Lighthouse Auditing

    - This project scores 100 for Performance, Accessibility, and Best Practices.

All pages were tested on multiple resolutions for proper responsiveness.

All files and pages were validated by direct input using:

* [Nu Html Checker](https://validator.w3.org/#validate_by_input)
    - When testing the HTML code, syntax issues arise on all pages seemingly related to the use of jinja templating and other code borrowed directly from the Data Centric Design mini project.

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - No error found.

* [JSHint](https://jshint.com/)
    - No error found.

* [PEP8](http://pep8online.com/)
    - No error found.

## Deployment

- ### Local copy
1. Install all the requirements: Go to the workspace. In the terminal window type: pip3 install -r requirements.txt.
2. Create a database in MongoDB
    - Signup and login to MongoDB account.
    - Create a cluster and a database.
    - Create a collection in the db: categories, tasks, and users.
    - Add string values for the collection.
3. Create the environment variables
    - Create a .gitignore file in the root directory of the project.
    - Add the env.py file in the .gitignore.
    - Create the file env.py. This will contain all the envornment variables.
    - Import os
    - os.environ.setdefault("IP", "Added by developer")
    - os.environ.setdefault("PORT", "Added by developer")
    - os.environ.setdefault("SECRET_KEY", "Added by developer")
    - os.environ.setdefault("MONGO_URI", "Added by developer")
    - os.environ.setdefault("MONGO_DBNAME", "Added by developer")
  4. Run the app: Type python3 app.py in the terminal.
  
- ### Heroku Deployment
1. Set up local workspace for Heroku
    - In terminal window type: pip3 freeze -- local > requirements.txt. (The file is needed for Heroku to know which filed to install.)
    - In termial window type: python app.py > Procfile (The file is needed for Heroku to know which file is needed as entry point.)
2. Set up Heroku: create a Heroku account and create a new app and select region.
3. Deployment method 'Github'
    - Click on the Connect to GitHub section in the deploy tab in Heroku.
    - Search to connect with the proper repository.
    - When repository appears click on connect to connect the repository with Heroku.
    - Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars.
    - Enter the variables contained in your env.py file. it is about: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME
4. Push the requirements.txt and Procfile to repository.
    - $ git add requirements.txt
    - $ git commit -m "Add requirements.txt"
    - $ git add Procfile 
    - $ git commit -m "Add Procfile"
5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to Aotmatic deployments. Click on Enable Automatic Deploys. By Manual deploy click on Deploy Branch.

  Heroku will receive the code from Github and host the app using the required packages. Click on Open app in the right corner of Heroku account. The app wil open and the live link is available from the address bar.

## Known Bugs

*

## Future Improvements

* Change JPG images to WebP format.

* Add a confirmation message after users click delete before orders are actually deleted.

* Add better CRUD functionality for users to edit their profiles.

* Make entities more consistent. Instead of using 'tasks' and 'orders' for the same purpose, make all entities into either 'tasks' or 'orders' not both.

* Make the collapsible display orders in chronological order by the importance of the due dates, instead of by the order of when new orders were added.

* Fix the appointment time icon to actually work when clicked and provide ease of adding appointment times instead of users having to manually type times into the field.

## Future Improvements for Future Projects

* 
## Credits

* Code

    Code used as a template was borrowed from the Code Institute Data Centric Design Mini Project by Tim Nelson [here](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/) with his final Github commit [here.](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching)
    
    Code for icons from [Font Awesome](https://fontawesome.com/).

    All other code was written or changed by the developer.

## Acknowledgements

* Guidance and Moral Support

    Code Institute on Slack;

    My mentor Narender Singh;

    My family.

This site was developed for educational purposes only.