from sqlalchemy import DateTime, func

from persistent.db_utils import db


class Blacklist(db.Model):
    __tablename__ = 'blacklist'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    app_uuid = db.Column(db.String(100), nullable=False)
    blocked_reason = db.Column(db.String(255), nullable=False)
    ip_address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, email, app_uuid, blocked_reason, ip_address):
        self.blocked_reason = blocked_reason
        self.email = email
        self.app_uuid = app_uuid
        self.ip_address = ip_address

    def __repr__(self):
        return f"<Blacklist {self.email}>"

    def to_dict(self):
        return {
            "id": self.id,
            "app_uuid": self.app_uuid,
            "email": self.email,
            "blocked_reason": self.blocked_reason,
            "ip_address": self.ip_address,
            "created_at": self.created_at
        }
