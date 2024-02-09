import random
import string
import os
try:
    from google_play_scraper import app, exceptions
except:
    os.system('pip install google_play_scraper')

def generate_code():
    alphanumeric = string.ascii_uppercase + string.digits
    return ''.join(''.join(random.choice(alphanumeric) for _ in range(4)) for _ in range(4))

def check_redeemability(codes, country="us"):
    try:
        redeemable_codes = []    
        for code in codes:
            try:
                result = app(code, lang="en", country=country)
                if result["url"]:
                    redeemable_codes.append({"code": code, "url": result["url"]})
            except exceptions.NotFoundError:
                print(f"Code {code} is not found on the Google Play Store.")
            except exceptions.ExtraHTTPError:
                print(f"An HTTP error occurred while checking code {code}.")    
        return redeemable_codes
    except:
        check_redeemability(codes, country)

codes_to_check = [generate_code() for _ in range(5000)]
country = "us"
redeemable_codes_list = check_redeemability(codes_to_check, country)

print("Generated Codes:")
for i, generated_code in enumerate(codes_to_check, start=1):
    print(f"{i}. {generated_code}")

print("\nRedeemable Codes:")
for redeemable_code in redeemable_codes_list:
    print(f"Code: {redeemable_code['code']}, URL: {redeemable_code['url']}")
