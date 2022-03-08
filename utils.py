import json

def get_posts_all():
    """возвращает посты"""
    with open("data/data.json", "r", encoding="utf-8") as file:
        posts_all = json.load(file)
    return posts_all


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""
    posts_all = get_posts_all()
    posts_by_user = []
    for post in posts_all:
        if post["poster_name"] == user_name:
            posts_by_user.append(post)
    return posts_by_user


def search_for_posts(query):
    """возвращает список словарей по вхождению query"""
    posts_all = get_posts_all()
    posts_with_query = []
    for post in posts_all:
        if query.lower() in post["content"].lower():
            posts_with_query.append(post)
    return posts_with_query


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    posts_all = get_posts_all()
    for post in posts_all:
        if post["pk"] == pk:
            return post


def get_comments_all():
    """возвращает комментарии"""
    with open("data/comments.json", "r", encoding="utf-8") as file:
        comments_all = json.load(file)
    return comments_all


def get_comments_for_post_id(pk):
    """возвращает комментарии к определенному посту"""
    comments_all = get_comments_all()
    comments_for_post = []
    for comment in comments_all:
        if comment["post_id"] == pk:
            comments_for_post.append(comment)
    return comments_for_post