from pydantic import BaseModel


class FileInfo(BaseModel):
    player1_name: str
    player2_name: str
    location: str
    date: str
    extension: str

    def get_file_name(self):
        return f"{self.date}_{self.player1_name}_{self.player2_name}_{self.location}_video"