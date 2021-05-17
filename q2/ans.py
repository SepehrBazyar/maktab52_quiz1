from jdatetime import date, datetime
class TimestampOpen:
    def __init__(self, name: str, mode = 'r') -> None:
        self.start = datetime.now()
        self.file = open(name, mode)
    
    def __enter__(self):
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write(self.start, datetime.now())
        return True