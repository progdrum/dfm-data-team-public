from shared import db


class UsedCarCampaign(db.Model):
    """
    This is the model representing the used car campaign data 
    provided for the exercise.
    """
    __tablename__ = 'used_car_campaign'

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date, nullable=False)
    customer_id = db.Column(db.String(20), nullable=False)
    campaign_id = db.Column(db.String(20), nullable=False)
    campaign = db.Column(db.String(40))
    campaign_state = db.Column(db.String(20))
    campaign_serving_status = db.Column(db.String(40))
    clicks = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    budget = db.Column(db.Integer)
    budget_explicitly_shared = db.Column(db.Boolean)
    label_ids = db.Column(db.String(20))
    labels = db.Column(db.String(40))
    invalid_clicks = db.Column(db.Integer)
    conversions = db.Column(db.Integer)
    conv_rate = db.Column(db.Float)
    ctr = db.Column(db.Float)
    cost = db.Column(db.Integer)
    impressions = db.Column(db.Integer)
    search_lost_is = db.Column(db.Float)
    avg_position = db.Column(db.Float)
    interaction_rate = db.Column(db.Float)
    interactions = db.Column(db.Integer)

    def __repr__(self):
        return '<UCC id={0}, customer={1}, campaign={2}>'.format(self.id,
                                                                 self.customer_id,
                                                                 self.campaign_id)
