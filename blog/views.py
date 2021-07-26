from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 17, 2018'
    },
    {
        'author': 'Pardhiva',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date_posted': 'April 21, 2019'
    }

]


def home(request):
    context = {
        'myPosts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    # return HttpResponse('<h1>Blog About</h1>')
