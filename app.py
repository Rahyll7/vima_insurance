from flask import Flask, jsonify, request
from flask_cors import CORS  
import json

app = Flask(__name__)

CORS(app)

def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

data = load_data()

@app.route('/get_policies', methods=['GET'])
def get_policies():
    if data:
        return jsonify({"data": data, "status": 200, "message": "data has been successfully fetched"})
    else:
        return jsonify({"message": "data not found", "status": 404})

@app.route("/search_policies", methods=["POST"])
def search_policies():
    search_term = request.json.get('name', '').lower()
    print(search_term, "check")
    result = [policy for policy in data if search_term in policy['name'].lower()]
    if result:
        return jsonify({"data": result, "status": 200, "message": "search results found"})
    else:
        return jsonify({"message": "no policies found", "status": 404})

@app.route("/filter_policies", methods=["POST"])
def filter_policies():
    try:
        filters = request.json or {}
        filtered_data = data.copy()

        min_premium = filters.get('min_premium')
        if min_premium and str(min_premium).isdigit():
            filtered_data = [p for p in filtered_data if p['premium'] >= int(min_premium)]

        max_premium = filters.get('max_premium')
        if max_premium and str(max_premium).isdigit():
            filtered_data = [p for p in filtered_data if p['premium'] <= int(max_premium)]

        policy_type = filters.get('type')
        if policy_type and isinstance(policy_type, str) and policy_type.strip():
            filtered_data = [p for p in filtered_data if policy_type.lower() in p['type'].lower()]

        min_coverage = filters.get('min_coverage')
        if min_coverage and str(min_coverage).isdigit():
            filtered_data = [p for p in filtered_data if p['coverage'] >= int(min_coverage)]

        sort_direction = filters.get('sort')
        if sort_direction and sort_direction.lower() in ['asc', 'desc']:
            reverse = sort_direction.lower() == 'desc'
            filtered_data = sorted(filtered_data, key=lambda x: x['premium'], reverse=reverse)

        if filtered_data:
            return jsonify({
                "status": 200,
                "message": "Policies filtered successfully",
                "data": filtered_data
            })

        return jsonify({
            "status": 404,
            "message": "No matching policies found",
            "data": []
        })

    except Exception as e:
        return jsonify({
            "status": 500,
            "message": "Internal server error",
            "data": []
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
