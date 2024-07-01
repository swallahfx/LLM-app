import openai
from openai import OpenAIError
from flask import current_app
from ..models import session
from ..models.ask import QA

class AskController:
    def __init__(self):
        self.client = openai

    def get_answer(self, question):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": question}
                ],
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
            return answer
        except OpenAIError as e:
            current_app.logger.error(f"OpenAI API error: {str(e)}")
            raise e

    def save_question_answer(self, question, answer):
        new_qa = QA(question=question, answer=answer)
        session.add(new_qa)
        session.commit()
