from enum import Enum

from flask import request
from flask_restx import Namespace, Resource
from service import company_service

api = Namespace('company', path='/api/company')

class LangEnum(Enum):
    KO = 'ko'
    EN = 'en'
    JA = 'ja'


@api.route('')
class WantedCompanies(Resource):
    parser = api.parser()
    parser.add_argument('company_name', type=str, default=None, help='조회 할 회사명', required=True)
    @api.expect(parser)
    def get(self):
        """회사명 조회"""
        return company_service.search_company(request.args.get('company_name'))


@api.route('')
class WantedCompaniesChange(Resource):
    parser = api.parser()
    parser.add_argument('company_id', type=int, help='company key', required=True)
    parser.add_argument('col_target', type=LangEnum, help='추가 TAG Target(ko, en, ja)', required=True)
    parser.add_argument('company_tag', type=str, default=None, help='추가 TAG', required=True)

    @api.expect(parser)
    def put(self):
        """테그 추가 """
        return company_service.update_company(request.args.get('company_id'), request.args.get('col_target'), request.args.get('company_tag'))

    @api.expect(parser)
    def delete(self):
        """테그 삭제"""
        return company_service.delete_company(request.args.get('company_id'), request.args.get('col_target'), request.args.get('company_tag'))
