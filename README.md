# Django Social Media App Documentation

## Project Overview

The Django Social Media App is a web application that allows users to sign up, log in, create posts, comment on other users' posts, and manage their profiles. It uses Django as the backend framework and includes a simple user interface with Bootstrap for styling. This app includes key features like user authentication, creating and viewing posts, commenting, searching posts, and managing user profiles.

---

## Features

1. **User Registration and Authentication**
   - Users can sign up for an account, log in, and log out.
   - Authentication and authorization are handled using Django's built-in user system.
   - Upon registration, a user profile is automatically created using Django signals.
   
2. **User Profile**
   - Each user has a profile page where they can view their personal details and posts.
   - Users can access their profile from the main navigation when logged in.

3. **Posts**
   - Users can create posts with a title and content.
   - Posts are displayed in a list on the main page.
   - Posts can be searched by title or content using a search bar.
   - Each post has a detail view where users can see the full post and its comments.

4. **Comments**
   - Users can comment on posts.
   - Comments are displayed below the post in the detail view.

5. **Search Functionality**
   - Users can search posts by title or content.
   - The search bar filters results dynamically based on the user's query.

6. **Responsive Design**
   - The app is mobile-friendly and fully responsive thanks to Bootstrap 5.
