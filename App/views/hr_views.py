from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required, current_user
from App.controllers.hr_controller import get_hr_stats


hr_views = Blueprint('hr_views', __name__, template_folder='../templates')

@hr_views.route('/hr/dashboard')
@jwt_required()
def dashboard():
    if current_user.role != 'hr':
        return "Access Denied", 403
    stats = get_hr_stats(current_user.institution_id)
    return render_template('hr/hr.html', **stats)

