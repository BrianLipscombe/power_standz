<h1 align="center"><img src="media/powerstandzlogo.png" /></h1>
<h1 align="center"><img src="media/readme_banner.png" /></h1>

This is Brian Lipscombe's fourth Milestone Project (Full Stack Frameworks with Django) at [Code Institute](https://codeinstitute.net). It was built using HTML5, CSS3, JavaScript, Python+Django, Postgres, Stripe, AWS, Gitpod, and deployed on Heroku. It is designed with Code Institute's Assessment Handbook Project Idea 0 in mind - Bring your own idea to life, based on providing value to users to address a specific real or imagined need.

The idea is to sell custom collectible device-charging stations that are inspired by popular film and TV concepts.

Please note that at this stage, PowerStandz is a fictitious eCommerce store created for the purposes of satisfying the requirements for the Code Institute Full Stack Development Course Milestone Project 4.

The site can be found [here](https://powerstandz.herokuapp.com/) on Heroku.

## User Experience (UX)

* User Stories

1. As a Potential Customer, I would like to be able to:

    - Immediately understand the intent of the site.
    - View and navigate the site on all devices.
    - Learn about the chargers with a description of each, so I can make an informed purchasing decision.
    - Understand the delivery charges, and how much I need to spend to get free delivery, so I can make an informed purchasing decision.
    - Add products to my cart, so I can make a purchase.
    - Receive confirmation of my purchase via email, so I can be confident that the purchase has been made successfully.
    - Register on the site, so I can make a repeat purchase more easily.
    - Contact the business via social media links with inquiries.

2. As a Registered User, I would like to be able to:

    - Sign in to my account.
    - Sign out of my account.
    - Recover a forgotten password.
    - View and update my personal profile.
    - See a summary of my orders.
    - Contact the business via social media links about a specific order.
    - Add reviews to products (this feature will be added).

3. As a Business Owner, I would like to be able to:

    - Add, edit and delete products.
    - Edit product prices.
    - Delete user reviews, in case malicious reviews are added (this feature will be added).

* Design

1. Color Scheme

    - Black, white, and shades of green are mainly used throughout the site to compliment the custom logo design that intends to offer plenty of contrast and a simply yet energetic vibe. 

2. Imagery

    The background image and logo was designed by the developer using Adobe Photoshop. All of the product images were taken from the following sites and edited by the developer also using Adobe Photoshop:<br>
    [Morpheus](https://www.reddit.com/r/shittymoviedetails/comments/kdzzls/in_the_matrix_1999_neo_can_either_take_either_the/)<br>
    [FleetwoodLab](https://www.amazon.de/-/en/Greenlight-GREEN86500-Fleetwood-Bounder-Breaking/dp/B07B7LSR2M)<br>
    [StarDestroyer](https://specialtyproducts.store/imperial-star-destroyer-star-wars-metal-model-kit-iconx/)<br>
    [Jaws](https://www.bbc.com/news/newsbeat-33591730)<br>
    [Thor'sHammer](https://fireandsteel.ca/products/marvel-avengers-thors-hammer)<br>
    [DoctorStrangeEnergySpell](https://www.instructables.com/Dr-Strange-Spell-Props/)<br>
    [TheBatmanChestplate](https://geekculture.co/robert-pattinson-the-batman-symbol-seems-to-be-using-gun-parts-from-wayne-murder/)<br>
    [Grogu](https://starwars.fandom.com/wiki/Hovering_pram)<br>
    [CaptainAmericaShield](https://www.artstation.com/artwork/mqWbl1)<br>
    [PulpFictionBriefcase](https://www.123rf.com/photo_117274967_black-leather-business-briefcase-on-white-background.html?vti=m4upeylkb5urkyxzat-1-68)<br>
    [AlienEgg](https://www.wantitall.co.za/toys/alien-foam-and-latex-life-size-egg-and-facehugger-prop-replica-with-led-lights__b01850nqhu)<br>
    [DarthVader](https://www.rsfigures.com/collections/darth-vader/products/royal-selangor-hand-finished-star-wars-collection-pewter-darth-vader-bust)<br>
    [smartphones](https://www.freepnglogos.com/pics/smartphone)<br>
    [PS5Controllers](https://www.pngall.com/playstation-5-png/download/47893)

3. Typography

    All fonts were kept basic for easy readability, except for the logo which was designed in Adobe Photoshop using Charlemagne Std Bold font as well as additional layers for added flare and subtle glowing energetic feel.

## Features

* Product Details
* Purchase Products
* Registration Form
* Sign In
* Sign Out
* Update Profile
* Recover Password
* Order Summary
* Add Product
* Edit Product
* Delete Product
* Edit Prices
* Responsive
* Interactive

## Wireframes
<h1 align="center"><img src="wireframe/index.png" /></h1>
<h1 align="center"><img src="wireframe/all_products.png" /></h1>
<h1 align="center"><img src="wireframe/product_description.png" /></h1>
<h1 align="center"><img src="wireframe/cart.png" /></h1>
<h1 align="center"><img src="wireframe/empty_cart.png" /></h1>

## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

* [CSS3](https://en.wikipedia.org/wiki/CSS)

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

* [Python3](https://www.python.org/download/releases/3.0/)

* [Django](https://www.djangoproject.com/)

* [Heroku](https://signup.heroku.com/)

* [AWS](https://aws.amazon.com)

* [Stripe](https://stripe.com/)

* [Font Awesome](https://fontawesome.com/)

* [Github](https://github.com/)

* [Gitpod](https://www.gitpod.io/)

* [Git](https://en.wikipedia.org/wiki/Git)

* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)

* [Bootstrap](https://getbootstrap.com/)

* [jQuery](https://jquery.com/)

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

* This project is confirmed to work with different browsers: Chrome and Internet Explorer. This project has also been tested using different mobile devices, laptops, and a desktop.

* Lighthouse Auditing

    - Scores are currently suboptimal but will hopefully be improved upon resubmission.

All pages were tested on multiple resolutions for proper responsiveness.

All files and pages were validated by direct input using:

* [Nu Html Checker](https://validator.w3.org/#validate_by_input)
    - Errors currently exist but will hopefully be resolved upon resubmission.

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - No errors found.
<h1 align="center"><img src="validation/css_validate1.png" /></h1>
<h1 align="center"><img src="validation/css_validate2.png" /></h1>   

* [JSHint](https://jshint.com/)
    - No errors found, only a few warnings.
 <h1 align="center"><img src="validation/js_validate1.png" /></h1>
 <h1 align="center"><img src="validation/js_validate2.png" /></h1>
 <h1 align="center"><img src="validation/js_validate3.png" /></h1>   

* [PEP8](http://pep8online.com/)
    - Errors and warnings currently exist in multiple py files in this project, but some will hopefully be resolved upon resubmission. Please note, feeble attempts to fix some of these problems caused server errors after pushing to Heroku and were therefore undone, and then intentionally left in the original syntax, as provided in the Code Institute Boutique Ado walkthrough source code.

  ## Heroku Deployment
1. Set up local workspace for Heroku
    - In terminal window type: pip3 freeze -- local > requirements.txt. (The file is needed for Heroku to know which filed to install.)
    - In termial window type: python app.py > Procfile (The file is needed for Heroku to know which file is needed as entry point.)
2. Set up Heroku: create a Heroku account and create a new app and select region.
3. Deployment method 'Github'
    - Click on the Connect to GitHub section in the deploy tab in Heroku.
    - Search to connect with the proper repository.
    - When repository appears click on connect to connect the repository with Heroku.
    - Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars.
    - Enter the variables contained in your env.py file. it is about: IP, PORT, SECRET_KEY
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

    Code used as a template throughout this project was borrowed from the Code Institute Boutique Ado walkthrough by Chris Zielinski found [here.](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546)

    Code for the footer in this project was borrowed from the Code Institute MS4 project entitled Perkulator by Richard Ash found [here.](https://github.com/richardhenyash/perkulater)
    
    Other Code was taken from frameworks and toolkits such as [bootstrap](https://getbootstrap.com/) and [Font Awesome](https://fontawesome.com/).

## Acknowledgements

* Guidance and Moral Support

    Code Institute on Slack, my mentor, and most importantly my family.

This site was developed for educational purposes only.