from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
posts = [] # db를 대체합니다.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    posts.append(data)
    return jsonify(message='게시글이 작성되었습니다.')

# app.run(debug=True) 설정 하면 코드가 변경될 때마다 자동으로 서버를 재시작하고, 오류 메시지를 콘솔에 표시
if __name__ == '__main__':
    app.run(debug=True)