from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound


from .models import (
    DBSession,
    MyModel,
    )

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    a = 'hola'
    d = {'a':1,'b':2}
    c = 0
    return {'one':one, 'project':'PythonChile'}
