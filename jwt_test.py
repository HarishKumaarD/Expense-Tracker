# File: quick_jwt_test.py
from dotenv import load_dotenv
load_dotenv()

try:
    from app.security import create_access_token
    
    # Test token creation
    test_data = {"sub": "test@example.com"}
    token = create_access_token(test_data)
    print("✅ JWT working correctly!")
    print(f"Sample token: {token[:50]}...")
    
except Exception as e:
    print(f"❌ JWT Error: {e}")
    
    # Debug information
    print("\nDebug info:")
    import jwt
    print(f"JWT package location: {jwt.__file__}")
    print(f"JWT package methods: {[method for method in dir(jwt) if not method.startswith('_')]}")