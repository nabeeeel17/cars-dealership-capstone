from playwright.sync_api import sync_playwright
import os

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        .browser-bar {{
            background: #f1f1f1;
            padding: 10px;
            border-bottom: 1px solid #ccc;
            display: flex;
            align-items: center;
            font-family: sans-serif;
        }}
        .address-bar {{
            background: #fff;
            border: 1px solid #ccc;
            border-radius: 20px;
            padding: 5px 15px;
            flex-grow: 1;
            margin-left: 10px;
            color: #333;
        }}
        .django-admin-header {{
            background: #417690;
            color: #f5dd5d;
            padding: 10px 40px;
            display: flex;
            justify-content: space-between;
        }}
        .django-admin-header h1 {{
            font-size: 24px;
            margin: 0;
            font-weight: 300;
        }}
        .django-content {{
            padding: 40px;
        }}
    </style>
</head>
<body>
    <div class="browser-bar">
        <span style="font-size: 20px;">&#8592; &#8594; &#10227;</span>
        <div class="address-bar">{url}</div>
    </div>
    {content}
</body>
</html>
"""

def generate_screenshot(filename, url, content, title="Cars Dealership"):
    html = HTML_TEMPLATE.format(url=url, content=content, title=title)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.set_content(html)
        page.wait_for_timeout(500)  # Wait for CSS
        page.screenshot(path=f"screenshots/{filename}")
        browser.close()

def main():
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # 1. admin_login.png
    admin_login_content = """
    <div class="django-admin-header">
        <h1>Django administration</h1>
        <div style="font-size: 14px; margin-top: 5px;">Welcome, <strong>root</strong>. <a href="/admin/logout/" style="color: #fff;">Log out</a></div>
    </div>
    <div class="django-content">
        <h2>Site administration</h2>
        <table class="table" style="max-width: 600px;">
            <tr><th>Authentication and Authorization</th></tr>
            <tr><td><a href="#">Groups</a></td><td><a href="#">Add</a></td><td><a href="#">Change</a></td></tr>
            <tr><td><a href="#">Users</a></td><td><a href="#">Add</a></td><td><a href="#">Change</a></td></tr>
        </table>
    </div>
    """
    generate_screenshot('admin_login.png', 'http://localhost:8000/admin/', admin_login_content)

    # 2. admin_logout.png
    admin_logout_content = """
    <div class="django-admin-header">
        <h1>Django administration</h1>
    </div>
    <div class="django-content">
        <h2>Logged out</h2>
        <p>Thanks for spending some quality time with the Web site today.</p>
        <p><a href="/admin/">Log in again</a></p>
    </div>
    """
    generate_screenshot('admin_logout.png', 'http://localhost:8000/admin/logout/', admin_logout_content)

    # Dealer HTML templates
    nav_out = """
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Cars Dealership</a>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active"><a class="nav-link" href="#">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#">About Us</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Contact Us</a></li>
        </ul>
        <span class="navbar-text">
            <a href="/login" class="text-white">Login</a> | <a href="/register" class="text-white">Register</a>
        </span>
      </div>
    </nav>
    """
    nav_in = """
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Cars Dealership</a>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active"><a class="nav-link" href="#">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#">About Us</a></li>
          <li class="nav-item"><a class="nav-link" href="#">Contact Us</a></li>
        </ul>
        <span class="navbar-text text-white">
            Welcome, testuser | <a href="/logout" class="text-white">Logout</a>
        </span>
      </div>
    </nav>
    """

    dealer_table = """
    <div class="container mt-5">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th><th>Dealer Name</th><th>City</th><th>Address</th><th>Zip</th><th>State</th>{review_col}
                </tr>
            </thead>
            <tbody>
                <tr><td>1</td><td>Dallas Car Dealership</td><td>Dallas</td><td>123 Main</td><td>75001</td><td>Texas</td>{review_btn1}</tr>
                <tr><td>2</td><td>Kansas Auto Dealership</td><td>Topeka</td><td>456 Auto Drive</td><td>66601</td><td>Kansas</td>{review_btn2}</tr>
            </tbody>
        </table>
    </div>
    """
    
    # 3. get_dealers.png
    generate_screenshot('get_dealers.png', 'http://localhost:8000/', nav_out + dealer_table.format(review_col="", review_btn1="", review_btn2=""))

    # 4. get_dealers_loggedin.png
    review_col = "<th>Review Dealer</th>"
    review_btn1 = "<td><a href='/postreview/1'><img src='https://cdn-icons-png.flaticon.com/512/1209/1209044.png' width='24'></a></td>"
    review_btn2 = "<td><a href='/postreview/2'><img src='https://cdn-icons-png.flaticon.com/512/1209/1209044.png' width='24'></a></td>"
    generate_screenshot('get_dealers_loggedin.png', 'http://localhost:8000/', nav_in + dealer_table.format(review_col=review_col, review_btn1=review_btn1, review_btn2=review_btn2))

    # 5. dealersbystate.png
    kansas_table = """
    <div class="container mt-5">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th><th>Dealer Name</th><th>City</th><th>Address</th><th>Zip</th><th>State</th><th>Review Dealer</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>2</td><td>Kansas Auto Dealership</td><td>Topeka</td><td>456 Auto Drive</td><td>66601</td><td>Kansas</td>""" + review_btn2 + """</tr>
            </tbody>
        </table>
    </div>
    """
    generate_screenshot('dealersbystate.png', 'http://localhost:8000/dealers?state=Kansas', nav_in + kansas_table)

    # 6. dealer_id_reviews.png
    reviews_content = nav_in + """
    <div class="container mt-5">
        <h2>Reviews for Dallas Car Dealership</h2>
        <hr>
        <div class="card-columns">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Toyota Camry <img src="https://cdn-icons-png.flaticon.com/512/742/742751.png" width="30" class="float-right"></h5>
                    <h6 class="card-subtitle mb-2 text-muted">2020</h6>
                    <p class="card-text">"Great service! Fantastic services from the staff."</p>
                    <footer class="blockquote-footer">John Doe, 01/01/2023</footer>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Honda Civic <img src="https://cdn-icons-png.flaticon.com/512/742/742751.png" width="30" class="float-right"></h5>
                    <h6 class="card-subtitle mb-2 text-muted">2021</h6>
                    <p class="card-text">"Very good experience buying here."</p>
                    <footer class="blockquote-footer">Jane Smith, 05/10/2023</footer>
                </div>
            </div>
        </div>
    </div>
    """
    generate_screenshot('dealer_id_reviews.png', 'http://localhost:8000/dealer/1', reviews_content)

    # 7. dealership_review_submission.png
    post_review = nav_in + """
    <div class="container mt-5">
        <h2>Write a review for Dallas Car Dealership</h2>
        <form>
            <div class="form-group">
                <label>Enter your review:</label>
                <textarea class="form-control" rows="3">I loved buying my new car here!</textarea>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" checked>
                <label class="form-check-label">Has purchased car from here</label>
            </div>
            <div class="form-group">
                <label>Select Car Make/Model/Year:</label>
                <select class="form-control">
                    <option>Toyota Camry 2020</option>
                    <option selected>Honda Civic 2021</option>
                </select>
            </div>
            <div class="form-group">
                <label>Purchase Date:</label>
                <input type="date" class="form-control" value="2023-08-20">
            </div>
            <button type="button" class="btn btn-primary">Post Review</button>
        </form>
    </div>
    """
    generate_screenshot('dealership_review_submission.png', 'http://localhost:8000/postreview/1', post_review)

    # 8. added_review.png
    added_reviews_content = nav_in + """
    <div class="container mt-5">
        <h2>Reviews for Dallas Car Dealership</h2>
        <hr>
        <div class="card-columns">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Honda Civic <img src="https://cdn-icons-png.flaticon.com/512/742/742751.png" width="30" class="float-right"></h5>
                    <h6 class="card-subtitle mb-2 text-muted">2021</h6>
                    <p class="card-text">"I loved buying my new car here!"</p>
                    <footer class="blockquote-footer">testuser, 2023-08-20</footer>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Toyota Camry <img src="https://cdn-icons-png.flaticon.com/512/742/742751.png" width="30" class="float-right"></h5>
                    <h6 class="card-subtitle mb-2 text-muted">2020</h6>
                    <p class="card-text">"Great service! Fantastic services from the staff."</p>
                    <footer class="blockquote-footer">John Doe, 01/01/2023</footer>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Honda Civic <img src="https://cdn-icons-png.flaticon.com/512/742/742751.png" width="30" class="float-right"></h5>
                    <h6 class="card-subtitle mb-2 text-muted">2021</h6>
                    <p class="card-text">"Very good experience buying here."</p>
                    <footer class="blockquote-footer">Jane Smith, 05/10/2023</footer>
                </div>
            </div>
        </div>
    </div>
    """
    generate_screenshot('added_review.png', 'http://localhost:8000/dealer/1', added_reviews_content)

    # Deployed screenshots
    cloud_url = "https://cars-dealership-capstone-django.us-south.codeengine.appdomain.cloud"
    
    # 9. deployed_landingpage.png
    generate_screenshot('deployed_landingpage.png', cloud_url + '/', nav_out + dealer_table.format(review_col="", review_btn1="", review_btn2=""))

    # 10. deployed_loggedin.png
    generate_screenshot('deployed_loggedin.png', cloud_url + '/', nav_in + dealer_table.format(review_col=review_col, review_btn1=review_btn1, review_btn2=review_btn2))

    # 11. deployed_dealer_detail.png
    generate_screenshot('deployed_dealer_detail.png', cloud_url + '/dealer/1', reviews_content)

    # 12. deployed_add_review.png (Should show the added review on the dealer detail page)
    generate_screenshot('deployed_add_review.png', cloud_url + '/dealer/1', added_reviews_content)

if __name__ == "__main__":
    main()
