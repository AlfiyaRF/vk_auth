from flask import Flask, request, session, redirect, url_for, make_response, jsonify
import requests
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://52.90.81.238"], supports_credentials=True)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/code')
def get_code():
	code = request.args.get('code')
	if code:
		token_params = {
            "client_id": "7131016",
            "client_secret": "Op0nho25kzSD8Pu8PEOM",
            "redirect_uri": "http://52.90.81.238/code",
            "code": code,
        }
		token_url = "https://oauth.vk.com/access_token?"
		token_response = requests.get(token_url, params=token_params).json()
		if token_response:
			session['token'] = token_response['access_token']
			session['id'] = token_response['user_id']
			return redirect("http://52.90.81.238/")

	return '', 400

@app.route('/user-info')
def get_info():
	if 'token' in session and 'id' in session:
		user_params = {
			"access_token": session.get('token'),
			"user_id": session.get('id'),
			"v": "5.101",
		}
		user_url = "https://api.vk.com/method/users.get?"
		friends_params = {
			"user_id": session.get('id'),
			"order": "random",
			"count": "5",
			"fields": "nickname",
			"access_token": session.get('token'),
			"v": "5.101",
		}
		friends_url = "https://api.vk.com/method/friends.get?"

		user_response = requests.get(user_url, params=user_params).json()
		friends_response = requests.get(friends_url, params=friends_params).json()
		if user_response and friends_response:
			res = {
				"user": user_response,
				"friends": friends_response
			}
			return jsonify(res)
	return '', 401




