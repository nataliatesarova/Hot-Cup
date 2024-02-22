## Introduction
Hot&Cup is a web platform designed and built to serve as an e-commerce store (Business-to-Consumer) offering customers a selection of tea, coffee, and chocolate. The site used Django, Python, HTML, JavaScript and CSS, incorporating Amazon S3 and Stripe. [Link to deployed site](https://hot-cup-a72a7710ed7c.herokuapp.com/)

The target audience for Hot&Cup encompasses anyone with a fondness for coffee, tea, and hot chocolate. This broad demographic includes individuals across various age groups, lifestyles, and preferences who share a common appreciation for these delights. Whether someone enjoys a morning ritual with a fresh cup of coffee, relishes the calming effect of tea in the afternoon, or indulges in the rich flavors of a hot chocolate as a treat, Hot&Cup aims to cater to their needs. This inclusive approach ensures that the platform offers something for every enthusiast out there, making it a go-to destination for consumers seeking quality, variety, and the simple joy found in these universally beloved beverages and treats.

## Features
### Navbar
The Navbar prominently displays the site name Hot&Cup on the far-left, doubling as a link to the homepage. At the left there are links for 'All Products', 'Coffee', 'Hot Chocolate', and 'Tea'. The link for frequently asked questions (FAQ) and search tool is placed centrally.  Situated on the right are accessible links to 'Register', 'Login', "Wishlist' (if logged in), and the 'Shopping Bag'. Additionally, a banner is featured, informing users of the €30 minimum purchase necessary to qualify for free delivery. The Navbar is fully Responsive and switches to hamburger menu on small screens.
![navbar]()

### Homepage
The homepage incorporates a background image of tea cups with a central plate with welcome message and product introduction.

### Footer
The footer contains links to stores Facebook and Instagram page. There is also links for 'Homepage', 'All products' and 'FAQ'. The contact details are also provided. A feature for newsletter subscription utilizing Mailchimp is available.

### Register
The registration page on Hot&Cup facilitates a smooth sign-up process for new customers. It features a clean layout where users can input their email, a chosen username and password. The page requires users to enter their email and password twice for verification purposes to prevent typing errors.

### Login
The login page offers existing users a secure and straightforward method to access their accounts. With an emphasis on user experience, the login process is optimized for efficiency, ensuring customers can swiftly proceed to browsing and purchasing.

### Products Page
The Products Page of Hot&Cup serves as a visual showcase of the various beverages available for purchase. Each product is presented in a card-like format, displaying a image. Alongside the image, the product name and price are displayed. 

Below the name and price there is a brief description of the product. This snippet of text is designed to entice the user by providing just enough information to pique their interest without overwhelming them with details.

A prominent 'View Product' button is placed beneath each description, inviting users to learn more about the item.

### Product Details Page
<!-- The Product Details Page showcases the product image and essential information for the selected item. The product name and price is immediately visible, and a succinct description is provided.

Customers can select the product weight from a dropdown menu and also adjust the desired quantity. Prominent 'Add to Bag' and 'Keep Shopping' buttons facilitate the purchasing process, while an 'Add to Wishlist' option allows for future purchases.

When logged in an interactive review section invites customer engagement, enabling them to post and read reviews, fostering an informed community of shoppers.

The page's design ensures a smooth and efficient shopping experience, aligned with Hot&Cup's brand and user experience standards. -->

### Reviews
<!-- Hot&Cup values customer feedback, and the reviews feature enables users to post their opinions and experiences with products. These reviews help other customers make informed decisions and contribute to the platform's trustworthiness. Reviews can only be posted by a registered and logged in user. -->

### Shopping Cart
The Shopping Bag page presents a clear summary of the customer's selected items for purchase. It displays product details such as an image, name, price, and quantity, along with the subtotal for each item. An option to remove items is readily accessible.

The page provides a breakdown of costs, including the item total and delivery charges, culminating in the grand total. It also informs customers how much more they need to spend to qualify for free delivery, encouraging additional purchases. The checkout process is secured with a prominent 'Secure Checkout' button, while a 'Keep Shopping' option allows users to continue browsing.

### Checkout
<!-- The checkout process is streamlined for efficiency, with clear steps and secure payment options. Integration with Stripe allows for a variety of payment methods, ensuring a smooth transaction process. -->

<!-- ### Profile
The user is invited to enter name, phone Number, street address, town or city, county, postcode and country -->

### FAQ Page
The FAQ section on Hot&Cup is designed to address common customer inquiries and provide helpful information about product storage, origins, return policies, and shipping times.

### My Wishlist
When logged in the user has the option to add and remove products on a wishlist for future purchases.

## Design
<!-- Colour Scheme

The website has a simple, elegant look that feels cozy and stylish at the same time. I use a mix of down-to-earth and soft, calming colors to make our visitors feel welcome and at ease. I keep the colors consistent throughout the site:

--primary-green: #a5d9a5; A soothing pastel green that brings a touch of nature and tranquility.
--rich-brown: #63453d; A deep, warm brown that provides depth and solidity.
--cream: #f2e8c5; A light, creamy hue that offers a soft background for our content.
--sky-blue: #c5d7f2; A light blue that evokes the openness and calm of the sky.
--accent-pink: #f0bc00; A vibrant pink that adds a playful pop of color.
--neutral-grey: #938c8c; A muted grey for balanced typography and subtle accents.
Secondary colors used sparingly across the website to enhance the visual experience include:

#cdc8c8: A dusty rose for highlighting important elements.
#333: A classic dark grey for strong contrast in texts.
#ff7a7a: A soft red for calls to action and interactive elements.
#0d0d0d: A solid black used mainly in text for readability.
#888 and #97908e: Shades of grey for secondary text and borders.
#eeebe3 and #8f8f8f: Variations of light grey used in backgrounds and to delineate areas.
#dc3545: A bold red to draw attention and provide visual cues.
#aab7c4 and #c7dbd2: Cool blues and greens for a refreshing touch.
The color scheme was chosen to reflect our brand's values and to ensure a visually engaging and comfortable browsing experience. -->

<!-- #### Main Color Scheme

Navigation bar grey: 

Main background: 

Button: 

Footer background:

Login card: -->

### Wireframe mock-ups

[Balsamiq](https://balsamiq.com/) was used to design the wireframes for my website.
![Home Page Wireframe](assets/Balsamiq1.png)
![Recipe Page Wireframe](assets/Balsamiq2.png)
![Recipe Detail Wireframe](assets/Balsamiq3.png)
![Recipe Detail, Add to Wishlist, Review, Wireframe](assets/Balsamiq4.png)


### Database Schema
![Database Schema Diagram]()
The database schemas were designed using [Lucid App](https://lucid.app/). These schemas were pivotal in planning the database models and defining their respective fields. They also facilitated visualizing the relationships between the models and their interactions. 



<!-- ## UX

## Agile Development
The project applied Agile Methodology on GitHub for planning and execution. User Stories were established as GitHub issues clearly outlining their purposes.

Additionally, 5 Epics were initiated and expanded into ? User Stories. Each of these stories was also assigned story points based on their complexity. The specifics of each epic, along with their corresponding user stories, can be located within the project's kanban board
[here](https://github.com/users/nataliatesarova/projects/17/views/1). -->

<!-- ## Epics and user stories

The following Epic and user stories were completed. The MoSCoW prioritization was used to categorize the user story tasks into Must Have, Should Have, Could Have, and Won't Have. Must Haves are critical, Should Haves are important, Could Haves are desirable, and Won't Haves are excluded for now. This categorization helps focus on crucial tasks first, ensuring project success while allowing flexibility for less critical items.

### Epic 1:

### Epic 2:

### Epic 3:

### Epic 4:

### Epic 5:


<!-- <!-- ## Future features  -->

## Future features

Discount Discovery: Users can quickly locate deals to save on purchases.
Best-seller Insights: Shoppers see what's trending to follow popular choices.
Personalized Browsing: Product suggestions evolve from user activity for tailored options.
Custom Alerts: Notifications for new stock or items cater to user interests.
Cart Customization: Flexibility in quantity selection for each cart item.
Save for Later: Option to hold items in the cart for future purchase.
Delivery Estimates: Visible anticipated item arrival times for better planning.
Promo Code Application: Users can redeem codes for additional savings.
Order History: A full view of past transactions aids in budgeting and repurchases.
Sales Analytics: Admins access data on sales and customer habits for strategic adjustments.
Inventory Alerts: Automated notifications for low stock to prevent shortages. -->

# Testing

## Validator

HTML:
![W3C validator]()

CSS:
![Jigsaw validator]()

Code Institute Python Linter:
![Python Linter]()

JShint validator: was used for validation to ensure no JavaScript errors.
![JShint validator]()

## Testing of user stories -->

<!-- # Bugs -->

# Technologies
## Languages

- HTML
- CSS
- JavaScript
- Python

## Frameworks and Tools

- Django: Python framework used in the project's development.
- Bootstrap: Front-end CSS framework for design consistency.
- PostgreSQL
- Balsamiq: Tool used for wireframe creation.
- LucidChart: Platform for designing the database schema.
- Font Awesome: Source for icons.
- Chrome Dev Tools: Used for development and responsive testing.
- Git: Version control through Gitpod terminal for commits and pushes to GitHub.
- GitHub: Repository for storing the project's code.
- Heroku: Platform for deploying the application.
- AWS S3: Used to store static and media files.
- Stripe: Used to handle payments.

## Search Engine Optimization SEO and Marketing

### Business Model

Hot&Cup embraces a consumer-centric online retail approach, delivering a range of quality teas, coffees, and hot chocolate. Catering to connoisseurs of these beverages, our platform ensures a smooth and intuitive shopping journey. The goal is to attract customers desiring variety, value for money, and the convenience of having their favorite items delivered to their homes.

### SEO

Sitemap and robots.txt files have been added to the site's root to help with SEO.

A sitemap, crucial for website navigation, was developed with the assistance of xml-sitemaps based on the live version of the site, and has been positioned at the top directory of the project. Furthermore, a robots.txt document has been instituted at the project's highest level to direct search engine bots regarding which website URLs are permissible for access.

### Marketing

From a marketing perspective, the website features a section for newsletter subscription, aimed at boosting user interaction and advancing the online store's visibility through strategic email marketing campaigns and a robust social media presence.

Additionally, a Facebook page has been established to further enhance our digital footprint and engage with our audience on social media platforms.

Facebook business page [Facebook](https://www.facebook.com/profile.php?id=61556575922935)
![Facebook business page](assets/Facebook.png)

Mailchimp
![Mailchimp]()

## Deployment

Live Deployment: Find the application deployed on [Heroku](https://hot-cup-a72a7710ed7c.herokuapp.com/).

To deploy your application successfully on Heroku, you must first update the requirements.txt file. This file contains a list of all the packages necessary for your application to function.

To generate this list, execute the command pip3 freeze > requirements.txt. This creates or updates your requirements.txt with the current packages and versions.

After updating the requirements, commit the changes and push them to your GitHub repository.

Important: Before pushing any code to GitHub, ensure that all sensitive credentials are stored in an env.py file and that this file is listed in your .gitignore. This prevents Git from tracking the file and stops it from being uploaded to GitHub, keeping your credentials secure.

### For setting up Stripe:

- Sign into your Stripe account.
- Head to the developers' section found at the top right.
- In the API keys area, take note of the PUBLIC_KEY and SECRET_KEY.
- Enter these keys into your env.py file.
- Go to the Webhooks section via the menu and select 'Add endpoint'.
- Provide your application's deployment link, which should resemble: https://your_website.herokuapp.com/checkout/wh/.
- Select the relevant events you want the webhook to listen for and confirm by adding the endpoint.
- After your app is live, conduct a test purchase to verify webhook functionality. Check the webhook's responses on the webhooks page.

### For AWS setup:

- Log into your AWS account.
- To make a new S3 bucket, pick the AWS region nearest to you and give the bucket a unique name.
- In the Object Ownership settings, choose "ACLs enabled" for object access.
- In the Block Public Access settings, turn off "block all public access" since your app needs to reach the bucket contents.
- Confirm these choices and create your bucket.
- Then, adjust the bucket's settings:
- Bucket Properties: Access the bucket's properties, find the website hosting section, and hit edit. Activate static website hosting, choose "Host a static website", and put "index.html" and "error.html" in the respective fields, then save.
- Bucket Permissions: Click the "Permissions" tab, scroll to "CORS configuration", and click edit. Insert the needed code snippet and save your changes.
![AWS](assets/AWS.png)

To set up your S3 bucket's policy and permissions, follow these steps:

- In the bucket policy section, click 'Edit'.
Note your bucket's ARN, for example, arn:aws:s3:::test-bucket.

To create a new policy:
- Open the policy generator tool.
- Choose 'S3 Bucket Policy' as the policy type.
- Set 'Effect' to 'Allow'.
- Enter * for Principal to apply the policy to all users.
- Select 'Amazon S3' as the service.
- Choose 'GetObject' as the action.
- Input your bucket's ARN.
- Add the statement and then generate the policy.
- Copy the new policy.
- Applying the policy:

Paste the policy into the bucket policy editor on AWS.
Append "/*" to your bucket's ARN in the policy to enable access to all contents.
Save the changes.
For ACL settings:

Go to the Access control list (ACL) section and click 'Edit'.
Enable 'List' for 'Everyone' to allow public access and acknowledge the warning.
If you can't edit, ensure 'ACLs enabled' is selected under 'Object Ownership' in your bucket settings.

For setting up IAM and permissions in AWS:

- Creating an IAM User Group
- Go to the IAM dashboard in AWS.
- Select "User Groups" from the left menu.
- Click "Create user group," name it, and then create it. You'll add users and set permissions later.
- Setting Up a Permissions Policy
- Navigate to "Policies" in the left menu and choose "Create policy."
- Use the "Import managed policy" option to search for "AmazonS3FullAccess." Import it.
- In the policy editor, switch to the "JSON" tab.
- Find the "Resource" section in the JSON. Replace the placeholder ARN ("") with your bucket's ARN. Include your bucket's ARN again, this time appending "/*" to allow access to all objects within the bucket.
This process creates a policy giving full access to the specified S3 bucket and prepares a user group for managing permissions effectively.
![IAM](assets/IAM.png)

- On the next page, provide a name and description for the policy and then click 'Create Policy'.
- To link the policy to a user group, go to 'User Groups' from the sidebar menu.
- Click the name of the group you've previously set up and head over to the 'Permissions' tab.
- Choose 'Attach Policy', find the policy you just made, select it, and confirm by clicking 'Attach Policy'.
- For creating a new user, navigate to 'Users' in the sidebar and select 'Add User'.
- Type in the desired username.
- Mark the checkboxes for 'Programmatic access' and 'AWS Management Console access' and proceed to the next step.
- Add the new user to the group by clicking 'Add user to group', check the group you formed before, and finalize by clicking 'Create User'.
- Make sure to note down the 'Access key ID' and 'Secret access key' shown, as they will be required for S3 bucket connectivity.
- To keep a record of these credentials, click 'Download .csv'.

To get your project up and running on Heroku, follow these steps:

### Deployment on Heroku

- Sign up for a Heroku account if you haven't already.
- Once signed in, start a new app by pressing the 'Create app' button.
- Choose a distinctive name for your app, pick a server region, and then click 'Create App'.
- On your app's dashboard, go to the 'Settings' section and look for 'Config Vars'.
- Enter any sensitive information like credentials and API keys in the 'Config Vars' section to keep them secure. This project specifically requires certain credentials to be stored here.

  1. Django's secret key
  2. Database Credentials
  3. AWS access key 
  3. AWS secret key
  4. Email host password.
  5. Stripe public key
  6. stripe secret key
  7. Stripe wh secret

- Navigate to 'Buildpacks' in your app's settings. Buildpacks prepare your environment by installing additional dependencies not listed in your requirements.txt. For this project, select the Python buildpack.
- Switch to the 'Deploy' tab at the top of the page.
- Choose GitHub as the deployment method. Confirm the connection to GitHub, then locate and connect to your repository.
- In the 'Automatic Deploys' section, you have the option to enable automatic updates. This will automatically rebuild your app every time you push changes to the connected GitHub repository. Activate this if desired.
- To deploy, click the 'Deploy Branch' button. Heroku will then build your app. Once the build process is complete, you'll receive a notification indicating a successful deployment, along with a button to view your live application.

### Forking the Repository

Log in to GitHub or create an account. Go to https://github.com/nataliatesarova/Hot-Cup. Click "Fork" at the top-right of the repository. A copy will be created in your own repository.

### Cloning Repository

Visit https://github.com/nataliatesarova/Hot-Cup. Click the green "Code" button and choose "Clone by HTTPS". Copy the provided URL. In your terminal, navigate to your desired directory. Type 'git clone [copied URL]' and press enter to clone the repository locally.

<!-- # Credits and Acknowledgments

I would like to thank my mentor Rory Sheridan and all the tutors, teachers and student colleagues for help and advice on the project. -->