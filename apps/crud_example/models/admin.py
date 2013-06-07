# -*- coding: utf-8 -*-
import datetime
from mole import request, redirect

from mocrud.admin import Admin, ModelAdmin, AdminPanel
from mocrud.filters import QueryFilter

from app import app, db
#from auth import auth
from models import User, Message, Note, Relationship
from mocrud.auth import Auth
auth = Auth(app, db, user_model=User)

class NotePanel(AdminPanel):
    template_name = 'admin/notes.html'

    def get_urls(self):
        return (
            ('/create/', self.create),
        )

    def create(self):
        if request.method == 'POST':
            if request.form.get('message'):
                Note.create(
                    user=auth.get_logged_in_user(),
                    message=request.form['message'],
                )
        next = request.form.get('next') or self.dashboard_url()
        return redirect(next)

    def get_context(self):
        return {
            'note_list': Note.select().order_by(Note.created_date.desc()).paginate(1, 3)
        }

class UserStatsPanel(AdminPanel):
    template_name = 'admin/user_stats.html'

    def get_context(self):
        last_week = datetime.datetime.now() - datetime.timedelta(days=7)
        signups_this_week = User.select().where(User.join_date > last_week).count()
        messages_this_week = Message.select().where(Message.pub_date > last_week).count()
        return {
            'signups': signups_this_week,
            'messages': messages_this_week,
        }

admin = Admin(app, auth)

auth.register_admin(admin)
admin.register(Relationship)
admin.register(Message, MessageAdmin)
admin.register(Note, NoteAdmin)
admin.register_panel('Notes', NotePanel)
admin.register_panel('User stats', UserStatsPanel)

from zkeco_models import Checkinout
admin.register(Checkinout)
