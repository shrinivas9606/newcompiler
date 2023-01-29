from django.shortcuts import render
import sys

# Create your views here.

#create index function

def index(request):
    return render(request, 'index.html')

def runcode(request):
    
    if request.method == 'POST':
        codeareadata = request.POST['codearea']

        try:
            #save original standard output reference

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w') #change the standard output to the file we created

            #execute code

            exec(codeareadata) #example => print("hello world")

            sys.stdout.close()

            sys.stdout = original_stdout #reset the standard output to its original value

            #finall read output from file and save in output variable

            output = open('file.txt', 'r').read()
        except Exception as e:
            #to return error in the code
            sys.stdout = original_stdout
            output = e


        #finally return and render index page and send codedata and output to show on page

        return render(request, 'index.html', {"code":codeareadata, "output":output})
