# Task Map Checklist

1. **README.md**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/README.md](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/README.md)
2. **server/frontend/static/About.html**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/frontend/static/About.html](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/frontend/static/About.html)
3. **server/frontend/static/Contact.html**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/frontend/static/Contact.html](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/frontend/static/Contact.html)
4. **server/frontend/src/components/Register/Register.jsx**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/frontend/src/components/Register/Register.jsx](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/frontend/src/components/Register/Register.jsx)
5. **Django auth endpoints**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/djangoapp/views.py](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/server/djangoapp/views.py)
6. **Dealer/review API endpoints**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/database/app.js](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/database/app.js)
7. **Flask sentiment analysis endpoint**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/sentiment_analyzer/app.py](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/sentiment_analyzer/app.py)
8. **Django admin**: Run `python manage.py createsuperuser`. Manual screenshot: `admin_login`, `admin_logout`
9. **Home page (Django + React)**: Manual screenshot: `deployed_landingpage`
10. **CI/CD**: [https://github.com/yan-ulc/cars-dealership-capstone/blob/main/.github/workflows/main.yml](https://github.com/yan-ulc/cars-dealership-capstone/blob/main/.github/workflows/main.yml). Run CI/CD manual screenshot: `CICD`
11. **Deployment**: Manual screenshot: `deployed_landingpage`, `deployed_loggedin`, `deployed_dealer_detail`, `deployed_add_review`

## Commands to generate output
- `django_server`: `python manage.py runserver > django_server.txt`
- `loginuser`: `curl -X POST http://localhost:8000/djangoapp/login/ -H "Content-Type: application/json" -d "{\"userName\":\"testuser\", \"password\":\"testpass\"}" > loginuser.txt`
- `logoutuser`: `curl -X POST http://localhost:8000/djangoapp/logout/ > logoutuser.txt`
- `getalldealers`: `curl http://localhost:3030/dealers > getalldealers.txt`
- `getdealerbyid`: `curl http://localhost:3030/dealers/1 > getdealerbyid.txt`
- `getdealersbyState`: `curl http://localhost:3030/dealers?state=Kansas > getdealersbyState.txt`
- `getdealerreviews`: `curl http://localhost:3030/reviews/1 > getdealerreviews.txt`
- `getallcarmakes`: `curl http://localhost:3030/cars > getallcarmakes.txt`
- `analyzereview`: `curl "http://localhost:5000/analyze?text=Fantastic%20services" > analyzereview.txt`
- `CICD`: Check the GitHub Actions tab.
- `deploymentURL`: Copy your IBM Cloud Code Engine URL.

## Manual Screenshots
- `admin_login.png`: Take screenshot of /admin login page
- `admin_logout.png`: Take screenshot of /admin logout page
- `get_dealers.png`: Screenshot of home page showing dealers before login
- `get_dealers_loggedin.png`: Screenshot of home page showing dealers and logged in state
- `dealersbystate.png`: Screenshot of home page filtered by state (e.g. Kansas)
- `dealer_id_reviews.png`: Screenshot of dealer detail page showing reviews
- `dealership_review_submission.png`: Screenshot of the post review form
- `added_review.png`: Screenshot of dealer detail page showing the newly added review
- `deployed_landingpage.png`: Screenshot of deployed landing page
- `deployed_loggedin.png`: Screenshot of deployed app logged in
- `deployed_dealer_detail.png`: Screenshot of deployed dealer detail page
- `deployed_add_review.png`: Screenshot of deployed post review page
