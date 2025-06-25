# 공통 예외처리 클래스 구현 예정 

class GoodsBaseException(Exception):
    """프로젝트 공통 베이스 예외"""
    pass

class APIRequestException(GoodsBaseException):
    """API 요청 실패 예외"""
    pass

class DataParseException(GoodsBaseException):
    """데이터 파싱 실패 예외"""
    pass

# 사용 예시
# raise APIRequestException("API 호출 실패!") 