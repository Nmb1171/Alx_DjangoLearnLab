Social Media API
Description
This project is a Django-based REST API for a social media platform. Users can register, log in, manage profiles, follow others, like posts, and view notifications for interactions. The project is designed for scalability and production readiness.

Features
Completed:
User Authentication:
Register, log in, and authenticate using token-based authentication.
Profile Management:
View and update profile details (e.g., bio and profile picture).
Posts and Comments:
Users can create, view, edit, and delete posts and comments.
Pagination and filtering for large datasets.
Follow Functionality:
Users can follow and unfollow other users.
View the list of followers for a user.
Personalized Feed:
Authenticated users can view posts from the users they follow.
Likes:
Users can like and unlike posts.
Prevents duplicate likes for the same post.
Notifications:
Automatically notify users when:
Someone follows them.
Someone likes their post.
Someone comments on their post.
Users can view a list of their notifications.
Upcoming:
Deployment:
Prepare and deploy the API to a production environment.
Installation
To set up this project on your local machine:

Clone the repository:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd social_media_api
Set up a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate   # For Windows, use `env\Scripts\activate`
Install dependencies:

Copy code
pip install -r requirements.txt
Configure the database: Open the settings.py file and add your PostgreSQL database credentials:

NAME: Database name
USER: Username
PASSWORD: Password
Apply migrations:

Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server:

Copy code
python manage.py runserver
API Endpoints
User Authentication
Register User

URL: /register/
Method: POST
Description: Register a new user and receive a token.
Request:
json
Copy code
{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "password123"
}
Response:
json
Copy code
{
    "token": "abc123xyz..."
}
Login User

URL: /login/
Method: POST
Description: Log in and retrieve a token.
Profile Management

URL: /profile/
Methods: GET, PUT
Description: Retrieve or update the logged-in user’s profile.
Posts
List All Posts

URL: /api/posts/
Method: GET
Description: Retrieve all posts with pagination.
Create a Post

URL: /api/posts/
Method: POST
Headers:
makefile
Copy code
Authorization: Token <your_token_here>
Request:
json
Copy code
{
    "title": "My First Post",
    "content": "This is my first post content."
}
Update a Post

URL: /api/posts/<id>/
Method: PUT
Delete a Post

URL: /api/posts/<id>/
Method: DELETE
Comments
List All Comments

URL: /api/comments/
Method: GET
Create a Comment

URL: /api/comments/
Method: POST
Headers:
makefile
Copy code
Authorization: Token <your_token_here>
Request:
json
Copy code
{
    "post": 1,
    "content": "This is a comment."
}
Update a Comment

URL: /api/comments/<id>/
Method: PUT
Delete a Comment

URL: /api/comments/<id>/
Method: DELETE
Follow Functionality
Follow a User

URL: /follow/<user_id>/
Method: POST
Description: Follow a user by their ID.
Unfollow a User

URL: /unfollow/<user_id>/
Method: POST
View Followers

URL: /followers/<user_id>/
Method: GET
Description: Retrieve a list of followers for a user.
Feed
View Feed
URL: /feed/
Method: GET
Description: Retrieve a feed of posts from followed users.
Likes
Like a Post

URL: /posts/<post_id>/like/
Method: POST
Description: Like a post by its ID.
Unlike a Post

URL: /posts/<post_id>/unlike/
Method: POST
Notifications
View Notifications
URL: /notifications/
Method: GET
Description: Retrieve a list of notifications for the logged-in user.
Technologies Used
Backend Framework: Django and Django REST Framework
Database: PostgreSQL
Authentication: Token-based authentication with rest_framework.authtoken
