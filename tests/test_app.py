import os
import sys

# 프로젝트 루트(= fastapi-ci-cd-demo)를 파이썬 모듈 검색 경로에 추가
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from app.main import health_check, list_items, add_item


def test_health():
    assert health_check() == {"status": "ok"}


def test_add_item():
    # 각 테스트는 새 프로세스에서 돌아가므로 items 리스트는 매번 초기 상태라고 가정
    add_item("apple")
    add_item("banana")
    assert list_items() == {"items": ["apple", "banana"]}
