import json
from dao.post import Post


class PostsDAO:
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_posts(self):
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            new_posts = []
            posts_data = json.load(file)

            for post in posts_data:
                new_posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']))

        return new_posts

    def load_posts_json(self):
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)

        return posts_data

    def load_comments(self):
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
        return comments

    def get_all_posts(self):
        return self.load_posts()

    def get_posts_by_username(self, username):
        posts = self.load_posts()
        user_posts = []

        for post in posts:
            if post.poster_name.lower() == username.lower():
                user_posts.append(post)

        return user_posts

    def get_comments_by_post_id(self, post_id):
        comments = self.load_comments()
        post_comments = []

        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)
        return post_comments

    def search_posts(self, substr):
        posts = self.load_posts()
        new_posts = []

        for post in posts:
            if substr.lower() in post.content.lower():
                new_posts.append(post)
        return new_posts

    def get_post_by_pk(self, pk):
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post
        return

    def get_post_by_pk_json(self, pk):
        posts = self.load_posts_json()
        for post in posts:
            if post['pk'] == pk:
                return post
        return

