from . import get_naver_access_token
import requests
from config import settings

def get_product_list(
    searchKeywordType="CHANNEL_PRODUCT_NO",
    channelProductNos=None,
    originProductNos=None,
    groupProductNos=None,
    sellerManagementCode=None,
    productStatusTypes=None,
    page=1,
    size=50,
    orderType="NO",
    periodType="PROD_REG_DAY",
    fromDate=None,
    toDate=None
):
    """
    네이버 스마트스토어 상품 목록 조회 API 연동 예시
    """
    access_token = get_naver_access_token()
    url = f"{settings.NAVER_API_BASE_URL}/external/v1/products/search"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json;charset=UTF-8",
        "Content-Type": "application/json"
    }
    payload = {
        "searchKeywordType": searchKeywordType,
        "channelProductNos": channelProductNos or [],
        "originProductNos": originProductNos or [],
        "groupProductNos": groupProductNos or [],
        "sellerManagementCode": sellerManagementCode,
        "productStatusTypes": productStatusTypes or [],
        "page": page,
        "size": size,
        "orderType": orderType,
        "periodType": periodType,
        "fromDate": fromDate,
        "toDate": toDate
    }
    # None 값은 제거
    payload = {k: v for k, v in payload.items() if v is not None}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"상품 목록 조회 실패: {response.status_code} {response.text}")
