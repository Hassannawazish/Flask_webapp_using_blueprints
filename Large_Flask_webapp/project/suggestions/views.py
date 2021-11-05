from flask import Blueprint, flash, render_template, redirect, url_for
from database.setup import Base, sessionmaker, engine, db_session
from project.suggestions.forms import *
from project.models import Suggestion, userName

suggestion_blueprint = Blueprint('suggest',
                              __name__,
                              template_folder='templates/suggestions')


@suggestion_blueprint.route('/add', methods=['GET', 'POST'])
def add_sug():

    form = AddForm()

    if form.validate_on_submit():

        user_name = form.user_name.data
        suggest = form.suggestion.data

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        usr_name = userName(user_name)
        session.add(usr_name)
        session.flush()
        new_sug = Suggestion(suggest, usr_name.id)

        session.add(new_sug)
        session.commit()
        db_session.close()
        flash('Submitted...........!')
        flash('Thanks for your suggestion, hopefully it will resolve the 3D printing issues.')
        return redirect(url_for('suggest.flag_sug'))

    return render_template('add.html', form=form)


@suggestion_blueprint.route('/flag')
def flag_sug():
    return render_template('flag.html')

@suggestion_blueprint.route('/list')
def list_sug():

    suggest = Suggestion.query.all()
    username = userName.query.all()
    suggestionz = []
    sug_id = []
    USR = []
    usr_id = []
    for i in suggest:
        suggestionz.append(i.sugg)
        sug_id.append(i.id)
    for j in username:
        USR.append(j.user_name)
        usr_id.append(j.id)
    comb = zip(usr_id, USR, suggestionz)
    return render_template('list.html', lis=comb)