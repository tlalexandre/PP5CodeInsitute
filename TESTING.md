Go back to [README.md](/README.md)

# Testing

- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#JavaScript)
  - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [CRUD](#crud)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [User Story Testing](#user-story-testing)
- [Stripe](#stripe)
- [Bugs](#bugs)

## Code Validation

### HTML

| Page               | Validator                                                                            | Result            | Comment                                         |
| ------------------ | ------------------------------------------------------------------------------------ | ----------------- | ----------------------------------------------- |
| Home               | ![home](./documentation/images/testing/html/homepagehtml.png)                        | <mark>PASS<mark>  |                                                 |
| Products           | ![products](./documentation/images/testing/html/productshtml.png)                    | <mark>PASS<mark>  |                                                 |
| Product Detail     | ![product detail](./documentation/images/testing/html/productdetailhtml.png)         | <mark>PASS<mark>  |                                                 |
| Add Product        | ![add product](./documentation/images/testing/html/addproducthtml.png)               | <mark>PASS<mark>  |                                                 |
| Edit Product       | ![add product](./documentation/images/testing/html/editproducthtml.png)              | <mark>PASS<mark>  |                                                 |
| Programs           | ![programs](./documentation/images/testing/html/programshtml.png)                    | <mark>PASS<mark>  |                                                 |
| Program Detail     | ![program detail](./documentation/images/testing/html/programdetailhtml.png)         | <mark>Error<mark> | Youtube embed issue outdated property           |
| Cart               | ![cart](./documentation/images/testing/html/carthtml.png)                            | <mark>PASS<mark>  |                                                 |
| Checkout           | ![checkout](./documentation/images/testing/html/checkouthtml.png)                    | <mark>PASS<mark>  |                                                 |
| Subscription       | ![subscription](./documentation/images/testing/html/subscriptionhtml.png)            | <mark>PASS<mark>  |                                                 |
| Profile            | ![profile](./documentation/images/testing/html/profilehtml.png)                      | <mark>PASS<mark>  |                                                 |
| Order Confirmation | ![order confirmation](./documentation/images/testing/html/orderconfirmationhtml.png) | <mark>PASS<mark>  |                                                 |
| My Courses         | ![my courses](./documentation/images/testing/html/mycourseshtml.png)                 | <mark>PASS<mark>  |                                                 |
| Logout             | ![logout](./documentation/images/testing/html/logouthtml.png)                        | <mark>PASS<mark>  |                                                 |
| Login              | ![login](./documentation/images/testing/html/loginhtml.png)                          | <mark>PASS<mark>  |                                                 |
| Register           | ![register](./documentation/images/testing/html/registerhtml.png)                    | <mark>Error<mark> | Prerendered all auth form - ul within small tag |
| Errors             | ![errors](./documentation/images/testing/html/errorshtml.png)                        | <mark>PASS<mark>  |                                                 |
| Privacy            | ![errors](./documentation/images/testing/html/privacyhtml.png)                       | <mark>PASS<mark>  |                                                 |

### CSS

| File     | Validator                                                       | Result           |
| -------- | --------------------------------------------------------------- | ---------------- |
| Base     | ![base](./documentation/images/testing/css/basecss.png)         | <mark>PASS<mark> |
| Program  | ![program](./documentation/images/testing/css/programscss.png)  | <mark>PASS<mark> |
| Profile  | ![profile](./documentation/images/testing/css/profilescss.png)  | <mark>PASS<mark> |
| Product  | ![product](./documentation/images/testing/css/productscss.png)  | <mark>PASS<mark> |
| Checkout | ![checkout](./documentation/images/testing/css/checkoutcss.png) | <mark>PASS<mark> |
| Cart     | ![cart](./documentation/images/testing/css/cartcss.png)         | <mark>PASS<mark> |

## JavaScript

| File               | Validator                                                                   | Result           | Comment                          |
| ------------------ | --------------------------------------------------------------------------- | ---------------- | -------------------------------- |
| stripe_elements.js | ![stripe elements](./documentation/images/testing/js/stripe_elementsjs.png) | <mark>PASS<mark> | Global variables and es6 enabled |
| mailchimp.js       | ![mailchimp](./documentation/images/testing/js/mailchimpjs.png)             | <mark>PASS<mark> | Global variable errors           |
| toast.js           | ![toast](./documentation/images/testing/js/toastsjs.png)                    | <mark>PASS<mark> | Global variables and es6 enabled |

## Python

| File     | App      | Image                                                                     | Result           | Comment                                                             |
| -------- | -------- | ------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------- |
| views    | home     | ![views](./documentation/images/testing/python/homeviewspy.png)           | <mark>PASS<mark> |                                                                     |
| urls     | home     | ![urls](./documentation/images/testing/python/homeurlspy.png)             | <mark>PASS<mark> |                                                                     |
| tests    | home     | ![test](./documentation/images/testing/python/hometestspy.png)            | <mark>PASS<mark> |                                                                     |
| views    | products | ![views](./documentation/images/testing/python/productsviewspy.png)       | <mark>PASS<mark> |                                                                     |
| utils    | products | ![utils](./documentation/images/testing/python/productsutilspy.png)       | <mark>PASS<mark> |                                                                     |
| urls     | products | ![urls](./documentation/images/testing/python/productsurlspy.png)         | <mark>PASS<mark> |                                                                     |
| tests    | products | ![tests](./documentation/images/testing/python/productstestspy.png)       | <mark>PASS<mark> |                                                                     |
| models   | products | ![models](./documentation/images/testing/python/productsmodelspy.png)     | <mark>PASS<mark> |                                                                     |
| admin    | products | ![admin](./documentation/images/testing/python/productsadminpy.png)       | <mark>PASS<mark> |                                                                     |
| forms    | products | ![forms](./documentation/images/testing/python/productformspy.png)        | <mark>PASS<mark> |                                                                     |
| views    | programs | ![views](./documentation/images/testing/python/programsviewspy.png)       | <mark>PASS<mark> |                                                                     |
| urls     | programs | ![urls](./documentation/images/testing/python/programsurlspy.png)         | <mark>PASS<mark> |                                                                     |
| tests    | programs | ![tests](./documentation/images/testing/python/programstestspy.png)       | <mark>PASS<mark> |                                                                     |
| models   | programs | ![models](./documentation/images/testing/python/programsmodelspy.png)     | <mark>PASS<mark> |                                                                     |
| admin    | programs | ![admin](./documentation/images/testing/python/programsadminpy.png)       | <mark>PASS<mark> |                                                                     |
| views    | profiles | ![views](./documentation/images/testing/python/profilesviewspy.png)       | <mark>PASS<mark> |                                                                     |
| urls     | profiles | ![urls](./documentation/images/testing/python/profilesurlspy.png)         | <mark>PASS<mark> |                                                                     |
| tests    | profiles | ![tests](./documentation/images/testing/python/profilestestspy.png)       | <mark>PASS<mark> |                                                                     |
| models   | profiles | ![models](./documentation/images/testing/python/profilesmodelspy.png)     | <mark>PASS<mark> |                                                                     |
| forms    | profiles | ![forms](./documentation/images/testing/python/profilesformspy.png)       | <mark>PASS<mark> |                                                                     |
| admin    | profiles | ![admin](./documentation/images/testing/python/profilesadminpy.png)       | <mark>PASS<mark> |                                                                     |
| webhooks | checkout | ![webhooks](./documentation/images/testing/python/checkoutwebhookspy.png) | <mark>PASS<mark> | Line too long - code from CI walkthrough on webhook - left unedited |
| handler  | checkout | ![handler](./documentation/images/testing/python/checkouthandlerpy.png)   | <mark>PASS<mark> |                                                                     |
| view     | checkout | ![view](./documentation/images/testing/python/checkoutviewspy.png)        | <mark>PASS<mark> |                                                                     |
| urls     | checkout | ![urls](./documentation/images/testing/python/checkouturlspy.png)         | <mark>PASS<mark> |                                                                     |
| tests    | checkout | ![urls](./documentation/images/testing/python/checkouttestspy.png)        | <mark>PASS<mark> |                                                                     |
| signals  | checkout | ![signals](./documentation/images/testing/python/checkoutsignalspy.png)   | <mark>PASS<mark> |                                                                     |
| models   | checkout | ![models](./documentation/images/testing/python/checkoutmodelspy.png)     | <mark>PASS<mark> |                                                                     |
| forms    | checkout | ![forms](./documentation/images/testing/python/checkoutformspy.png)       | <mark>PASS<mark> |                                                                     |
| admin    | checkout | ![admin](./documentation/images/testing/python/checkoutadminpy.png)       | <mark>PASS<mark> |                                                                     |
| views    | cart     | ![views](./documentation/images/testing/python/cartviewspy.png)           | <mark>PASS<mark> |                                                                     |
| utils    | cart     | ![utils](./documentation/images/testing/python/cartutilspy.png)           | <mark>PASS<mark> |                                                                     |
| urls     | cart     | ![urls](./documentation/images/testing/python/carturlspy.png)             | <mark>PASS<mark> |                                                                     |
| tests    | cart     | ![tests](./documentation/images/testing/python/carttestspy.png)           | <mark>PASS<mark> |                                                                     |
| context  | cart     | ![context](./documentation/images/testing/python/cartcontextpy.png)       | <mark>PASS<mark> |                                                                     |

## Responsiveness

The responsiveness of the website was thoroughly tested on various devices, including a MacBook Pro 15-inch, a Huawei P30 Pro, and a 24-inch monitor. Across all devices, the elements displayed cleanly and were well-organized, ensuring a consistent and user-friendly experience.

## Browser Compatibility

| Browser       | Result                                                     | Pass/Fail         |
| ------------- | ---------------------------------------------------------- | ----------------- |
| Google Chrome | All pages, load as expected. All features work as expected | <mark>Pass</mark> |
| Firefox       | All pages, load as expected. All features work as expected | <mark>Pass</mark> |
| Edge          | All pages, load as expected. All features work as expected | <mark>Pass</mark> |
| Safari        | All pages, load as expected. All features work as expected | <mark>Pass</mark> |

## Lighthouse

| Page                   | Validator                                                                                    | Result                 |
| ---------------------- | -------------------------------------------------------------------------------------------- | ---------------------- |
| Home                   | ![home](./documentation/images/testing/lighthouse/home.png)                                  | <mark>Excellent</mark> |
| Home Mobile            | ![home mobile](./documentation/images/testing/lighthouse/homemobile.png)                     | <mark>Good</mark>      |
| Products               | ![products](./documentation/images/testing/lighthouse/products.png)                          | <mark>Excellent</mark> |
| Product Mobile         | ![products mobile](./documentation/images/testing/lighthouse/productsmobile.png)             | <mark>Pass</mark>      |
| Product Detail         | ![product detail](./documentation/images/testing/lighthouse/productdetail.png)               | <mark>Good</mark>      |
| Product Detail Mobile  | ![product detail mobile](./documentation/images/testing/lighthouse/productdetailmobile.png)  | <mark>Pass</mark>      |
| Add Product            | ![add product](./documentation/images/testing/lighthouse/addproduct.png)                     | <mark>Excellent</mark> |
| Add Product Mobile     | ![add product mobile](./documentation/images/testing/lighthouse/addproductmobile.png)        | <mark>Excellent</mark> |
| Edit Product           | ![edit product](./documentation/images/testing/lighthouse/editproduct.png)                   | <mark>Excellent</mark> |
| Edit Product Mobile    | ![edit product mobile](./documentation/images/testing/lighthouse/editproductmobile.png)      | <mark>Excellent</mark> |
| Programs               | ![programs](./documentation/images/testing/lighthouse/programs.png)                          | <mark>Excellent</mark> |
| Programs Mobile        | ![programs mobile](./documentation/images/testing/lighthouse/programsmobile.png)             | <mark>Pass</mark>      |
| Programs Detail        | ![programs detail](./documentation/images/testing/lighthouse/programsdetail.png)             | <mark>Good</mark>      |
| Programs Detail Mobile | ![programs detail mobile](./documentation/images/testing/lighthouse/programdetailmobile.png) | <mark>Pass</mark>      |
| Cart                   | ![cart](./documentation/images/testing/lighthouse/cart.png)                                  | <mark>Good</mark>      |
| Cart Mobile            | ![cart mobile](./documentation/images/testing/lighthouse/cartmobile.png)                     | <mark>Pass</mark>      |
| Checkout               | ![checkout](./documentation/images/testing/lighthouse/checkout.png)                          | <mark>Pass</mark>      |
| Checkout Mobile        | ![checkout mobile](./documentation/images/testing/lighthouse/checkoutmobile.png)             | <mark>Pass</mark>      |
| Confirmation           | ![confirmation](./documentation/images/testing/lighthouse/confirmation.png)                  | <mark>Excellent</mark> |
| Confirmation Mobile    | ![confirmation mobile](./documentation/images/testing/lighthouse/confirmationmobile.png)     | <mark>Pass</mark>      |
| Subscription           | ![subscription](./documentation/images/testing/lighthouse/subscriptions.png)                 | <mark>Excellent</mark> |
| Subscription Mobile    | ![subscription mobile](./documentation/images/testing/lighthouse/subscriptionsmobile.png)    | <mark>Pass</mark>      |
| My courses             | ![my courses](./documentation/images/testing/lighthouse/mycourses.png)                       | <mark>Excellent</mark> |
| My courses Mobile      | ![my courses mobile](./documentation/images/testing/lighthouse/mycoursesmobile.png)          | <mark>Excellent</mark> |
| My courses Mobile      | ![my courses mobile](./documentation/images/testing/lighthouse/mycoursesmobile.png)          | <mark>Excellent</mark> |

Signficant optimisation practices were used to try and increase the Largest Contentful Paint (LCP)

1. Optimisation of images in webp format
2. Post load all JS to stop blocking script downloads in head
3. Image lazy load below the fold

Main issues that could not be resolved which drastically reduced the LCP and performance score was server delays from Heroku which impacted the first byte load.
After must research I could not find a solution to this issue. I will continue to try optimise and research best practices but for now I need further guidance.

### Heroku Server Delay Issue

![Server Delay](./documentation/images/testing/lighthouse/serverdelay.png)

## CRUD

The main crud functionality of this website pertains to user accounts and product purchases

### Create

1. Users can create accounts
2. Users can create cart items
3. Users can create orders
4. Admins and Moderators can create products

### Read

1. All products are read from DB
2. All programs are read from DB
3. All subscriptions are read from DB
4. All user orders are read from DB
5. All user information is read from DB

### Update

1. Users can update cart items
2. Users can update user account information
3. Users can update user profile information
4. Users can update subscription status
5. Admins and Moderators can update products

### Delete

1. Users can remove items from cart
2. User can delete thier accounts
3. Admins and Moderators can delete products

## Manual Testing

### Site Navigation

| Element                  | Action      | Expected Result                                         | Pass/Fail         |
| ------------------------ | ----------- | ------------------------------------------------------- | ----------------- |
| Logo                     | Click       | Redirect to Home page                                   | <mark>Pass</mark> |
| Swag Button              | Click       | Render a dropdown menu of all product categories        | <mark>Pass</mark> |
| Swag Dropdown Link       | Click       | Redirect to selected product category page              | <mark>Pass</mark> |
| Courses Button           | Click       | Render a dropdown menu of all program categories        | <mark>Pass</mark> |
| Courses Dropdown Link    | Click       | Redirect to selected program category page              | <mark>Pass</mark> |
| Subscription Link        | Click       | Redirect to subscription page                           | <mark>Pass</mark> |
| Profile Button           | Click       | Render a dropdown menu of all profile sections          | <mark>Pass</mark> |
| Profile Dropdown         | Click       | Redirect to selected page                               | <mark>Pass</mark> |
| Profile Dropdown Link    | Click       | Redirect to selected page                               | <mark>Pass</mark> |
| Profile Dropdown Auth    | Display     | Render logout, profile, courses, add product links      | <mark>Pass</mark> |
| Profile Dropdown NonAuth | Click       | Render login and register links                         | <mark>Pass</mark> |
| Cart Icon Link           | Click       | Redirect to cart page                                   | <mark>Pass</mark> |
| Hamburger Menu           | Click       | Render a dropdown menu of all links                     | <mark>Pass</mark> |
| Footer Socials           | Click       | Redirect in a new tab to all respective media platforms | <mark>Pass</mark> |
| Privacy and Policy Link  | Click       | Redirect to privacy policy page                         | <mark>Pass</mark> |
| About Page               | Click       | Redirect to about page                                  | <mark>Pass</mark> |
| Footer Email             | Click       | Open up an email provider with developer email attached | <mark>Pass</mark> |
| Newsletter Input Valid   | Submit      | User email logged in mailchimp                          | <mark>Pass</mark> |
| Newsletter Input Valid   | Submit      | User notified of success                                | <mark>Pass</mark> |
| Newsletter Input Invalid | Submit      | Error context displayed to UI                           | <mark>Pass</mark> |
| Register Link            | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Log in Link              | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Log out Link             | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Profile Link             | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Nav Link                 | Hover/Focus | Darken colour of text                                   | <mark>Pass</mark> |
| Footer Socials           | Hover/Focus | Provide background colour feedback change               | <mark>Pass</mark> |

### Home Page

| Element            | Action | Expected Result                           | Pass/Fail         |
| ------------------ | ------ | ----------------------------------------- | ----------------- |
| Shop Now Button    | Click  | Redirect to selected product page         | <mark>Pass</mark> |
| Buy Courses Button | Click  | Redirect to selected programs page        | <mark>Pass</mark> |
| Carousel Arrow     | Click  | Navigate to next slide based on direction | <mark>Pass</mark> |
| Carousel Button    | Click  | Navigate to next slide based on number    | <mark>Pass</mark> |
| Membership Link    | Click  | Redirect to Subscription page             | <mark>Pass</mark> |

### Product Page

| Element                  | Action      | Expected Result                                                 | Pass/Fail         |
| ------------------------ | ----------- | --------------------------------------------------------------- | ----------------- |
| Category Widgets         | Click       | Redirect to selected product category page                      | <mark>Pass</mark> |
| Filter By Price Button   | Click       | Filter queried products based on price                          | <mark>Pass</mark> |
| Filter By Rating Button  | Click       | Filter queried products based on rating                         | <mark>Pass</mark> |
| Filter By Sale Button    | Click       | Filter queried products based on sale                           | <mark>Pass</mark> |
| Filter Direction         | Display     | Filter direction displayed via an arrow                         | <mark>Pass</mark> |
| Current Category         | Display     | Current displayed category is shown in the header               | <mark>Pass</mark> |
| Search Bar               | Search      | Filter products based on query to category, name or description | <mark>Pass</mark> |
| Product Cards            | Display     | All filtered Product Cards Rendered in grid layout              | <mark>Pass</mark> |
| Product View Card Button | Click       | Redirect to product detail page                                 | <mark>Pass</mark> |
| Product Edit Button      | Display     | Only moderators and admins can see this button                  | <mark>Pass</mark> |
| Product Edit Button      | Click       | Redirect to edit product page                                   | <mark>Pass</mark> |
| Product View Card Button | Hover/Focus | Background darkens, text lightens                               | <mark>Pass</mark> |
| Product Edit Button      | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Filter Button            | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Search Icon              | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Category Widgets         | Hover/Focus | Background turns orange, text turns white                       | <mark>Pass</mark> |

### Product Detail Page

| Element             | Action      | Expected Result                                                  | Pass/Fail         |
| ------------------- | ----------- | ---------------------------------------------------------------- | ----------------- |
| Quantity Input      | Input       | Updates the total amount of desired product - no negative values | <mark>Pass</mark> |
| Add to Cart Button  | Click       | Total quantity of item added to cart                             | <mark>Pass</mark> |
| Add to Cart Button  | Click       | Notification appears upon outcome of adding to cart              | <mark>Pass</mark> |
| Product Edit Button | Display     | Only moderators and admins can see this button                   | <mark>Pass</mark> |
| Product Edit Button | Click       | Redirect to edit product page                                    | <mark>Pass</mark> |
| Back Link           | Click       | Redirects back to the products page                              | <mark>Pass</mark> |
| Paginator           | Click       | All navigations buttons redirect to correct paginated results    | <mark>Pass</mark> |
| View Product Button | Click       | Redirect to related product detail page                          | <mark>Pass</mark> |
| Related Products    | Display     | Display product cards of 4 related items with pagination         | <mark>Pass</mark> |
| Back Link           | Hover/Focus | Text darkens                                                     | <mark>Pass</mark> |
| Add to Cart Button  | Hover/Focus | Background darkens, text lightens                                | <mark>Pass</mark> |
| Product Edit Button | Hover/Focus | Background darkens                                               | <mark>Pass</mark> |
| Paginator Button    | Hover/Focus | Background darkens                                               | <mark>Pass</mark> |

### Add Product Page

| Element            | Action      | Expected Result                                | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------------- | ----------------- |
| Authentication     | Display     | Only Moderators and Admins can access the page | <mark>Pass</mark> |
| Form               | Display     | A form is rendered with all fields editable    | <mark>Pass</mark> |
| Form               | Display     | Required fields are clearly marked             | <mark>Pass</mark> |
| Form Valid         | Submit      | A a product is saved to the database           | <mark>Pass</mark> |
| Form Valid         | Submit      | User is redirected to the products page        | <mark>Pass</mark> |
| Form Valid         | Submit      | A notification displays the success message    | <mark>Pass</mark> |
| Form Invalid       | Submit      | Error context is rendered to the UI            | <mark>Pass</mark> |
| Form Invalid       | Submit      | A notification display an error occured        | <mark>Pass</mark> |
| Form Invalid       | Submit      | User is redirected to the add product page     | <mark>Pass</mark> |
| Products Link      | Click       | Navigate to products page                      | <mark>Pass</mark> |
| Products Link      | Hover/Focus | Darkens text                                   | <mark>Pass</mark> |
| Form Image Button  | Hover/Focus | Darkens background                             | <mark>Pass</mark> |
| Form Submit Button | Hover/Focus | Darkens background                             | <mark>Pass</mark> |

### Edit Product Page

| Element             | Action      | Expected Result                                           | Pass/Fail         |
| ------------------- | ----------- | --------------------------------------------------------- | ----------------- |
| Tests Add Products  | All         | All validation and display context from add products pass | <mark>Pass</mark> |
| Form                | Display     | Product data is pre rendered to the page                  | <mark>Pass</mark> |
| Form                | Display     | Product data is pre rendered to the page                  | <mark>Pass</mark> |
| Current Image       | Display     | Link to current image displayed                           | <mark>Pass</mark> |
| Current Image Clear | Checked     | Image is removed from the product                         | <mark>Pass</mark> |
| Current Image Clear | Checked     | Image is removed from the product                         | <mark>Pass</mark> |
| Form Update Button  | Click       | Form is submitted                                         | <mark>Pass</mark> |
| Form Delete Button  | Click       | Confirmation modal appears                                | <mark>Pass</mark> |
| Modal Delete Button | Click       | Product is removed from the database                      | <mark>Pass</mark> |
| Modal Delete Button | Click       | User is redirected to the products page                   | <mark>Pass</mark> |
| Modal Delete Button | Click       | A notification message is displayed to user               | <mark>Pass</mark> |
| Modal Cancel Button | Click       | Modal is hidden                                           | <mark>Pass</mark> |
| Products Link       | Click       | Navigate to products page                                 | <mark>Pass</mark> |
| Products Link       | Hover/Focus | Darkens text                                              | <mark>Pass</mark> |
| Form Update Button  | Hover/Focus | Darkens background                                        | <mark>Pass</mark> |
| Form Delete Button  | Hover/Focus | Darkens background                                        | <mark>Pass</mark> |

### Program Page

| Element                 | Action      | Expected Result                                                 | Pass/Fail         |
| ----------------------- | ----------- | --------------------------------------------------------------- | ----------------- |
| Category Widgets        | Click       | Redirect to selected program category page                      | <mark>Pass</mark> |
| Filter By Price Button  | Click       | Filter queried programs based on price                          | <mark>Pass</mark> |
| Filter By Rating Button | Click       | Filter queried programs based on rating                         | <mark>Pass</mark> |
| Filter By Sale Button   | Click       | Filter queried programs based on sale                           | <mark>Pass</mark> |
| Filter Direction        | Display     | Filter direction displayed via an arrow                         | <mark>Pass</mark> |
| Current Category        | Display     | Current displayed category is shown in the header               | <mark>Pass</mark> |
| Search Bar              | Search      | Filter programs based on query to category, name or description | <mark>Pass</mark> |
| Program Cards           | Display     | All filtered program Cards Rendered in grid layout              | <mark>Pass</mark> |
| Program Card            | Click       | Redirect to program detail page                                 | <mark>Pass</mark> |
| Product Card            | Hover/Focus | Border outline turns blue, cursor is a pointer                  | <mark>Pass</mark> |
| Filter Button           | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Search Icon             | Hover/Focus | Background darkens                                              | <mark>Pass</mark> |
| Category Widgets        | Hover/Focus | Background turns orange, text turns white                       | <mark>Pass</mark> |

### Program Detail Page

| Element                  | Action      | Expected Result                                                | Pass/Fail         |
| ------------------------ | ----------- | -------------------------------------------------------------- | ----------------- |
| Enroll Button            | Click       | Adds course to cart                                            | <mark>Pass</mark> |
| Remove from Cart Button  | Click       | Removes course from cart                                       | <mark>Pass</mark> |
| Login to Enroll          | Click       | Redirects to login page                                        | <mark>Pass</mark> |
| Enrolled Button          | Click       | Button is disabled if already enrolled                         | <mark>Pass</mark> |
| Add / Remove Cart Button | Click       | Notification appears upon outcome of adding/removing from cart | <mark>Pass</mark> |
| Module Accordion         | Click       | Display hidden text and rotate arrow                           | <mark>Pass</mark> |
| Back Link                | Click       | Redirects back to the programs page                            | <mark>Pass</mark> |
| Paginator                | Click       | All navigations buttons redirect to correct paginated results  | <mark>Pass</mark> |
| View Product Button      | Click       | Redirect to related program detail page                        | <mark>Pass</mark> |
| Related Products         | Display     | Display program cards of 4 related items with pagination       | <mark>Pass</mark> |
| Video                    | Display     | Display Video if course is purchased in orders                 | <mark>Pass</mark> |
| Enrolled Button          | Display     | Display Enrolled grey button if course is purchased            | <mark>Pass</mark> |
| Back Link                | Hover/Focus | Text darkens                                                   | <mark>Pass</mark> |
| Add to Cart Button       | Hover/Focus | Background darkens, text lightens                              | <mark>Pass</mark> |
| Remove from Cart Button  | Hover/Focus | Background darkens, text lightens                              | <mark>Pass</mark> |
| Login to Enroll          | Hover/Focus | Background darkens, text lightens                              | <mark>Pass</mark> |
| Paginator Button         | Hover/Focus | Background darkens                                             | <mark>Pass</mark> |

### Subscription Page

| Element                     | Action      | Expected Result                                                | Pass/Fail         |
| --------------------------- | ----------- | -------------------------------------------------------------- | ----------------- |
| Subscribe Button            | Click       | Adds subscription to cart                                      | <mark>Pass</mark> |
| Subscribe Button            | Click       | If subscription is already in cart it is replaced              | <mark>Pass</mark> |
| Remove Subscription Button  | Click       | A confirmation modal is displayed                              | <mark>Pass</mark> |
| Remove Subscription Confirm | Click       | Current active subscription is removed                         | <mark>Pass</mark> |
| Add / Remove Cart Button    | Click       | Notification appears upon outcome of adding/removing from cart | <mark>Pass</mark> |
| Non authenticated users     | Visit       | Redirected to Login page                                       | <mark>Pass</mark> |
| Remove Subscription Button  | Display     | If already subscribed remove button rendered and card is grey  | <mark>Pass</mark> |
| Subscription status         | Display     | Current subscription noticed in subheading                     | <mark>Pass</mark> |
| Subscribe Button            | Hover/Focus | Text darkens, border darkens                                   | <mark>Pass</mark> |

### Cart Page

| Element                     | Action      | Expected Result                                                | Pass/Fail         |
| --------------------------- | ----------- | -------------------------------------------------------------- | ----------------- |
| Update Cart Button          | Click       | Updates the quantity of product by desired amount              | <mark>Pass</mark> |
| Remove from Cart Button     | Click       | Removes all quantity of selected item from cart                | <mark>Pass</mark> |
| Remove Subscription Button  | Click       | A confirmation modal is displayed                              | <mark>Pass</mark> |
| Remove Subscription Confirm | Click       | Current active subscription is removed                         | <mark>Pass</mark> |
| Add / Remove Cart Button    | Click       | Notification appears upon outcome of adding/removing from cart | <mark>Pass</mark> |
| Checkout Button             | Click       | Redirects to checkout page                                     | <mark>Pass</mark> |
| Continue Shopping Link      | Click       | Redirects to products page                                     | <mark>Pass</mark> |
| Update Cart Button          | Display     | Only available for products                                    | <mark>Pass</mark> |
| Discounts                   | Display     | All added discounts are displayed (sale, membership)           | <mark>Pass</mark> |
| Total Cost                  | Display     | Total cost is accurately displayed with breakdown              | <mark>Pass</mark> |
| Update Cart Button          | Hover/Focus | Background darkens, text darkens                               | <mark>Pass</mark> |
| Remove from cart Button     | Hover/Focus | Background darkens, text darkens                               | <mark>Pass</mark> |
| Checkout Button             | Hover/Focus | Background darkens                                             | <mark>Pass</mark> |
| Continue Shopping Link      | Hover/Focus | Text darkens                                                   | <mark>Pass</mark> |

### Checkout Page

| Element                    | Action      | Expected Result                                            | Pass/Fail         |
| -------------------------- | ----------- | ---------------------------------------------------------- | ----------------- |
| Checkout No Items          | Display     | Redirect to cart page with noti                            | <mark>Pass</mark> |
| Checkout Form              | Submit      | Checkout form submit user and delivery data to stripe      | <mark>Pass</mark> |
| Checkout Form              | Submit      | Stripe payment intent, charge and succeeded occurs         | <mark>Pass</mark> |
| Checkout Form              | Submit      | Non valid form returns context of errors                   | <mark>Pass</mark> |
| Checkout Form              | Submit      | Successful order redirects to checkout success page        | <mark>Pass</mark> |
| Checkout Form              | Submit      | Stripe webhooks are logged via stripe listeners            | <mark>Pass</mark> |
| Checkout Form Save Details | Submit      | Authenticated users details are saved if button is checked | <mark>Pass</mark> |
| Stripe Payment Element     | Submit      | Stripe payment element renders error context if not valid  | <mark>Pass</mark> |
| Pay Now Button             | Click       | Submits user/delivery/payment information                  | <mark>Pass</mark> |
| Continue Shopping Link     | Click       | Redirects to products page                                 | <mark>Pass</mark> |
| Remove from Cart Button    | Click       | Removes all quantity of selected item from cart            | <mark>Pass</mark> |
| Loading Spinner            | Display     | A loading spinner is displayed when await payment results  | <mark>Pass</mark> |
| Cart Items                 | Display     | All Cart items are displayed with a price breakdown        | <mark>Pass</mark> |
| Total Cost                 | Display     | The total cost is accounted for for a price breakdown      | <mark>Pass</mark> |
| Pay Now Button             | Hover/Focus | Background darkens                                         | <mark>Pass</mark> |
| Checkout Form Save Details | Checked     | Background darkens                                         | <mark>Pass</mark> |

### Checkout Success/ Past Order Page

| Element       | Action  | Expected Result                                                     | Pass/Fail         |
| ------------- | ------- | ------------------------------------------------------------------- | ----------------- |
| Checkout Form | Display | Checkout form rendered all Order information, price, user, delivery | <mark>Pass</mark> |
| Checkout Form | Display | Total cost breakdown is displayed for the user                      | <mark>Pass</mark> |
| Notification  | Display | A Notification appears highlighting the successful order number     | <mark>Pass</mark> |

### Profile Page

| Element                | Action      | Expected Result                                                  | Pass/Fail         |
| ---------------------- | ----------- | ---------------------------------------------------------------- | ----------------- |
| User Form              | Submit      | A valid user form updates the users first/last name and username | <mark>Pass</mark> |
| User Form              | Submit      | Non valid form returns the context of the error                  | <mark>Pass</mark> |
| User Notification      | Submit      | A Notification appears highlighting outcome of form submission   | <mark>Pass</mark> |
| Delivery Form          | Submit      | A valid form updates the user delivery information               | <mark>Pass</mark> |
| Delivery Form          | Submit      | Non valid form returns the context of the error                  | <mark>Pass</mark> |
| Delivery Notification  | Submit      | A Notification appears highlighting outcome of form submission   | <mark>Pass</mark> |
| Delete Account Button  | Click       | A confirmation modal appears warning the user of the action      | <mark>Pass</mark> |
| Delete Account Confirm | Click       | The user account is deleted from the database                    | <mark>Pass</mark> |
| Delete Account Confirm | Click       | A notification informs the user of the outcome of the operation  | <mark>Pass</mark> |
| Checkout Form          | Display     | Total cost breakdown is displayed for the user                   | <mark>Pass</mark> |
| Update Profile Button  | Click       | Submits the user form                                            | <mark>Pass</mark> |
| Update Delivery Button | Click       | Submits the user profile form for delivery information           | <mark>Pass</mark> |
| Past Order Link        | Click       | Redirects the user to the checkout success page / past order     | <mark>Pass</mark> |
| Past Orders            | Display     | Renders all authenticated users past orders                      | <mark>Pass</mark> |
| Update Profile Button  | Hover/Focus | Background darkens                                               | <mark>Pass</mark> |
| Update Delivery Button | Hover/Focus | Background darkens                                               | <mark>Pass</mark> |
| Past Order             | Hover/Focus | Text darkens                                                     | <mark>Pass</mark> |

### My Courses Page

| Element                | Action      | Expected Result                                    | Pass/Fail         |
| ---------------------- | ----------- | -------------------------------------------------- | ----------------- |
| Program Cards          | Display     | All enrolled program Cards Rendered in grid layout | <mark>Pass</mark> |
| Explore Courses Button | Click       | Redirect to programs page                          | <mark>Pass</mark> |
| Explore Courses Button | Display     | No Courses associated with user                    | <mark>Pass</mark> |
| Program Card           | Click       | Redirect to program detail page                    | <mark>Pass</mark> |
| Product Card           | Hover/Focus | Border outline turns blue, cursor is a pointer     | <mark>Pass</mark> |
| Explore Courses Button | Click       | Background darkens                                 | <mark>Pass</mark> |

### Sign Up Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     | <mark>Pass</mark> |
| Form(Valid)   | Submit         | Sign up in Notification received            | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Context rendered to UI                | <mark>Pass</mark> |
| Form(Invalid) | Submit         | Error Notification received                 | <mark>Pass</mark> |
| Login Link    | Click          | Redirect to Login Page                      | <mark>Pass</mark> |
| Form Button   | Hover/Focus    | Darken Background                           | <mark>Pass</mark> |
| Login Link    | Hover/Focus    | Darken Text                                 | <mark>Pass</mark> |

### Sign In Page

| Element              | Action         | Expected Result                             | Pass/Fail         |
| -------------------- | -------------- | ------------------------------------------- | ----------------- |
| Page                 | Authentication | Authenticated users redirected to Home page | <mark>Pass</mark> |
| Form(Valid)          | Submit         | Redirected to Home page                     | <mark>Pass</mark> |
| Form(Valid)          | Submit         | Sign up in Notification received            | <mark>Pass</mark> |
| Form(Invalid)        | Submit         | Error Context rendered to UI                | <mark>Pass</mark> |
| Form(Invalid)        | Submit         | Error Notification received                 | <mark>Pass</mark> |
| Register Link        | Click          | Redirect to Sign In Page                    | <mark>Pass</mark> |
| Forgot Password Link | Click          | Redirect to Password Reset Page             | <mark>Pass</mark> |
| Form Button          | Hover/Focus    | Darken Background                           | <mark>Pass</mark> |
| Register Link        | Hover/Focus    | Darken Text                                 | <mark>Pass</mark> |
| Forgot Password Link | Hover/Focus    | Darken Text                                 | <mark>Pass</mark> |

### Log Out Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Page          | Authentication | Un-authenticated users redirected to Home page | <mark>Pass</mark> |
| Logout Button | Click          | User session is Logged out                     | <mark>Pass</mark> |
| Logout Button | Click          | Redirected to Home page                        | <mark>Pass</mark> |
| Form Button   | Hover/Focus    | Darken Background                              | <mark>Pass</mark> |

### Password Reset Page

| Element           | Action      | Expected Result                                   | Pass/Fail         |
| ----------------- | ----------- | ------------------------------------------------- | ----------------- |
| Email Input Valid | Submit      | Sends An Email with a reset link to entered email | <mark>Pass</mark> |
| Login Button      | Click       | Redirects to login page                           | <mark>Pass</mark> |
| Reset Button      | Click       | Sends An Email with a reset link to entered email | <mark>Pass</mark> |
| Login Button      | Hover/Focus | Darken Background                                 | <mark>Pass</mark> |
| Reset Button      | Hover/Focus | Darken Background                                 | <mark>Pass</mark> |

### Password Reset Email

| Element    | Action | Expected Result                                   | Pass/Fail         |
| ---------- | ------ | ------------------------------------------------- | ----------------- |
| Email Link | Submit | Link directs the user to the password change form | <mark>Pass</mark> |

### Password Change Page

| Element       | Action      | Expected Result                       | Pass/Fail         |
| ------------- | ----------- | ------------------------------------- | ----------------- |
| Form Valid    | Submit      | Updates the users password            | <mark>Pass</mark> |
| Form Valid    | Submit      | Redirects to password updated page    | <mark>Pass</mark> |
| Form(Valid)   | Submit      | Change Password Notification received | <mark>Pass</mark> |
| Form(Invalid) | Submit      | Error Notification received           | <mark>Pass</mark> |
| Form Invalid  | Submit      | Renders the error context to the user | <mark>Pass</mark> |
| Reset Button  | Click       | Updates the users password            | <mark>Pass</mark> |
| Reset Button  | Hover/Focus | Darken Background                     | <mark>Pass</mark> |

### Django Administration Panel

| Element            | Action | Expected Result                           | Pass/Fail         |
| ------------------ | ------ | ----------------------------------------- | ----------------- |
| Product Model      | Create | Admins can create new products            | <mark>Pass</mark> |
| Program Model      | Create | Admins can create new programs            | <mark>Pass</mark> |
| Subscription Model | Create | Admins can create new subscriptions       | <mark>Pass</mark> |
| Module Model       | Create | Admins can create new modules             | <mark>Pass</mark> |
| Category Model     | Create | Admins can create new Categories          | <mark>Pass</mark> |
| Order Model        | Create | Admins can create new Orders              | <mark>Pass</mark> |
| Product Model      | Update | Admins can update exisiting products      | <mark>Pass</mark> |
| Program Model      | Update | Admins can update exisiting programs      | <mark>Pass</mark> |
| Subscription Model | Update | Admins can update exisiting subscriptions | <mark>Pass</mark> |
| Module Model       | Update | Admins can update exisiting modules       | <mark>Pass</mark> |
| Category Model     | Update | Admins can update exisiting Categories    | <mark>Pass</mark> |
| Order Model        | Update | Admins can update exisiting Orders        | <mark>Pass</mark> |
| Product Model      | Delete | Admins can delete exisiting products      | <mark>Pass</mark> |
| Program Model      | Delete | Admins can delete exisiting programs      | <mark>Pass</mark> |
| Subscription Model | Delete | Admins can delete exisiting subscriptions | <mark>Pass</mark> |
| Module Model       | Delete | Admins can delete exisiting modules       | <mark>Pass</mark> |
| Category Model     | Delete | Admins can delete exisiting Categories    | <mark>Pass</mark> |
| Order Model        | Delete | Admins can delete exisiting Orders        | <mark>Pass</mark> |

## Automated testing

Automated testing was conducted to verify the accuracy of the page responses and templates. However, due to time constraints, there was no opportunity for further elaboration or expansion. Future features include full automated test coverage.

All automated tests are documented in test.py files and pass without error.

## User Story Testing

| User Story                                                                                                                                                                                             | Screenshot                                                                                                                  | Result           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| As a developer I can setup a new Django project so that I can create the project's structure                                                                                                           | The project was set up successfully                                                                                         | <mark>PASS<mark> |
| As a developer, I can perform an early deployment of the application to verify the functionality of the initial setup so that I can continue testing the application as it evolves during development. | The application was deployed after the initial set up to confirm everything is working as expected                          | <mark>PASS<mark> |
| As a developer I can connect database, static/media storage and stripe payments so that data is accessible on deployment and payments are configured early                                             | The application was linked to AWS, Stripe And Elephant SQL. All required services are linked                                | <mark>PASS<mark> |
| As a developer I can choose a colour theme so that all pages have a consistent feel and style.                                                                                                         | A colour theme was selected for the website                                                                                 | <mark>PASS<mark> |
| As a developer I can layout wireframes so that I have a clear idea of the sites structure and theme                                                                                                    | Wireframes created and referenced throughout site layout                                                                    | <mark>PASS<mark> |
| As a User I can intuitively navigate through the website so that I can view all content with ease.                                                                                                     | <details><summary>Navigation Bar</summary><img src="./documentation/images/features/navbar.png"></details>                  | <mark>PASS<mark> |
| As a Developer, I want to ensure the styling and theme of the website are consistent with intuitive UI/UX so that users easily digest content and perform all actions with ease.                       | All elements across all pages are responsive to multiple devices and screensizes                                            | <mark>PASS<mark> |
| As a developer, I can plan out multiple apps that have clear separation of function so that a larger scale project can be broken down into smaller modules                                             | Main application seperated into modular apps for clear functional seperation                                                | <mark>PASS<mark> |
| As a developer, I can create data model classes for products so that structure my data effectively develop relationships between each type                                                             | Product Model clearly structured with effective relationships                                                               | <mark>PASS<mark> |
| As a developer, I can create data model classes for programs so that structure my data effectively develop relationships between each type                                                             | Program Model clearly structured with effective relationships                                                               | <mark>PASS<mark> |
| As a developer, I can create data model classes for subscriptions so that structure my data effectively develop relationships between each type                                                        | Subscription Model clearly structured with effective relationships                                                          | <mark>PASS<mark> |
| As a developer, I can create data model classes for profile so that structure my data effectively develop relationships between each type                                                              | Profile Model clearly structured with effective relationships                                                               | <mark>PASS<mark> |
| As a developer, I can create data model classes for orders so that structure my data effectively develop relationships between each type                                                               | Order Model clearly structured with effective relationships                                                                 | <mark>PASS<mark> |
| As a site owner, I can see all my models and data through an admin portal so I can effectively manage my data through CRUD requests                                                                    | Administration classes all registered with full CRUD capabilities                                                           | <mark>PASS<mark> |
| As a User, I can create or login into my account so that I can retrieve my preexisting secure data                                                                                                     | <details><summary>Login Form</summary><img src="./documentation/images/features/register.png.png"></details>                | <mark>PASS<mark> |
| As a User, I can log out so that I can secure my account from other users                                                                                                                              | <details><summary>Log Out</summary><img src="./documentation/images/features/logout.png"></details>                         | <mark>PASS<mark> |
| As a developer, I can create mock data so that the final application has products, programs and other required models immediately created                                                              | Fixture files and json files created to quickly populate mock data                                                          | <mark>PASS<mark> |
| As a developer, I can have a base template so that all other templates can inherit from it and keep consistant theming                                                                                 | Base template designed, contains relevant links and scripts and is the root inheritance for all subsequent templates        | <mark>PASS<mark> |
| As a User, I can visit the home page so that I can get a understanding of what the website content is about and navigate through                                                                       | <details><summary>Home Page</summary><img src="./documentation/images/features/homepage.png"></details>                     | <mark>PASS<mark> |
| As a developer, I can create data model classes for categories so that structure my data effectively develop relationships between each type                                                           | Category Model clearly structured with effective relationships                                                              | <mark>PASS<mark> |
| As a User, I can visit the product page so that I can view all products available to purchase                                                                                                          | <details><summary>Product Page</summary><img src="./documentation/images/features/productspage.png"></details>              | <mark>PASS<mark> |
| As a User, I can see standardised product preview card, providing key information at a glance so I can quickly make a decision                                                                         | <details><summary>Product Preview Card</summary><img src="./documentation/images/features/productcard.png"></details>       | <mark>PASS<mark> |
| As a User, I can visit the product detail page so that I can get more information on the product and add it to my card                                                                                 | <details><summary>Product Detail Page</summary><img src="./documentation/images/features/productdetail.png"></details>      | <mark>PASS<mark> |
| As a User, I can use a search bar to narrow down search results so that I can quickly find products/programs tailored to me                                                                            | <details><summary>Search Bar</summary><img src="./documentation/images/features/searchbar.png"></details>                   | <mark>PASS<mark> |
| As a User, I can visit the program page so that I can view all program available to enroll in                                                                                                          | <details><summary>Programs Page</summary><img src="./documentation/images/features/programspage.png"></details>             | <mark>PASS<mark> |
| As a User, I can visit the program detail page so that I can get more information on the program and add it to my cart in                                                                              | <details><summary>Program Detail Page</summary><img src="./documentation/images/features/programdetail.png"></details>      | <mark>PASS<mark> |
| As a User, I can see standardised program preview card, providing key information at a glance so I can quickly make a decision                                                                         | <details><summary>Program Card</summary><img src="./documentation/images/features/programcard.png"></details>               | <mark>PASS<mark> |
| As a User, I can add and remove items from my shopping cart so that I can manage my purchases easily and efficiently.                                                                                  | <details><summary>Update Cart</summary><img src="./documentation/images/features/updateitem.png"></details>                 | <mark>PASS<mark> |
| As a User, I can view detailed information about items in my shopping cart on the cart detail page, so that I can review my items before proceeding to checkout.                                       | <details><summary>Cart Page</summary><img src="./documentation/images/features/cartpage.png"></details>                     | <mark>PASS<mark> |
| As a User, I can easily identify and interact with individual items in my shopping cart through standardised cart item cards, so that I can quickly review and manage my selections.                   | <details><summary>Cart Card</summary><img src="./documentation/images/features/cartcard.png"></details>                     | <mark>PASS<mark> |
| As a User, I can receive notification messages whenever a CRUD (Create, Read, Update, Delete) action is taken, so that I am informed about the outcome of my actions and any relevant changes.         | <details><summary>Notifications</summary><img src="./documentation/images/features/notifications.png"></details>            | <mark>PASS<mark> |
| As a User, I can visit the subscription page so that I can view all subscriptions available                                                                                                            | <details><summary>Subscriptions</summary><img src="./documentation/images/features/subscriptions.png"></details>            | <mark>PASS<mark> |
| As a User, I can view a checkout page so that I can get a run down of items and my total charge                                                                                                        | <details><summary>Subscriptions</summary><img src="./documentation/images/features/checkoutpage.png"></details>             | <mark>PASS<mark> |
| As a developer, I can view and manage line items within orders to track my purchase accurately and efficiently.                                                                                        | Line items are editable with adding products to orders from backend. Only certain desired fields                            | <mark>PASS<mark> |
| As a User, I can securely process my order based on the checkout so that I can buy products from the store                                                                                             | <details><summary>Checkout</summary><img src="./documentation/images/features/checkoutpage.png"></details>                  | <mark>PASS<mark> |
| As a Developer, I can securely complete my payment using Stripe integration with webhooks, ensuring that my transaction is protected and verified.                                                     | <details><summary>Checkout</summary><img src="./documentation/images/testing/stripewh.png"></details>                       | <mark>PASS<mark> |
| As a User, I can get sales and member discounts so that I can get items at a better price                                                                                                              | <details><summary>Discounts</summary><img src="./documentation/images/features/discounts.png"></details>                    | <mark>PASS<mark> |
| As a User, I can remove my active membership so that I can opt out of payments                                                                                                                         | <details><summary>Remove Membership</summary><img src="./documentation/images/features/confirmmodal.png"></details>         | <mark>PASS<mark> |
| As a User, I can visit a profile page so that I can view my personal details and update them                                                                                                           | <details><summary>Profile Page</summary><img src="./documentation/images/features/profilepage.png"></details>               | <mark>PASS<mark> |
| As a User, I can view my past orders on the profile page so that I can track my purchase history and review previous transactions.                                                                     | <details><summary>Profile Page</summary><img src="./documentation/images/features/profilepage.png"></details>               | <mark>PASS<mark> |
| As a User, I can view the order confirmation page to see the details of my recent order so that I can verify the items purchased and their prices.                                                     | <details><summary>Checkout Success</summary><img src="./documentation/images/features/checkoutsuccess.png"></details>       | <mark>PASS<mark> |
| As a User, I can access a my courses page where I can view all the courses I have bought or enrolled in, so that I can easily track my learning progress and access course materials.                  | <details><summary>My Courses</summary><img src="./documentation/images/features/mycourses.png"></details>                   | <mark>PASS<mark> |
| As a User, I want to receive a confirmation email after registering for an account, so that I can verify my email address and activate my account.                                                     | <details><summary>Checkout</summary><img src="./documentation/images/features/emailverification.png"></details>             | <mark>PASS<mark> |
| As a User, I can receive an order confirmation emails after successfully completing a purchase, so that I have a record of the transaction and can review the details of my order.                     | <details><summary>Checkout</summary><img src="./documentation/images/features/orderconfirmationemail.png"></details>        | <mark>PASS<mark> |
| As a User, I can see a loading spinner so that I know my actions were registered and a result in pending                                                                                               | <details><summary>Loading Spinner</summary><img src="./documentation/images/features/loading.png"></details>                | <mark>PASS<mark> |
| As a User, I can see my current membership level so that I know what discounts I can avail                                                                                                             | <details><summary>Current Membership</summary><img src="./documentation/images/features/subscriptionlevel.png"></details>of | <mark>PASS<mark> |
| As a User, I can access a short video on the program page if I am enrolled in a course, so that I can get a mock studying experience.                                                                  | <details><summary>Enrolled Video</summary><img src="./documentation/images/features/programvideo.png"></details>of          | <mark>PASS<mark> |
| As a User, I can discover related products and programs on the program page, so that I can explore additional resources or offerings that complement my current selection.                             | <details><summary>Related products</summary><img src="./documentation/images/features/relateditems.png"></details>          | <mark>PASS<mark> |
| As a User, I can see error pages (such as 400, 403, 404, 500) so that I am informed and guided appropriately when unexpected issues arise during my interaction with the website.                      | <details><summary>Error Page</summary><img src="./documentation/images/features/errorpage.png"></details>                   | <mark>PASS<mark> |
| As a User, I can access the Privacy Policy page so that I understand how my personal information is collected, used, and protected.                                                                    | <details><summary>Privacy Policy Page</summary><img src="./documentation/images/features/privacypolicypage.png"></details>  | <mark>PASS<mark> |
| As a User, I can sign up for the newsletter so that I stay updated with the latest news and offerings                                                                                                  | <details><summary>Newsletter</summary><img src="./documentation/images/features/newsletter.png"></details>                  | <mark>PASS<mark> |
| As a developer, I can ensure that all code is thoroughly documented with comments in a standardised format so that anyone reading the code can easily understand its purpose.                          | All custom code is commented and documented                                                                                 | <mark>PASS<mark> |
| As a User, I can reset my password if I forget it, so that I can regain access to my account.                                                                                                          | <details><summary>Password Reset</summary><img src="./documentation/images/features/passwordreset.png"></details>           | <mark>PASS<mark> |
| As a User, I can delete my account so that my personal information and data are removed from the website                                                                                               | <details><summary>Delete Account</summary><img src="./documentation/images/features/accountdeletion.png"></details>         | <mark>PASS<mark> |
| As a Moderator User, I can update product information but do not have administration access, so ensure product information is accurate                                                                 | <details><summary>Moderator</summary><img src="./documentation/images/features/addproducts.png"></details>                  | <mark>PASS<mark> |
| As a Moderator or Superuser, I can manage products by adding, editing, and deleting so that I can keep business inventory up to date.                                                                  | <details><summary>Add/Edit Product</summary><img src="./documentation/images/features/addproducts.png"></details>           | <mark>PASS<mark> |

## Stripe

- Payment Element

![Order](./documentation/images/testing/stripecardelement.png)

- Stripe webhooks

![Webhook](./documentation/images/testing/stripewh.png)

- Stripe Events/Payments

![Events](./documentation/images/testing/stripepayments.png)

## Bugs

Two bugs were left unhandled. Reasons are documented. Issues will take too much time and can lead to large restructuring of codebase. Noted for fix in future editions of website.

| Bug                                                                                                      | Status |
| -------------------------------------------------------------------------------------------------------- | ------ |
| [Bug: Negative Products #52](https://github.com/DarrachBarneveld/ci-swag/issues/52)                      | Closed |
| [Bug: Adding Generic Items To Cart #59](https://github.com/DarrachBarneveld/ci-swag/issues/59)           | Closed |
| [Bug: Checkout Form Error Context #60](https://github.com/DarrachBarneveld/ci-swag/issues/60)            | Closed |
| [Bug: PhoneNumber Order Widget #63](https://github.com/DarrachBarneveld/ci-swag/issues/63)               | Closed |
| [Bug: Stripe Autofill #66](https://github.com/DarrachBarneveld/ci-swag/issues/66)                        | Closed |
| [Bug: Form Accessibiliy #67](https://github.com/DarrachBarneveld/ci-swag/issues/67)                      | Closed |
| [Bug: Form Accessibiliy #67](https://github.com/DarrachBarneveld/ci-swag/issues/67)                      | Closed |
| [Bug: LCP Page Performance #70](https://github.com/DarrachBarneveld/ci-swag/issues/70)                   | Open   |
| [Bug: Stripe WH Order Creation #75](https://github.com/DarrachBarneveld/ci-swag/issues/75)               | Closed |
| [Bug: Stripe WH fires on invalid order error #76](https://github.com/DarrachBarneveld/ci-swag/issues/76) | Closed |
| [Bug: No Update Quantity On Added Products #80](https://github.com/DarrachBarneveld/ci-swag/issues/80)   | Closed |
| [Bug: Query newly added product #81](https://github.com/DarrachBarneveld/ci-swag/issues/81)              | Open   |
| [Bug: Message Overlay #82](https://github.com/DarrachBarneveld/ci-swag/issues/82)                        | Open   |

### Bug Comments

Issue number [76](<(https://github.com/DarrachBarneveld/ci-swag/issues/76)>) was the largest and most difficult issue I encountered. My solution is not fool proof as stated in the issue card comments but as it was related to the course walkthrough I couldnt find signficant support to help me resolve this issue. I tried my very best to provide a solution that was error free and and mimimal security errors.

Minor bugs left unfixed for future features. Documented.

### Noteable issues

When purchasing the senior dev subscription you can add all courses to cart. This means even upon cancellation of the monthly subscription the courses will still be available which is a hack. All courses should have a payment attached to them in a future feature.
