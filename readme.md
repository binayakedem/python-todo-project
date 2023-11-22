<!-- to install virtual env -->
pip install virtual-env
<!-- virtual memory=isolating and new thing and which are required are used not more it makes easy -->

<!-- to make virtual environment or to create virtual env  venv is any name you can use  -->
python -m venv  env

<!-- to install django -->
pip install django


<!-- when packages are install we have to dumb in specific location for future -->

<!--  this creates the txt file which include or consists of all packages installed detail in txt file -->
pip freeze > requirements.txt
  



  <!--  to create django project -->
  django-admin startproject projectname or django-admin startproject projectname . to create without double folder


  <!-- to run the project  -->
  python .\manage.py runserver


  <!-- to install all liv from requirements.txt -->
  pip install -r .\requirements.txt


<!-- to create the app inside project -->
python .\manage.py  startapp appname


<!-- to connect todolist with main project go to setting of main project and add todolist in install app -->

<!-- another importan thing is create new file in the todolist for urls connection name as urls.py  urls are also present in main project but it will become conjusted so just copy main urls to new todolist and add more urls-->

<!-- last thing is todolist urls is not known by main projecct so add in urls of main project  -->

go to settings
<!-- to connect template with current directory using join here import os-->
os.path.join(BASE_DIR,'templates')


<!-- now to render emplate value -->
return render(request,'index.html')


<!-- navbar is used in anywhere so we have to  -->

how to render data comes from template in view

def home(request):
context={
  "name":"Binaya"
}


<!-- to creaate models  in this example charfield and description are declared-->
class Task(models.Model):
    name=models.CharField(max_length=10)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
  


  <!-- now to migrate into database we have to write some commands  -->
  python .\manage.py makemigrations

  <!-- to migrate into dbsqlite we have command -->
  python .\manage.py migrate



  <!-- to bring data from model -->

  we have to import models and use in views

  <!-- to create superuser -->
  python .\manage.py createsuperuser


<!-- to make or add admin or anything in admin pannel is   by   :@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display=('name','description','is_completed')
    list_filter=('is_completed',)
    search_fields=('name',) -->

<!-- jsonformatter.curiosconcept.com -->