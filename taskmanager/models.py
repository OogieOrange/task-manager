from taskmanager import db


class Category(db.Model):
    #schema for the category table
    id = db.Column(db.Integer, primary_key=True)
    catagory_name = db.Column(db.String(25), uniqe=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string
        return self.catagory_name


class Task(db.Model):
    #schema for the task table
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), uniqe=True, nullable=False)
    task_desctiption = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string
        return f"#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"

