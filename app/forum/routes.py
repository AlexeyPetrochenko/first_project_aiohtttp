from app.forum import views


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_get('/api/messages.list', views.ListMessageViews)
    app.router.add_view('/api/messages.create', views.CreateMessageView)
