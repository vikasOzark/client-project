from dataclasses import dataclass
from rest_framework import status


@dataclass
class ResponseFormat:
    ok:bool = False
    status_code:int = None
    message:str = None
    data:dict = None

    def __repr__(self) -> str:
        return {
            "ok" : self.ok,
            "status_code" : self.status_code,
            "message" : self.message,
            "data" : self.data
        }


def response_format(ok:bool, status_code:status, message:str = "", data:dict = {}):
    return {
            "ok" : ok,
            "status_code" : status_code,
            "message" : message,
            "data" : data
        }

