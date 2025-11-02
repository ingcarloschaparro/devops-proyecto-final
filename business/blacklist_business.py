from persistent.blacklist_model import Blacklist
from persistent.db_utils import db


def create_blacklist(blacklist: Blacklist):
    db.session.add(blacklist)
    db.session.commit()
    return blacklist.id


def find_blacklist_by_email(email: str):
    return Blacklist.query.filter_by(email=email).first()


def delete_all_blacklist():
    db.session.query(Blacklist).delete()
    db.session.commit()


def find_all_blacklist():
    return Blacklist.query.all()
