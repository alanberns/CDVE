from parser import issuite
from src.core.board.issue import Issue
#from src.core.board.issue  import Issues
from src.core.board.database import db

def list_issues():
    return Issue.query.all()


def create_issue(**kwargs):
   issue = Issue(**kwargs)
   db.session.add(issue)
   db.session.commit()






