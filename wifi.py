<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
        }

        h1 {
            margin: 0;
        }

        .container {
            max-width: 800px;
            margin: 30px auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            margin: 10px 0;
        }

        a {
            text-decoration: none;
            color: #2980b9;
            font-weight: bold;
        }

        a:hover {
            text-decoration: underline;
        }

        .logout-btn {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #c0392b;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }

        .logout-btn:hover {
            background-color: #e74c3c;
        }
    </style>
</head>
<body>
    <header>
        <h1>Student Dashboard</h1>
    </header>

    <div class="container">
        <p>Available pages:</p>
        <ul>
            {% for page in pages %}
                <li>
                    <a href="{{ url_for('role_page', role='student', page=page) }}">
                        {{ page|capitalize }}
                    </a>
                </li>
            {% endfor %}
        </ul>

        <a class="logout-btn" href="{{ url_for('logout') }}">Logout</a>
    </div>
</body>
</html>