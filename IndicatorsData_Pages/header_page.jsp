<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import ="java.sql.*" %>
<%@page import ="javax.sql.*" %>
<%
Class.forName("com.mysql.jdbc.Driver"); 
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 ResultSet resultSet = null;
 String username = request.getParameter("username");
String password = request.getParameter("password");	
String status_str ="disabled" ;
 %> 	
	
	
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
<style>
body {  
    background-color: Gainsboro;
  color: black;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 80%;
}
</style>
<script>
function f_ch_password()
{
document.header_form.target = "rightbottomframe";
document.header_form.action="change_password.jsp";
document.header_form.submit();
}
function f_admin()
{
document.header_form.target = "leftbottomframe";
document.header_form.action="admin_frame.html";
document.header_form.submit();
}
</script>
</head>
<body>
<form name="header_form">
<table border="0" width="1800">
<tr> <td width="20%">
  <marquee><h1> Online data is available <h1></marquee>
  </td>
  <td width="55%" align="right">
 <table border="0">
 <tr width="100%">   
 <% 
try {	
statement=con.createStatement();  
String sql="SELECT FIRST_NAME, LAST_NAME,ROLE_NAME,EMAIL_ID FROM business_users where USER_LOGIN_ID='"+username+"' and USER_PWD='"+password+"' AND ROLE_NAME='ADMIN'";
resultSet=statement.executeQuery(sql);
while(resultSet.next())
{				
status_str ="enabled" ; 
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<td>
<td><input type="button" name="batch_reports" value="Batch Reports"  onclick=""></td>
<td><input type="button" name="report_button" value="Other Reports"  onclick="" <%=status_str%>></td>
 <td><input type="button" name="admin_button" value="Admin"  onclick="" <%=status_str%>></td>
 <td><input type="button" name="change_my_password" value="Change My Password"  onclick="f_ch_password()"></td>  
 </tr> 
 </table>
 </td>
  <td width="25%" >
  

<table border="0" align="right">
<% 
try {	
statement=con.createStatement();  
String sql="SELECT FIRST_NAME, LAST_NAME,ROLE_NAME,EMAIL_ID FROM business_users where USER_LOGIN_ID='"+username+"' and USER_PWD='"+password+"'";
resultSet=statement.executeQuery(sql);
while(resultSet.next())
{				
%>
<tr><td>User Name :</td><td><%=resultSet.getString("FIRST_NAME")%> <%=resultSet.getString("LAST_NAME")%></td></tr>
<tr><td>User Role :</td><td><%=resultSet.getString("ROLE_NAME")%></td></tr>
<tr><td>User Email Id :</td><td><%=resultSet.getString("EMAIL_ID")%></td></tr>
 <%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<tr><td><a href="http://www.samruddhielectrotech.com/IndicatorsData_Pages/" target="_top"> Sign Out </a></td><td></td></tr>
 </table>
 </td>
 </tr>
 </table> 
</form> 
</body>
</html>