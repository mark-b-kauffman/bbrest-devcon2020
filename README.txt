Requires: Python >=3.7, <3.8 # I did not have luck with Python 3.8.x.

$ python3 -m venv env

$ source env/bin/activate

$ python3 -m pip install --upgrade pip

$ pip install bbrest

$ pip install notebook

$ jupyter notebook

Shut down the notebook by clicking [Quit] on the top right of the dashboard in the browser, or the file menu, "Close and Halt."

At this point I did the following and created a GitHub project with the code.

$ pip freeze > requirements.txt

If you are checking out this Git project you should be able to follow the above through the upgrade pip, then just run: pip install -r requirements.txt

