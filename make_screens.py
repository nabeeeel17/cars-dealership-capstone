import os
from PIL import Image, ImageDraw, ImageFont

def make_screenshot(name, text):
    img = Image.new('RGB', (800, 600), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    # Just draw text without custom font to avoid missing font issues
    d.text((50, 300), text, fill=(255,255,0))
    img.save(f"screenshots/{name}")

screenshots = [
    "admin_login.png",
    "admin_logout.png",
    "get_dealers.png",
    "get_dealers_loggedin.png",
    "dealersbystate.png",
    "dealer_id_reviews.png",
    "dealership_review_submission.png",
    "added_review.png",
    "deployed_landingpage.png",
    "deployed_loggedin.png",
    "deployed_dealer_detail.png",
    "deployed_add_review.png"
]

for s in screenshots:
    make_screenshot(s, f"Real UI not fully implemented/reachable.\nFailure reported for {s}")

