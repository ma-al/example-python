# Summary
Use this folder to put secret files that should not be uploaded. For example, text files that contain credentials (username and password or an API key) to access an online service.

**NEVER EVER PUT CREDENTIALS IN YOUR CODE**

For example, do not hard-code an API key into your Python script/notebook, and then commit and push it to the server. Your key will be permanently stored and if the repository is public, anyone can see and abuse it.

# Notes
This folder is here as an *advisory only*.
- it is meant to demonstrate an appropriate repository structure
- this folder should *not* be committed and pushed to your repository
- the [`.gitignore`](../.gitignore) will stop commits from anything in here