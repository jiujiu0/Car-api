"""
使用方法：
from website.Utils.ResultMessage import ResultMessage
return ResultMessage(data=data).success()
"""


class ResultMessage:
    def __init__(self, data="", code=100, message=""):
        self.code = code
        self.message = message
        self.data = data

    def success(self):
        return {
            "code": self.code if self.code != 100 else 200,
            "message": self.message if self.message != "" else "success",
            "data": self.data if self.data != "" else None,
        }

    def error(self):
        return {
            "code": self.code if self.code != 100 else 500,
            "message": self.message if self.message != "" else "error",
            "data": self.data if self.data != "" else None,
        }

    def fail(self):
        return {
            "code": self.code if self.code != 100 else 501,
            "message": self.message if self.message != "" else "fail",
            "data": self.data if self.data != "" else None,
        }