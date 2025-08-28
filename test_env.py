from app.core.config import get_settings  # path ঠিক করো

def main():
    settings = get_settings()
    print("✅ DATABASE_URL:", settings.DATABASE_URL)
    print("✅ JWT_SECRET:", settings.JWT_SECRET)
    print("✅ JWT_ALG:", settings.JWT_ALG)
    print("✅ ACCESS_TOKEN_EXPIRE_MINUTES:", settings.ACCESS_TOKEN_EXPIRE_MINUTES)

if __name__ == "__main__":
    main()
