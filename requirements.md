# Web Application Assignment Requirements
 
## Grading Requirements
The total score for the assignment cannot exceed **60 points**, including any additional (bonus) points.

To pass the assignment, students must obtain **at least 50% of the total available points** and:
- At least **25% of the points must be obtained in each category**: Core, Users, Data Processing & Forms, Design UI/UX.
- From the **REST API and Website categories combined**, students must obtain **at least 1.5 points in total**.

Failure to meet any of the above conditions results in the assignment being considered incomplete, regardless of the total number of points achieved.

## Basic rules
The application must be implemented using **Django** or an equivalent web framework.

If Django is used, the following requirements apply:
- The built-in Django authentication system (`django.contrib.auth`) must be used for user management, including registration, login, access control, and password reset.
- Custom user-related functionality should be built on top of the built-in authentication mechanisms.
- For REST API functionality, the application should use Django REST Framework (DRF).
- API endpoints should be implemented using standard DRF views/serializers and return data in JSON format.

The use of alternative frameworks or libraries must provide **equivalent functionality** and follow comparable best practices regarding security, structure, and maintainability. Consult any changes with lab instructor.

Violation of any rules may result in **point deductions**.

---

### The application follows good programming practices
The code should be readable, well structured, and logically organized, following the principle of separation of responsibilities.
 
### The application can be deployed on a separate machine without issues and includes a `requirements.txt` file
The assignment must be easy to run on a different computer.
 
**The project may be provided as a Git repository or as a source code archive (e.g. ZIP).**
 
The configuration must not depend on local paths or hard-coded values in the source code. A `requirements.txt` file and clear setup instructions are required.  After cloning the repository and following standard installation steps, the application should run correctly.



## Core (20 points)
The first three requirements (concerning views, models, and templates) must apply to the **core functionality of the application**, not to Django’s built-in user authentication or user management features. 

It means that components related to login, logout, registration, the default `User` model, user listing pages etc. **will not be counted** towards fullfillment of these requirements.
 
The required views, models, and templates should be based on the application’s specific logic (e.g. products, bookings, etc.).
 
**4 views + 3 models + 3 templates = 10 elements. Each of these elements is worth 2 points.
Each element must represent meaningful application logic and serve a real purpose within the application. Trivial or artificial elements (e.g. views returning only a simple HTTP response without functionality) will not be counted.**
 
### At least 4 views
The application must provide at least four independent functionalities, each exposed through a separate view (URL). Each view should serve a clear and specific purpose within the application. The views must be logically designed and consistent with the project’s domain.
 
### At least 3 models (with relations) – custom made, not built-in
The application must include at least three custom-designed models that are related to each other. **Built-in framework models will not be counted toward this requirement.** The models should reflect the problem domain of the application and define meaningful relationships between data entities.
 
### At least 3 templates (with inheritance _(extends)_ and inclusion _(include)_) – custom made
The application should use at least three custom HTML templates. Templates inheritance (e.g. a shared base layout) and inclusion template fragments must be used to avoid code duplication. The template structure should demonstrate the ability to build a modular and consistent user interface.
 
---
 
## Users (10 points)
 
Form fields must be logically designed and properly validated.
Fields that are required by the application logic must be marked as required, and appropriate validation rules must be applied. Meaningless, artificial, or non-functional fields will not be accepted.
### The application allows users to create an account
The application should provide user registration through a form and securely store user passwords.

**Each requirement is worth 2 points.**
 
### The application allows user login
Users must be able to log in to the system, and user sessions should be properly managed using the framework’s authentication mechanisms.
 
### The application restricts access to protected resources to logged-in users only
Access to resources marked as private or sensitive must be limited to authenticated users. Attempts to access such views without authorization should result in a redirect to the login page or an appropriate access-denied message.
 
### The application allows password reset (using a "fake" email mechanism)
The application must support password reset functionality by generating a one-time reset link sent via email. A fake email mechanism (for example, output to the console) must be used so that the process can be tested without sending real emails.
 
### Forms have server-side validation rules
Even if client-side validation is implemented, the server must also validate the submitted data, as client-side checks can be bypassed.
 
---
 
## Data Processing & Forms (10 points)
Forms required for this section must relate to the application’s core functionality (e.g. adding products, editing bookings, etc.), not with user authentication.
Forms used for login, logout, registration, password reset, or any other authentication-related purpose will not be counted towards fullfillment of these requirements.
 
Form fields must be logically designed and properly validated.
Fields that are required by the application logic must be marked as required, and appropriate validation rules must be applied. Meaningless, artificial, or non-functional fields will not be accepted.

**Each requirement is worth 2 points.**

### The application has a form with at least 4 different types of fields
The application must include an additional form  that contains at least four different types of input fields.
 
### The application allows saving and modifying records via custom web views
The application must include views that accept data from forms and save it to the database (create), as well as allow existing records to be edited (update). These must be custom views; the admin panel alone is not sufficient.
 
### The application has a view for displaying saved records
There must be a page that presents the stored data, either as a list of records and/or a detailed view of individual entries.
 
### The form has server-side validation rules
Even if client-side validation is implemented, the server must also validate the submitted data, as client-side checks can be bypassed.
 
### Properly configured admin panel allowing data modification
The admin panel should allow convenient viewing and editing of the application’s custom models in a clear and usable way.
 
---
 
## Design & UI/UX (15 points)
 
Design points are not awarded automatically. The frontend is evaluated according to the same principles as in the homework assignment, including the use of responsive units, a well-structured layout, proper typography, and overall visual consistency.

### Use of static CSS files
Styles should be placed in separate CSS files and served as static assets rather than being written inline in HTML.
 
### 10 pts – The application is aesthetically pleasing and follows well-established design guidelines (pre-made templates are prohibited)
The application should be aesthetically pleasing and follow well-established design guidelines. The use of ready-made, fully built page templates is prohibited. Inspiration from design principles such as layout grids, consistent spacing, proper heading hierarchy, sufficient contrast, coherent color palettes, clear button states, and readable forms is encouraged.
 
Evaluation focuses on:
- overall responsiveness (usability on smaller screens),
- appropriate use of responsive units (`%`, `rem`/`em`, `vw`/`vh` instead of fixed `px`),
- consistent spacing (margins and padding),
- readability (typography, line length, contrast),
- visual consistency of interface components (buttons, forms, messages).
 
### 3 pts – Forms have client-side validation rules (using JavaScript, not only HTML)
Client-side validation should be implemented using JavaScript (not only HTML validation) to improve user experience by providing immediate feedback before the form is submitted to the server.
Validation should be applied to most fields whenever it makes logical sense to validate them.
### 2 pts – Meaningful error handling in forms
When a user submits invalid data, the form should be returned with clear error messages associated with the relevant fields (and, if needed, a general error message). Correctly filled fields must retain their values so the user does not have to re-enter all data.
 
---
 
## REST API (3 points)
 
### Sensible API endpoint returning data in JSON
The application must expose **at least two** sensibly designed API endpoint that returns data in JSON format. The endpoint should not be artificial or purely for testing purposes, but instead correspond to a real functionality of the application.
 
---
 
## Website (2 points)
 
### The page uses JavaScript in addition to form validation rules checked on the client side
The page should use JavaScript in a way that goes beyond client-side form validation. JavaScript must provide real interactive or dynamic functionality.
 
---
 
## Additional Points
The total score for the assignment cannot exceed **60 points**, including any additional (bonus) points.

### Unit / Integration Tests (2 points)
The application may receive additional points for automated backend tests, including unit and/or integration tests. **A minimum of 30% coverage of the backend code is required.**
 
### Responsive Design with Media Queries (2 points)
The design must be adapted to **at least two screen resolutions (e.g. desktop and smartphone)** using media queries. This requires layout adjustments rather than simple automatic scaling. On smaller screens, all elements should remain readable, functional, and easy to use.
 
### Use of AJAX Technology (2 points)
The page should use AJAX to exchange data with the server dynamically without reloading the entire page. This typically involves fetching data from API endpoints and updating parts of the view, such as lists, object status, or action results. The communication must be asynchronous and genuinely based on data returned by the backend.
