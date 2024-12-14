from flask import jsonify
from dao.company_dao import Company
from config.database import db


def search_company(search_txt):
    if not search_txt:
        return jsonify({"error": "검색명을 입력 해주세요."}), 400

    companies = []
    company_ko_info = Company.query.filter(Company.company_name_ko.ilike(f"%{search_txt}%")).all()
    companies = add_companies(companies, company_ko_info)
    company_en_info = Company.query.filter(Company.company_name_en.ilike(f"%{search_txt}%")).all()
    companies = add_companies(companies, company_en_info)
    company_ja_info = Company.query.filter(Company.company_name_ja.ilike(f"%{search_txt}%")).all()
    companies = add_companies(companies, company_ja_info)
    company_tag_ko_info = Company.query.filter(Company.company_tag_ko.ilike(f"%{search_txt}%")).all()
    companies = add_companies(companies, company_tag_ko_info)
    company_tag_en_info = Company.query.filter(Company.company_tag_en.ilike(f"%{search_txt}%")).all()
    companies = add_companies(companies, company_tag_en_info)
    company_tag_ja_info = Company.query.filter(Company.company_tag_ja.ilike(f"%{search_txt}%")).all()
    companies = add_companies(companies, company_tag_ja_info)

    unique_companies = list({company['id']: company for company in companies}.values())

    return jsonify(unique_companies)


def add_companies(companies, company_info):
    if company_info:
        companies += [company.to_dict() for company in company_info]
    return companies


def update_company(company_id, col_target, company_tag):
    company = Company.query.get(company_id).to_dict()

    if not company:
        return jsonify({"error": "Company not found"}), 404

    company[f"company_tag_{col_target}"] += ("|" if company[f"company_tag_{col_target}"] else "") + company_tag

    db.session.commit()

    return jsonify(company)


def delete_company(company_id, col_target, company_tag):
    company = Company.query.get(company_id).to_dict()

    if not company:
        return jsonify({"error": "Company not found"}), 404

    tag = company[f"company_tag_{col_target}"].split("|")
    tag.remove(company_tag)
    company[f"company_tag_{col_target}"] = '|'.join(tag)

    db.session.commit()

    return jsonify(company)
