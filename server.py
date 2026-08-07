import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os

# Configuration
CONFIG_PATH = r"C:\Users\Kyra\hermes_config\litellm_config.yaml"

# Model Mapping
# When a button is clicked, we want to update the 'chat' model_name entry
# because the dashboard treats 'chat' as the primary slot.
MODEL_MAP = {
    "chat": "openai/google/gemma-4-12b-qat",
    "coder": "openai/qwen/qwen2.5-coder-14b",
    "reasoning": "openai/mistralai/ministral-3-14b-reasoning",
    "deep-logic": "openai/ternary-bonsai-27b@q4_1"
}

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/switch':
            content_length = int(self.headers['Content-Length'])
            post_data = self.r.read(content_length).decode('utf-8')
            data = json.loads(post_data)
            
            model_key = data.get("model")
            if model_key in MODEL_MAP:
                new_model = MODEL_MAP[model_key]
                
                # Read the current config
                with open(CONFIG_PATH, 'r') as f:
                    lines = f.readlines()
                
                # Find the 'chat' section and replace its model line
                new_lines = []
                skip_next = False
                for line in lines:
                    if line.strip().startswith("- model_name: chat"):
                        new_lines.append(line)
                        skip_next = True
                        continue
                    if skip_next:
                        if line.strip().startswith("model:"):
                            new_lines.append(f"      model: {new_model}\n")
                            skip_next = False
                        else:
                            new_lines.append(line)
                    else:
                        new_lines.append(line)
                
                with open(CONFIG_PATH, 'w') as f:
                    f.writelines(new_lines)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "model": new_model}).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": "Invalid model"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run():
    server = HTTPServer(('127.0.0.1', 8080), RequestHandler)
    print("State Manager running on http://127.0.0.1:8080")
    server.serve_forever()

if __name__ == '__main__':
    run()