import openai
from flask import current_app
from openai import OpenAIError

from ..models import session
from ..models.ask import QA


class AskController:
    def __init__(self):
        self.client = openai

    def get_answer(self, question):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                max_tokens=150,
            )
            return response.choices[0].message.content
        except (IndexError, TypeError, RuntimeError):
            raise RuntimeError(f"Failed to get an answer from OpenAI API")
        except OpenAIError as e:
            current_app.logger.error(
                f"OpenAI API error while getting answer for question '{question}': {str(e)}"
            )
            raise RuntimeError(f"Failed to get answer from OpenAI API: {str(e)}")

    def save_question_answer(self, question, answer):
        new_qa = QA(question=question, answer=answer)
        session.add(new_qa)
        session.commit()
