from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract
from HOME.models import Uploads

# Create your views here.

def Index(request):
    Text = ""
    if request.method == "POST":
        FILE = request.FILES['file']
        image1 = Image.open(FILE)
        Text = pytesseract.image_to_string(image1)
        
        response = HttpResponse("Cookie Set")  
        response.set_cookie('Textpytesseract', Text,max_age=30)  
        return response  
    
    Textpytesseract = ""
    # tutorial  = request.COOKIES['Textpytesseract']  
    tutorial  = request.COOKIES.get('Textpytesseract',"")  
    return render(request, 'index.html',{'tutorial':tutorial})