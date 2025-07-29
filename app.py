from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # Vulnerable SQL Query (no sanitization)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        print("[SQL QUERY]:", query)
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                message = "✅ Login Successful"
            else:
                message = "❌ Invalid Credentials"
        except Exception as e:
            message = f"❗ Error Detected: {e}"
        conn.close()
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
