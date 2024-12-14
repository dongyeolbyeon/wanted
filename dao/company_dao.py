from config.database import db

class Company(db.Model):
    __tablename__ = 'wanted_company'
    __bind_key__ = 'cluster'
    __table_args__ = {
        'mysql_collate': 'utf8mb4_general_ci'
    }

    id = db.Column(db.Integer, primary_key=True)
    company_name_ko = db.Column(db.String(50), nullable=True)
    company_name_en = db.Column(db.String(50), nullable=True)
    company_name_ja = db.Column(db.String(50), nullable=True)
    company_tag_ko = db.Column(db.String(400), nullable=True)
    company_tag_en = db.Column(db.String(400), nullable=True)
    company_tag_ja = db.Column(db.String(400), nullable=True)

    def __init__(self, company_name_ko, company_name_en, company_name_ja, company_tag_ko, company_tag_en, company_tag_ja):
        self.company_name_ko = company_name_ko
        self.company_name_en = company_name_en
        self.company_name_ja = company_name_ja
        self.company_tag_ko = company_tag_ko
        self.company_tag_en = company_tag_en
        self.company_tag_ja = company_tag_ja

    def __repr__(self):
        return f'<Company {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'company_name_ko': self.company_name_ko,
            'company_name_en': self.company_name_en,
            'company_name_ja': self.company_name_ja,
            'company_tag_ko': self.company_tag_ko,
            'company_tag_en': self.company_tag_en,
            'company_tag_ja': self.company_tag_ja,
        }
