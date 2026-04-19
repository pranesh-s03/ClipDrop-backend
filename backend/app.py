from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import uuid, time, os, threading, base64
 
app = Flask(__name__)
CORS(app)
 
# In-memory store: { code: { type, content, filename, mime, expires } }
store = {}
EXPIRY = 600  # 10 minutes
 
def cleanup():
    while True:
        now = time.time()
        expired = [k for k, v in store.items() if v['expires'] < now]
        for k in expired:
            del store[k]
        time.sleep(30)
 
threading.Thread(target=cleanup, daemon=True).start()
 
def gen_code():
    while True:
        code = str(uuid.uuid4())[:6].upper()
        if code not in store:
            return code
 
@app.route('/api/push', methods=['POST'])
def push():
    data = request.json
    if not data:
        return jsonify({'error': 'No data'}), 400
 
    content_type = data.get('type')  # 'text' or 'file'
    
    if content_type == 'text':
        text = data.get('content', '')
        if not text:
            return jsonify({'error': 'Empty text'}), 400
        if len(text) > 500_000:
            return jsonify({'error': 'Text too large (max 500KB)'}), 400
        code = gen_code()
        store[code] = {
            'type': 'text',
            'content': text,
            'expires': time.time() + EXPIRY
        }
 
    elif content_type == 'file':
        filename = data.get('filename', 'file')
        mime = data.get('mime', 'application/octet-stream')
        b64 = data.get('content', '')
        if not b64:
            return jsonify({'error': 'No file content'}), 400
        # Check size (base64 is ~4/3 of original)
        if len(b64) > 10_000_000:  # ~7.5MB original
            return jsonify({'error': 'File too large (max 7MB)'}), 400
        code = gen_code()
        store[code] = {
            'type': 'file',
            'content': b64,
            'filename': filename,
            'mime': mime,
            'expires': time.time() + EXPIRY
        }
    else:
        return jsonify({'error': 'Invalid type'}), 400
 
    remaining = int(store[code]['expires'] - time.time())
    return jsonify({'code': code, 'expires_in': remaining})
 
@app.route('/api/pull/<code>', methods=['GET'])
def pull(code):
    code = code.upper()
    item = store.get(code)
    if not item:
        return jsonify({'error': 'Code not found or expired'}), 404
    
    remaining = int(item['expires'] - time.time())
    
    if item['type'] == 'text':
        return jsonify({
            'type': 'text',
            'content': item['content'],
            'expires_in': remaining
        })
    elif item['type'] == 'file':
        return jsonify({
            'type': 'file',
            'content': item['content'],
            'filename': item['filename'],
            'mime': item['mime'],
            'expires_in': remaining
        })
 
@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok', 'items': len(store)})
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
