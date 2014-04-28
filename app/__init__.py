from flask import Flask, render_template
from forms import ApplicationForm
from flask.ext.assets import Environment, Bundle

def create_app(instance_path=None, debug=False):
    use_instances = False

    if instance_path is not None:
        use_instances = True

    app = Flask(
            __name__,
            instance_relative_config=use_instances,
            instance_path=instance_path,
            template_folder="views",
            static_path='/static',
            static_url_path='/static'
            )

    app.debug = debug
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
    app.config.from_pyfile('config.py')
    app.config.from_object('app.config')

    assets = Environment(app)
    
    css_bundle = Bundle('less/main.less', output='css/main.css', filters='less')
    assets.register('css', css_bundle)

    js_bundle = Bundle('js/main.js', output="main.min.js", filters="rjsmin")
    assets.register('js', js_bundle)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = ApplicationForm()

        if form.validate_on_submit():
            pass

        return render_template('index.jade', form=form)

    return app

