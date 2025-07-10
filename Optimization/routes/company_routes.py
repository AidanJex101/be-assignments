@company.route('/companies')
def get_companies():
    company_query = db.session.query(Companies).all()

    if not query:
        return jsonify({"message": "no companies found"}), 404

    else:
      return jsonify({"message": "companies found", "results": companies_schema.dump(query)}), 200