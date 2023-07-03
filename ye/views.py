from django.shortcuts import render


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

# Create your views here.

def myfunction(request):
    return render(request,'ye/web.html')

def myfunction1(request):
    page = "Hello you are on the project page"
    number = 9
    context = {'page': page,'number': number,'projectL':projectsList}
    return render(request,'ye/projects.html',context)

def myfunction2(request, pk):

    projectobj = None
    for x in projectsList:
        if x['id'] == pk:
            projectobj = x


    return render(request,'ye/single-project.html',{'pro':projectobj})

