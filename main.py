from flask import Flask, render_template, request, jsonify
from utils import PostOperator

data = "data/data.json"
comments = "data/comments.json"

app = Flask(__name__)

@app.route('/',)
def main_page():
    all_posts = PostOperator(data, comments)
    posts = all_posts.get_posts_all()
    return render_template("index.html", posts=posts)

@app.route('/post/<postid>',)
def post_page(postid):
    all_posts = PostOperator(data, comments)
    post = all_posts.get_post_by_pk(postid)
    comments_by_post = all_posts.get_comments_by_post_id(postid)
    amount = len(comments_by_post)
    return render_template("post.html", post=post, comments_by_post=comments_by_post, amount=amount)

@app.route('/search',)
def search_page():
    s = request.args['s']
    all_posts = PostOperator(data, comments)
    posts = all_posts.search_for_posts(s)
    amount = len(posts)
    return render_template("search.html", posts=posts, s=s, amount=amount)

@app.route('/users/<username>',)
def user_page(username):
    all_posts = PostOperator(data, comments)
    posts = all_posts.get_posts_by_user(username)

    return render_template("user-feed.html", posts=posts)

@app.route("/GET/api/posts")
def get_json():
    all_posts = PostOperator(data, comments)
    posts = all_posts.get_posts_all()
    return jsonify(posts)

@app.route("/GET/api/posts/<post_id>")
def get_json_id(post_id):
    all_posts = PostOperator(data, comments)
    post = all_posts.get_post_by_pk(post_id)
    return jsonify(post)

if __name__ == "__main__":
    app.run()
