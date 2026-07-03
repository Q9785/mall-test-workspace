import requests
import pytest

BASE_URL = "http://localhost:8085"


class TestLogin:

    def test_login_success(self):
        url = f"{BASE_URL}/sso/login"
        payload = {"username": "member", "password": "member123"}
        response = requests.post(url, data=payload)
        assert response.status_code == 200
        assert response.json().get("code") == 200
        assert response.json().get("data", {}).get("token") is not None

    def test_login_wrong_password(self):
        url = f"{BASE_URL}/sso/login"
        payload = {"username": "member", "password": "wrong"}
        response = requests.post(url, data=payload)
        assert response.status_code == 200
        assert response.json().get("code") != 200


class TestCart:

    def test_add_to_cart(self):
        login_url = f"{BASE_URL}/sso/login"
        login_payload = {"username": "member", "password": "member123"}
        login_response = requests.post(login_url, data=login_payload)
        assert login_response.status_code == 200
        token = login_response.json().get("data", {}).get("token")
        assert token is not None


        cart_url = f"{BASE_URL}/cart/add"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        cart_payload = {"productId": 27,"quantity": 1,"price": 2699,"productName": "小米8 全面屏游戏智能手机",
                        "productPic": "http://macro-oss.oss-cn-shenzhen.aliyuncs.com/mall/images/20221104/redmi_k50_01.jpg"}
        cart_response = requests.post(cart_url, json=cart_payload, headers=headers)
        assert cart_response.status_code == 200
        assert cart_response.json().get("code") == 200