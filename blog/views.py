from datetime import date

from django.shortcuts import render

all_posts = [
    {
        'title': "Programming Python",
        'slug': "programming-python",
        'image': "programming_goal.jpg",
        'author': "Viacheslav",
        'date': date(2023, 7, 24),
        'excerpt': "Striving to learn and understand code will make you a programmer",
        'content': "Some text about",
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/posts.html', {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post_detail.html', {'post': identified_post})
