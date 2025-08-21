from flask import Blueprint

import controllers 

companies = Blueprint('companies', __name__)

@companies.route('/company', methods=['POST'])
def create_company():
    return controllers.create_company()

@companies.route('/company/<company_id>', methods=['GET'])
def get_company_by_id(company_id):
    return controllers.get_company_by_id(company_id)

@companies.route('/companies', methods=['GET'])
def get_all_companies():
    return controllers.get_all_companies()

@companies.route('/company/<company_id>', methods=['PUT'])
def update_company_by_id(company_id):
    return controllers.update_company_by_id(company_id)

@companies.route('/company/<company_id>', methods=['DELETE'])
def delete_company_by_id(company_id):
    return controllers.delete_company_by_id(company_id)