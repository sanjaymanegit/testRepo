<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>

<!DOCTYPE html>
<html lang="en"> <!--<![endif]-->
<head>
<meta charset="utf-8">
<title>Paper Stack</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
<div class="container">
    <section id="content">
        <form action="main_page.jsp" method="post">
            <h1>Login Form</h1>
            <div>
                <input type="text" placeholder="Username" required="" value="ADMIN" id="username" name="username"/>
            </div>
            <div>
                <input type="password" placeholder="Password" required="" value="ADMIN1234" id="password" name="password"/>
            </div>
            <div>
                <input type="submit" value="Log in" />
                <a href="#">Lost your password?</a>
                <a href="#">Register</a>
            </div>
        </form>
        
    </section>
</div>
</body>
</html>