from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
# @login_required
def index():

    return render_template('home/home.html', segment='/index')


@blueprint.route('/<template>')
# @login_required
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template(f"home/{template}", segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except Exception:
        return render_template('home/page-500.html'), 500


# @blueprint.route('/accounts/<template>')
# @login_required
# def login_route(template):

#     try:
#         if not template.endswith('.html'):
#             template += '.html'

#         # Detect the current page
#         # segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template(f"accounts/{template}")

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except Exception:
#         return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except Exception:
        return None
