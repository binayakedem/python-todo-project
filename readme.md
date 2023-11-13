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



