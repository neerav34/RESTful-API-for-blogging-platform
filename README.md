# RESTful-API-for-blogging-platform

Certainly! Below, I'll provide additional details about the API endpoints added to the project, including their functionality, usage, and data models.

### API Endpoints:

1. *Create Post*:
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

### Data Models:

- **Post:**
  - `title` (str): Title of the post.
  - `content` (str): Content of the post.

- **Comment:**
  - `content` (str): Content of the comment.

- **LikeDislike:**
  - `value` (int): Value indicating like (1) or dislike (-1).

By following the API usage details and data models provided above, users can interact with the blogging platform API effectively, creating, reading, updating, and deleting posts, as well as adding comments, likes, and dislikes.
