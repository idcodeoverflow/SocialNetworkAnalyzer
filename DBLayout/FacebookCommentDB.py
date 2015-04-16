from DBLayout.DBConnection import DBConnection

__author__ = 'David'


class FacebookCommentDB:

    text = ''

    def __init__(self):
        self.text = ''
        self.db = DBConnection()
