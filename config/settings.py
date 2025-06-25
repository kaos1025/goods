import os
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

# 네이버 스마트스토어 API 설정
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_API_BASE_URL = os.getenv("NAVER_API_BASE_URL", "https://api.commerce.naver.com")

# DB 설정 예시
DB_TYPE = os.getenv("DB_TYPE", "sqlite")
DB_NAME = os.getenv("DB_NAME", "goods.db")

# SQLite 연결 예시
if DB_TYPE == "sqlite":
    DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", DB_NAME)

# DB 설정 예시
# DB_HOST = os.getenv("DB_HOST", "localhost")
#DB_PORT = int(os.getenv("DB_PORT", 3306))
#DB_USER = os.getenv("DB_USER", "root")
#DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# 기타 설정
DEBUG = os.getenv("DEBUG", "False") == "True"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# 마켓별 연동 설정 예시 (필요시 추가)
ABLY_API_KEY = os.getenv("ABLY_API_KEY", "")
ZIGZAG_API_KEY = os.getenv("ZIGZAG_API_KEY", "")
BRANDI_API_KEY = os.getenv("BRANDI_API_KEY", "")

# 프로젝트 환경설정 및 API 키 예시
API_KEY = "your_api_key_here" 