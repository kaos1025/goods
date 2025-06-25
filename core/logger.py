# 공통 로깅 유틸리티 구현 예정 

import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# 로거 설정 함수
def get_logger(name: str = "goods_project"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(LOG_LEVEL)
    return logger

# 사용 예시
# logger = get_logger(__name__)
# logger.info("로그 메시지 예시") 