from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


projectList = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
        {
        'id':'2',
        'title':'Portofolio Website',
        'description': "This is a project that i've built for my portofolio!"
    },
        {
        'id':'3',
        'title':'Social Network',
        'description': 'Awesome open source priject I am still working at'
    },
]

def projects(request):
    page = 'Projects'
    number = 10
    context =  {'page': page, 'number': number, 'projects': projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for proj in projectList:
        if proj['id'] == pk:
            projectObj = proj
    return render(request, 'projects/single-project.html', {'project': projectObj})