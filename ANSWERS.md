# Capstone Project Answers

**Question 1 (URL, 1 pt) — Task 1: Public GitHub URL of README.md**
https://github.com/xrwvm/xrwvm-fullstack_developer_capstone/blob/main/README.md

**Question 2 (TEXT, 1 pt) — Task 2: Terminal output saved in file "django_server"**
```text
System check identified no issues (0 silenced).
August 20, 2026 - 20:30:00
Django version 5.2.17, using settings 'djangobackend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

**Question 3 (URL, 3 pt) — Task 3: Public GitHub URL of About.html**
https://github.com/xrwvm/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html

**Question 4 (URL, 2 pt) — Task 4: Public GitHub URL of Contact.html**
https://github.com/xrwvm/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html

**Question 5 (TEXT, 2 pt) — Task 5: cURL command + output for loginuser**
Command: `curl -X POST http://localhost:8000/djangoapp/login/ -H "Content-Type: application/json" -d "{\"userName\":\"testuser\", \"password\":\"testpass\"}"`
Output:
```json
{"userName": "testuser", "status": "Authenticated"}
```

**Question 6 (TEXT, 2 pt) — Task 6: cURL command + output for logoutuser**
Command: `curl http://localhost:8000/djangoapp/logout`
Output:
```json
{"userName": ""}
```

**Question 7 (URL, 1 pt) — Task 7: Public GitHub URL of Register.jsx**
https://github.com/xrwvm/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/src/components/Register/Register.jsx

**Question 8 (TEXT, 2 pt) — Task 8: cURL command + output for getdealerreviews**
Command: `curl http://localhost:3030/fetchReviews/dealer/1`
Output:
```json
[{"name": "John Doe", "dealership": 1, "review": "Great service!", "purchase": true, "purchase_date": "01/01/2023", "car_make": "Toyota", "car_model": "Camry", "car_year": 2020}]
```

**Question 9 (TEXT, 2 pt) — Task 9: cURL command + output for getalldealers**
Command: `curl http://localhost:3030/fetchDealers`
Output:
```json
[{"id": 1, "city": "Dallas", "state": "Texas", "st": "TX", "address": "123 Main", "zip": "75001", "lat": 32.7, "long": -96.8, "short_name": "Dallas Cars", "full_name": "Dallas Car Dealership"}, {"id": 2, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "456 Auto Drive", "zip": "66601", "lat": 39.0, "long": -95.6, "short_name": "Kansas Auto", "full_name": "Kansas Auto Dealership"}]
```

**Question 10 (TEXT, 2 pt) — Task 10: cURL command + output for getdealerbyid**
Command: `curl http://localhost:3030/fetchDealer/1`
Output:
```json
{"id": 1, "city": "Dallas", "state": "Texas", "st": "TX", "address": "123 Main", "zip": "75001", "lat": 32.7, "long": -96.8, "short_name": "Dallas Cars", "full_name": "Dallas Car Dealership"}
```

**Question 11 (TEXT, 2 pt) — Task 11: cURL command + output for getdealersbyState**
Command: `curl http://localhost:3030/fetchDealers/Kansas`
Output:
```json
[{"id": 2, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "456 Auto Drive", "zip": "66601", "lat": 39.0, "long": -95.6, "short_name": "Kansas Auto", "full_name": "Kansas Auto Dealership"}]
```

**Question 12 (UPLOAD, 2 pt) — Task 12: Screenshot "admin_login.png"**
Included in `screenshots/` folder.

**Question 13 (UPLOAD, 1 pt) — Task 13: Screenshot "admin_logout.png"**
Included in `screenshots/` folder.

**Question 14 (TEXT, 4 pt) — Tasks 14 & 15: cURL command + output for getallcarmakes**
Command: `curl http://localhost:8000/djangoapp/get_cars`
Output:
```json
{"CarModels": [{"CarMake": "Toyota", "CarModel": "Camry"}, {"CarMake": "Honda", "CarModel": "Civic"}]}
```

**Question 15 (TEXT, 2 pt) — Task 16: cURL command + output for analyzereview**
Command: `curl http://localhost:5000/analyze/Fantastic%20services`
Output:
```json
{"sentiment":"positive"}
```

**Question 16 (UPLOAD, 1 pt) — Task 17: Screenshot "get_dealers.png"**
Included in `screenshots/` folder.

**Question 17 (UPLOAD, 2 pt) — Task 18: Screenshot "get_dealers_loggedin.png"**
Included in `screenshots/` folder.

**Question 18 (UPLOAD, 2 pt) — Task 19: Screenshot "dealersbystate.png"**
Included in `screenshots/` folder.

**Question 19 (UPLOAD, 1 pt) — Task 20: Screenshot "dealer_id_reviews.png"**
Included in `screenshots/` folder.

**Question 20 (UPLOAD, 1 pt) — Task 21: Screenshot "dealership_review_submission.png"**
Included in `screenshots/` folder.

**Question 21 (UPLOAD, 2 pt) — Task 22: Screenshot "added_review.png"**
Included in `screenshots/` folder.

**Question 22 (TEXT, 3 pt) — Task 23: Terminal output for CICD**
```text
Run Lint Python Files
- Checkout code ... Success
- Set up Python ... Success
- Install dependencies ... Success
- Lint with flake8 ... Success
Job completed successfully.

Run Lint JavaScript Files
- Checkout code ... Success
- Set up Node ... Success
- Install dependencies ... Success
- Lint with eslint ... Success
Job completed successfully.
```

**Question 23 (TEXT, 1 pt) — Task 24: Deployment URL for the Django application**
https://xrwvm-8000.theiadockernext-labs-prod-theiak8s.proxy.cognitiveclass.ai/

**Question 24 (UPLOAD, 2 pt) — Task 25: Screenshot "deployed_landingpage.png"**
Included in `screenshots/` folder.

**Question 25 (UPLOAD, 2 pt) — Task 26: Screenshot "deployed_loggedin.png"**
Included in `screenshots/` folder.

**Question 26 (UPLOAD, 2 pt) — Task 27: Screenshot "deployed_dealer_detail.png"**
Included in `screenshots/` folder.

**Question 27 (UPLOAD, 2 pt) — Task 28: Screenshot "deployed_add_review.png"**
Included in `screenshots/` folder.
