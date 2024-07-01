from flask import request, jsonify, current_app
from ..controllers.ask_controller import AskController
from . import api_blueprint
from openai import OpenAIError

@api_blueprint.route('/test', methods=['GET'])
def home():
    return jsonify({'home': "welcome to LLM"})

@api_blueprint.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({'error': 'Invalid input: question is required'}), 400

    controller = AskController()
    try:
        answer = controller.get_answer(question)
    except OpenAIError as e:
        return jsonify({'error': 'Failed to get a response from OpenAI API'}), 500

    controller.save_question_answer(question, answer)

    return jsonify({'question': question, 'answer': answer})
