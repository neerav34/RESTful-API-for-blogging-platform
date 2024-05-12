# RESTful-API-for-blogging-platform



# Prerequisites

1. Python: Ensure Python is installed on your system. You can download it from the official Python website.
   
2. MongoDB: Install MongoDB on your system. You can download it from the official MongoDB website.

# Installtion Steps

1. **Start MongoDB Server**:
   Start the MongoDB server. You can do this by running the mongod command in your terminal.

2. **Configure MongoDB URI**:
   Open the main.py file and ensure that the MongoDB URI in the MongoClient constructor matches your MongoDB server configuration.

3. **Run the API**:
   Start the FastAPI server by running the main.py file:
   
                uvicorn main:app --reload
   
   This command will start the server, and it will automatically reload whenever you make changes to the code.

   

# Testing the APIs

**Using Python Requests**:
You can also test the API endpoints programmatically using the requests library in Python. 


# Additional Notes

- Ensure that MongoDB is running and accessible before starting the FastAPI server.
- Make sure to handle any errors or exceptions gracefully in your code.
- You can customize the API behavior and endpoints according to your project requirements by modifying the code in main.py.
- Consider adding authentication and authorization mechanisms for securing the API if it will be exposed to external users.
- Monitor server logs and database interactions for debugging and optimization purposes.

# API Endpoints:

1. **Create Post**:
   - **HTTP Method:** POST
   - **URL:** `/posts/`
   - **Functionality:** Allows users to create a new blog post.
   - **Request Body:**
     - `title` (string): Title of the post.
     - `content` (string): Content of the post.
   - **Response:** Returns the newly created post with an assigned ID.

2. **Read Posts:**
   - **HTTP Method:** GET
   - **URL:** `/posts/`
   - **Functionality:** Retrieves a list of all blog posts.
   - **Response:** Returns a list of all posts in the database.

3. **Read Post by ID:**
   - **HTTP Method:** GET
   - **URL:** `/posts/{post_id}`
   - **Functionality:** Retrieves a specific blog post by its ID.
   - **Response:** Returns the post with the specified ID if found, otherwise returns a 404 error.

4. **Update Post:**
   - **HTTP Method:** PUT
   - **URL:** `/posts/{post_id}`
   - **Functionality:** Allows users to update an existing blog post.
   - **Request Body:** Same as the create post endpoint (title and content).
   - **Response:** Returns the updated post if successful, otherwise returns a 404 error.

5. **Delete Post:**
   - **HTTP Method:** DELETE
   - **URL:** `/posts/{post_id}`
   - **Functionality:** Deletes a blog post by its ID.
   - **Response:** Returns a success message if the post is deleted, otherwise returns a 404 error.

6. **Create Comment:**
   - **HTTP Method:** POST
   - **URL:** `/posts/{post_id}/comments/`
   - **Functionality:** Allows users to add a comment to a specific blog post.
   - **Request Body:**
     - `content` (string): Content of the comment.
   - **Response:** Returns the newly created comment with an assigned ID.

7. **Like Post:**
   - **HTTP Method:** POST
   - **URL:** `/posts/{post_id}/likes/`
   - **Functionality:** Allows users to like a specific blog post.
   - **Request Body:**
     - `value` (int): The value `1` to add a like.
   - **Response:** Returns a success message if the like is added successfully.

8. **Dislike Post:**
   - **HTTP Method:** POST
   - **URL:** `/posts/{post_id}/dislikes/`
   - **Functionality:** Allows users to dislike a specific blog post.
   - **Request Body:**
     - `value` (int): The value `1` to add a dislike.
   - **Response:** Returns a success message if the dislike is added successfully.

# Data Models:

 1. **Post:**
  - `title` (str): Title of the post.
  - `content` (str): Content of the post.

 2. **Comment:**
  - `content` (str): Content of the comment.

 3. **LikeDislike:**
  - `value` (int): Value indicating like (1) or dislike (-1).





   
