from flask import Flask, request, render_template, send_from_directory
import utils

app = Flask(__name__)

@app.route("/")
def page_index():
    posts_all = utils.get_posts_all()
    return render_template("index.html", posts_all=posts_all)

@app.route("/posts/<int:postid>")
def post_id(postid):
    post = utils.get_post_by_pk(postid)
    comments = utils.get_comments_for_post_id(postid)
    comments_count = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_count=comments_count)


@app.route("/search")
def search():
    query = request.args.get("s")
    posts = utils.search_for_posts(query)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, posts_count=posts_count, query=query)

@app.route("/users/<user_name>")
def user(user_name):
    posts = utils.get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=posts)

app.run()