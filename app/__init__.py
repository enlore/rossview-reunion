from flask import Flask, render_template, redirect, url_for, request, flash
from forms import ApplicationForm
from flask.ext.assets import Environment, Bundle
from flask_wtf import CsrfProtect

from helpers import FlaskMailgunMessage


def create_app(instance_path=None, debug=False, test=False):
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

    app.config.from_object('app.config')
    app.config.from_pyfile('config.py')

    if not test:
        CsrfProtect(app)

    assets = Environment(app)
    
    css_bundle = Bundle('less/main.less', output='css/main.css', filters='less')
    assets.register('css', css_bundle)

    js_bundle = Bundle('js/main.js', output="main.min.js", filters="rjsmin")
    assets.register('js', js_bundle)

    email = FlaskMailgunMessage(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = ApplicationForm()

        if form.validate_on_submit():
            if form.squirrel.data:
                # ANTI SPAM YO
                app.logger.info('SECRET SQUIRREL')
                return redirect(url_for('index'))

            form_data = "name: {}\nemail: {}\nphone: {}\n\n".format(
                    form.name.data,
                    form.email.data,
                    form.phone.data
                    )
            app.logger.info(form_data)

            # send the email
            email.send(form_data)

            flash(app.config['THANKS_FLASH'])

            return redirect(url_for('index'))

        return render_template('index.jade', form=form)

    return app

