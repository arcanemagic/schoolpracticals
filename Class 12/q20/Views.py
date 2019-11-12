from django.http import HttpResponse
from django.template import engines
from django.template.loader import render_to_string
def home(request):
    title = 'cal v1.0'
    author ='aaa'
    about_template = '''<!DOCTYPE html>
    <html>
    <head>
      <title>''' + title + '''</title>
    </head>
    <body>
        <center><h1>About ''' + title + '''</h1></center>
        <center><p>This Website was developed by ''' + author + '''.</p></center>

	<center>
	<form name="cal" action="\page1" method="get">
	Enter the first value
	<input name="val1" type="text" value=""><br>
	Enter the second value
	<input name="val2" type="text" value=""><br>
    	Enter the Operator(+,-,/,*)
	<input name="opt" type="text" value=""><br>
	<input name="sbmt" type="submit" value="submit">
	<input name="sst" type="reset" value="reset">
	</center>
	</form>

        <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>     </body>    </html>'''

    django_engine = engines['django']
    template = django_engine.from_string(about_template)
    html = template.render({'title': title, 'author': author})
    return HttpResponse(html)

def page1(request):
    title = 'cal v1.0'
    author ='aaa'
    val1 = int(request.GET.get('val1'))
    val2 = int(request.GET.get('val2'))
    opt=request.GET.get('opt')
    if opt=='+':
        sum=val1+val2
        about_template = '''<!DOCTYPE html>
        <html>
        <head>
          <title>''' + title + '''</title>
        </head>
        <body>
            <center><h1>About ''' + title + '''</h1></center>
            <center><p>The sum is ''' + str(sum) + '''</p></center>
            <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>
            </body>
            </html>'''
    elif opt=='-':
        sub=val1-val2
        about_template = '''<!DOCTYPE html>
        <html>
        <head>
          <title>''' + title + '''</title>
        </head>
        <body>
            <center><h1>About ''' + title + '''</h1></center>
            <center><p>The difference is ''' + str(sub) + '''</p></center>
            <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>
            </body>
            </html>'''
    elif opt=='*':
        prod=val1*val2
        about_template = '''<!DOCTYPE html>
        <html>
        <head>
          <title>''' + title + '''</title>
        </head>
        <body>
            <center><h1>About ''' + title + '''</h1></center>
            <center><p>The product is ''' + str(prod) + '''</p></center>
            <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>
            </body>
            </html>'''
    elif opt=='/':
        quot=val1/val2
        about_template = '''<!DOCTYPE html>
        <html>
        <head>
          <title>''' + title + '''</title>
        </head>
        <body>
            <center><h1>About ''' + title + '''</h1></center>
            <center><p>The quotient is ''' + str(quot) + '''</p></center>
            <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>
            </body>
            </html>'''
    else:
        about_template = '''<!DOCTYPE html>
        <html>
        <head>
          <title>''' + title + '''</title>
        </head>
        <body>
            <center><h1>About ''' + title + '''</h1></center>
            <center><p>Wrong operator, try again </p></center>
            <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>
            </body>
            </html>'''
    django_engine = engines['django']
    template = django_engine.from_string(about_template)
    html = template.render({'title': title, 'author': author})
    return HttpResponse(html)
