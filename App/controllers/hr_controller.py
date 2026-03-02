from App.models import Participant, Registration, Result, Institution
from App.database import db



def get_hr_stats(institution_id):
    total_reg=Participant.query.filter_by(institution_id=institution_id).count()
    participated = db.session.query(Registration)\
        .join(Participant)\
        .filter(Participant.institution_id == institution_id)\
        .join(Result).distinct(Registration.participant_id).count()
    participants=Participant.query.filter_by(institution_id=institution_id).all()
    return {
        "reg_count": total_reg,
        "part_count": participated,
        "no_show_count": total_reg - participated,
        "participants": participants,
        "institution": Institution.query.get(institution_id)
    }