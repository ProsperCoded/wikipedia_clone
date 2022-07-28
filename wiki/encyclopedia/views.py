from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from . import markdown_interpreter as interpreter
from . import util
from . import functions
from random import choice
def index(request):
    try:
        notification = request.notification
        print(request.notification)
    except AttributeError:
        notification = None
        pass
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "notification" : notification
    })
def view_entry(request,title):
    string = util.get_entry(title)
    if string == None:
        available_entry = util.list_entries()
        suggestion = functions.generate_suggestion(available_entry,title,True)
        
        return render(request, "encyclopedia/404.html",{
            "title": title,
            "options": suggestion
        })
        
    string_html = interpreter.convert_to_html(string = string)
    
    return render(request,"encyclopedia/entry.html",{
        "contents": string_html,
        "entry": title
    })

def search(request):
    query = request.GET['q']
    return view_entry(request,query)

def edit_entry(request,title):
    string = util.get_entry(title)
    return create_entry(request,initial_content=string, title=title)
                  

def create_entry(request, initial_content="",title=""):
    return render(request,'encyclopedia/create_entry.html',{
        "purpose" : "create",
        "title": title,
        "initial_content": initial_content
    })
    
def random_page(request):
    entries = util.list_entries()
    random_entry = choice(entries)
    # return HttpResponse(reverse(random_entry))
    return redirect("/"+random_entry)

def save_and_view(request):
    if request.method == "POST":
        title = request.POST['title']
        summary = request.POST['summary']
        content = request.POST['content']
        util.save_entry(title,content)
        request.notification = "Operation was successful"
        return redirect(f"/{title}")
    request.notification = "Sorry Your request Wasn't saved successfully \
        Please go to the official create page to create your entry"
    # return redirect('/')
    return HttpResponseRedirect(reverse('index'))