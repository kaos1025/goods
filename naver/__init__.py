# 네이버 스마트스토어 API 연동 구현 예정 

import requests
import time
import hashlib
import hmac
import base64
import bcrypt
import pybase64
from config import settings

# 전역 변수로 토큰 정보 관리 (실제 운영에서는 파일/DB 캐싱 권장)
_token_info = {
    "access_token": None,
    "expires_at": 0  # 만료 시각(UNIX timestamp)
}

def get_naver_access_token():
    """
    네이버 스마트스토어 커머스 API용 OAuth2 인증 토큰 발급 및 자동 갱신
    """
    now = int(time.time())
    # 만료 30분 전이면 재발급
    if _token_info["access_token"] and _token_info["expires_at"] - now > 1800:
        return _token_info["access_token"]

    url = "https://api.commerce.naver.com/external/v1/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    timestamp = str(int(time.time() * 1000))
    client_id = settings.NAVER_CLIENT_ID
    client_secret = settings.NAVER_CLIENT_SECRET
    type_ = "SELF"  # 문서에 따라 다름
    
    password = client_id + "_" + str(timestamp)
    hashed = bcrypt.hashpw(password.encode('utf-8'), client_secret.encode('utf-8'))
    client_secret_sign = pybase64.standard_b64encode(hashed).decode('utf-8')

    data = {
        "client_id": client_id,
        "timestamp": timestamp,
        "client_secret_sign": client_secret_sign,
        "type": type_,
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        token_info = response.json()
        _token_info["access_token"] = token_info["access_token"]
        # expires_in(초) + 현재 시각 = 만료 시각
        _token_info["expires_at"] = now + int(token_info.get("expires_in", 10800))
        return _token_info["access_token"]
    else:
        raise Exception(f"네이버 인증 실패: {response.status_code} {response.text}")
