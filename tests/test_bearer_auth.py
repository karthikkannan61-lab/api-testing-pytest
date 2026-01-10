import pytest
from clients.bearer_client import BearerClient
from config.config import Config


# =========================================================
# HELPER FUNCTIONS (REUSABLE ASSERTIONS)
# =========================================================

def get_product_by_id(products, product_id):
    """
    Returns product dictionary by product_id
    Fails fast if product is not found
    """
    product = next((p for p in products if p["id"] == product_id), None)
    assert product is not None, f"Product with id={product_id} not found"
    return product


def assert_rating_and_count(rating):
    """
    Contract validation for rating object
    """
    # Rating object existence
    assert rating is not None, "Rating is missing"

    # Structure validation
    assert isinstance(rating, dict), "Rating is not a dictionary"
    assert "rate" in rating, "rate key missing in rating"
    assert "count" in rating, "count key missing in rating"

    # Rate validation
    assert isinstance(rating["rate"], (int, float)), "rate is not numeric"
    assert 0 <= rating["rate"] <= 5, "rate is outside 0–5 range"

    # Count validation
    assert isinstance(rating["count"], int), "count is not integer"
    assert rating["count"] >= 0, "count is negative"


# =========================================================
# SMOKE TESTS (SERVICE HEALTH CHECK)
# =========================================================

@pytest.mark.smoke
def test_bearer_client_smoke():
    """
    Smoke Test:
    • Login works
    • Token is generated
    • Protected endpoint is accessible
    """
    client = BearerClient(Config.BASE_URL_3)

    login_response = client.login(username=Config.FAKESTORE_USERNAME, password=Config.FAKESTORE_PASSWORD)
    assert login_response.status_code in (200,201)
    assert client.token is not None

    products_response = client.get_products()
    assert products_response.status_code in (200,201)
    assert products_response.json() is not None

# =========================================================
# CONTRACT TESTS (PARAMETRIZED – PRODUCT IDS 1 TO 10)
# =========================================================

@pytest.mark.contract
@pytest.mark.parametrize("product_id", range(1, 11))
def test_products_rating_and_count_contract(product_id):
    """
    Contract Test:
    • Validates rating + count for products 1–10
    • Uses parametrization
    """
    client = BearerClient(Config.BASE_URL_3)

    login_response = client.login(username=USERNAME, password=PASSWORD)
    assert login_response.status_code in (200, 201)
    assert client.token is not None

    products_response = client.get_products()
    assert products_response.status_code in (200, 201)

    products = products_response.json()
    product = get_product_by_id(products, product_id)

    assert_rating_and_count(product["rating"])
