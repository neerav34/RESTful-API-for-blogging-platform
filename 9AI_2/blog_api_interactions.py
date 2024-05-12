################################## Creating a blog post ###################################


# import requests

# url = "http://localhost:8000/posts/"
# data = {
#     "title": "My second Blog Post",
#     "content": "This is the content of my first blog post.",
# }
# response = requests.post(url, json=data)
# print(response.json())


############################### Retrieving a blog post ########################################


# import requests

# # Retrieve all blog posts
# url = "http://localhost:8000/posts/"
# response = requests.get(url)
# print(response.json())

# Retrieve a specific blog post
# post_id = "663fe219c485f4a3e3ea54ec"  # Replace with a valid post ID
# url = f"http://localhost:8000/posts/{post_id}"
# response = requests.get(url)
# print(response.json())


# ############################### Updating a blog post #############################################


# import requests

# post_id = "606c0c91d9a1e2f0dc15f146"  # Replace with a valid post ID
# url = f"http://localhost:8000/posts/{post_id}"
# data = {"title": "Updated Title", "content": "Updated content goes here."}
# response = requests.put(url, json=data)
# print(response.json())


# ############################### Deleting a blog post ###############################################3


# import requests

# post_id = "606c0c91d9a1e2f0dc15f146"  # Replace with a valid post ID
# url = f"http://localhost:8000/posts/{post_id}"
# response = requests.delete(url)
# print(response.json())

# ############################### Adding a comment ##################################################


# import requests

# post_id = "663fe219c485f4a3e3ea54ec"  # Replace with a valid post ID
# url = f"http://localhost:8000/posts/{post_id}/comments/"
# data = {"content": "This is a comment on the post."}
# response = requests.post(url, json=data)
# print(response.json())

# ############################### Liking a blog post ##################################################


# import requests

# post_id = "663fe219c485f4a3e3ea54ec"  # Replace with a valid post ID
# url = f"http://localhost:8000/posts/{post_id}/likes/"
# data = {"value": 1}  # Add one like
# response = requests.post(url, json=data)
# print(response.json())

# ############################### Disliking a blog post #################################################


import requests

post_id = "663fe219c485f4a3e3ea54ec"  # Replace with a valid post ID
url = f"http://localhost:8000/posts/{post_id}/dislikes/"
data = {"value": 1}  # Add one dislike
response = requests.post(url, json=data)
print(response.json())
