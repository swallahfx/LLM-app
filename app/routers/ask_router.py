from flask import jsonify, request
from openai import OpenAIError

from ..controllers.ask_controller import AskController
from . import api_blueprint


@api_blueprint.route("/test", methods=["GET"])
def home():
    return jsonify({"home": "welcome to LLM"})


@api_blueprint.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    if not question:
        return jsonify({"error": "Invalid input: question is required"}), 400

    controller = AskController()
    try:
        answer = controller.get_answer(question)
        controller.save_question_answer(question, answer)

        return jsonify({"question": question, "answer": answer})
    except OpenAIError:
        return jsonify({"error": "Failed to get a response from OpenAI API"}), 500
