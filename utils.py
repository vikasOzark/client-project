from dataclasses import dataclass


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

    

