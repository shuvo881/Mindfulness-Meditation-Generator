from pydantic import BaseModel


class Step(BaseModel):
    text: str
    pause: str

class MeditationResponse(BaseModel):
    steps: list[Step]
    final_answer: str


