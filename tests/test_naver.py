# 네이버 연동 테스트 코드 예시 
from naver.api import get_product_list
from datetime import datetime, timedelta

if __name__ == "__main__":
    today = datetime.today()
    a_weeks_ago = today - timedelta(days=7)
    from_date = a_weeks_ago.strftime("%Y-%m-%d")
    to_date = today.strftime("%Y-%m-%d")
    
    result = get_product_list(
        productStatusTypes=["SALE"],
        page=1,
        size=50,
        fromDate=from_date,
        toDate=to_date
    )
    print(result) 