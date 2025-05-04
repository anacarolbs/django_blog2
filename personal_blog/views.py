from django.shortcuts import HttpResponse, render

def index(request):

    employes = [{ 'name' : 'John',
                    'designation': 'Writer'
                },
                { 'name' : 'Teste1',
                    'designation': 'Accountant'
                },
                { 'name' : 'Teste2',
                    'designation': 'Developer'
                },
                { 'name' : 'Teste3',
                    'designation': 'Developer'
                },
                ]

    data = {'employees': employes}
    return render(request, 'index.html', data)

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def post(request):
    return render(request, 'post.html')
