from django.shortcuts import render

posts = [
    {
        'author': 'Raja',
        'title': 'Blog post1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020',
    },
    {
        'author': 'Corey',
        'title': 'Blog post2',
        'content': 'First post content',
        'date_posted': 'August 28, 2020',
    },
    {
        'author': 'Michel',
        'title': 'Blog post3',
        'content': 'Third post content',
        'date_posted': 'August 21, 2020',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
