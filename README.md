# simple-blog-django

This is the `simple-blog` written in `Python` with the webframework `Django`. More Information <a href="https://haudraufhaun.github.io/2020/07/23/simple-blog.html">here</a>.

## Default Login credentials

For the django admin panel are the login-credentials following:

`username`: _admin_
`password`: _admin_

if you use this project in production, please make sure to change this password before start blogging with `simple-blog-django`.
I also recommend to create a username with your own Name to create the blogposts.

## Used Tools

- `Python`
  - `Django`
    - `django-admin-interface`
    - `django-ckeditor`
- `HTML`
- `CSS`

## Developer Setup

To try this project on your local machine do following:

1. open the terminal in the directory, where also the `README.md` ist stored (main directory)
2. on Windows type `python -m venv env` in the terminal | on MacOS/Linux type in your terminal `python3 -venv env`
3. on Windows (Git Bash) and MacOS type in your terminal `source env/Scripts/activate`
4. at the activated virtualenviroment `env`, type `pip install --upgrade pip` in the terminal
5. then enter the command `pip installl -r requirements.txt`
6. Now you can select in the open folder in VS Code the virtual-enviroment `env` as python-interpreter
