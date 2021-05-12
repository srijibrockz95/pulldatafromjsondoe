from Pullout import db

class Jenkinsmonitordata(db.Model):
    JobId = db.Column(db.Integer, primary_key=True)
    DisplayName = db.Column(db.String(120), nullable=False, unique=True)
    NextBuildNumber = db.Column(db.Integer, nullable=False)
    HealthReport = db.Column(db.Integer, nullable=False)
    LastSuccessfulBuild = db.Column(db.Integer, nullable=False)
    LastFailedBuild = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Jenkinsmonitordata %r>' % self.displayName