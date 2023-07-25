
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'your_database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/api/topics', methods=['POST'])
def increment_topic_count():
    topic_name = request.json.get('topic_name')
    count_date = request.json.get('count_date')

    conn = get_db()
    cursor = conn.cursor()

    # Insert or update topic count
    cursor.execute('''INSERT INTO TopicCounts (topic_name, count, count_date)
                      VALUES (?, 1, ?)
                      ON CONFLICT(topic_name, count_date) DO UPDATE SET count = count + 1''',
                   (topic_name, count_date))
    conn.commit()

    conn.close()

    return jsonify({'message': 'Topic count updated successfully.'}), 200

@app.route('/api/topics', methods=['GET'])
def get_topic_counts():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''SELECT topic_name, count, count_date
                      FROM TopicCounts
                      WHERE count_date >= ? AND count_date <= ?''',
                   (start_date, end_date))
    rows = cursor.fetchall()
    topic_counts = []
    for row in rows:
        topic_counts.append({
            'topic_name': row[0],
            'count': row[1],
            'count_date': row[2]
        })

    conn.close()

    return jsonify(topic_counts), 200

if __name__ == '__main__':
    app.run()

 