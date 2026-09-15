from flask import Flask, request, jsonify
from flask_cors import CORS
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)
CORS(app)

# ==========================================
# 1. CREDENCIAIS
# ==========================================
API_KEY = '4Ddotl8YoCIlrRUIFAYKltroXEURynJ-_9uQ14BeCiGC'
URL = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/5b1c046e-d37b-4618-a1d6-622eaff73dc6'
WORKSPACE_ID = 'aaaaa'

# ==========================================
# 2. AUTENTICAÇÃO
# ==========================================
authenticator = IAMAuthenticator(API_KEY)
assistant = AssistantV1(
    version='2021-11-27',
    authenticator=authenticator
)
assistant.set_service_url(URL)

# ==========================================
# 3. COMUNICAÇÃO (FRONTEND <-> BACKEND)
# ==========================================
@app.route('/api/message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message', '')

    try:
        response = assistant.message(
            workspace_id=WORKSPACE_ID,
            input={
                'text': user_message
            }
        ).get_result()

        if response['output']['text']:
            bot_response = response['output']['text'][0]
        else:
            bot_response = "Desculpe, não entendi. Pode repetir?"

        return jsonify({"response": bot_response})
    
    except Exception as e:
        print(f"Erro no Watson: {e}")
        return jsonify({"response": "Erro interno ao tentar contato com o Watson."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)