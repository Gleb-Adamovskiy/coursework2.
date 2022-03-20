import json

data = "data/data.json"
comments = "data/comments.json"

class PostOperator:

    def __init__(self, data, comments):
        self.data = data
        self.comments = comments

    def get_posts_all(self):
        # возвращает список всех постов
        try:
            with open(self.data, "r", encoding="utf8") as file:
                posts = json.load(file)
            return posts
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл не открывается")

    def get_comments_all(self):
        # возвращает список всех комментариев
        try:
            with open(self.comments, "r", encoding="utf8") as file:
                comment = json.load(file)
            return comment
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл не открывается")

    def get_posts_by_user(self, user_name):
        # возвращает посты определенного пользователя
        user_name_lower = user_name.lower()
        users_posts = []
        posts = self.get_posts_all()
        for post in posts:
            if post["poster_name"] == user_name_lower:
                users_posts.append(post)
        return users_posts

    def get_comments_by_post_id(self, post_id):
        # возвращает комментарии определенного поста
        comments = self.get_comments_all()
        comments_by_post = []
        for comment in comments:
            if comment["post_id"] == int(post_id):
                comments_by_post.append(comment)
        return comments_by_post

    def get_post_by_pk(self, pk):
        # возвращает один пост по его идентификатору
        users_posts = {}
        posts = self.get_posts_all()
        for post in posts:
            if post["pk"] == int(pk):
                users_posts = post
        return users_posts

    def search_for_posts(self, posts_fragment):
        # возвращает список словарей по вхождению posts_fragment
        posts = self.get_posts_all()
        posts_search = []
        posts_fragment_lower = posts_fragment.lower()
        for post in posts:
            if posts_fragment_lower in post["content"].lower():
                posts_search.append(post)

        return posts_search





test_post = PostOperator(data, comments)
post = test_post.get_posts_by_user('leo')
print(post)