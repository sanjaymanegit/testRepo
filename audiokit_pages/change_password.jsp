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
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/audiokit","root","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 ResultSet resultSet = null;
 String sql =""; 
 %>    
     
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Admin </title>
<style>
body {
  color: black;
  font-family: Calibri;
  font-size: 90%;
}

.btn-group button {
  background-color: #4CAF50 ; /* Green background #4CAF50*/
  border: 1px solid green; /* Green border */
  color: white; /* White text */
  padding: 5px 40px; /* Some padding */
  cursor: pointer; /* Pointer/hand icon */
  float: left; /* Float the buttons side by side */
}

/* Clear floats (clearfix hack) */
.btn-group:after {
  content: "";
  clear: both;
  display: table;
}

.btn-group button:not(:last-child) {
  border-right: none; /* Prevent double borders */
}

/* Add a background color on hover */
.btn-group button:hover {
  background-color: #3e8e41;
}

</style>
<script>
function f_save()
{
if (document.change_pwd_form.old_pwd.value == "")
{
    alert("Old password must be filled out");
    return false;
 }
else if(document.change_pwd_form.new_pwd.value == "")
{
    alert("New Password must be filled out");
    return false;
 }
else if(document.change_pwd_form.retype_new_pwd.value == "")
{
    alert("Re-Type New Password must be filled out");
    return false;
 } 
else if(document.change_pwd_form.new_pwd.value != document.change_pwd_form.retype_new_pwd.value)
{
    alert("Re-Typed New Passwor and New Password must be same");
    return false;
 } 
else 
{	
	document.change_pwd_form.flag_save.value='save';
	document.change_pwd_form.action = "change_password.jsp";
	document.change_pwd_form.submit();
}		
}

</script>

</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="change_pwd_form">
<%
String user_login_id=request.getParameter("user_login_id");
String flag_save=request.getParameter("flag_save");
String old_pwd ="" ;
String new_pwd ="" ; 
String retype_new_pwd ="" ; 
if (flag_save != null && flag_save.equals("save"))
{
 old_pwd = request.getParameter("old_pwd");
 new_pwd = request.getParameter("new_pwd");	 
 retype_new_pwd = request.getParameter("retype_new_pwd");
 statement=con.createStatement(); 
 sql="UPDATE BUSINESS_USERS SET USER_PWD='"+new_pwd+"', UPDATED_BY='"+user_login_id+"' WHERE USER_LOGIN_ID ='"+user_login_id+"' AND USER_PWD='"+old_pwd+"'"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 out.println("Password Changed Sccessfully !!!!!!");
 }	
%>
<h3>  Change My Password  </h3>   
<input type="hidden" value="x" name="flag_save">
<input type="hidden" name="user_login_id" value="<%=user_login_id%>">
<table border=0  style="height:150px;">
<tr>
<td width="30%">Old Password :</td>
<td width="70%"> <input type="password" name="old_pwd" value=""</td>
</tr>
<tr>
<td width="30%">New Password :</td>
<td width="70%"><input type="password" name="new_pwd" value=""></td>
</tr>
<tr>
<td width="30%"> Retype New Password :</td>
<td width="70%"> <input type="password" name="retype_new_pwd" value="">
</td>
</tr>
<tr>
<td width="20%">
</td>
<td width="70%">
<div class="btn-group">
  <button type="submit" name="add_role" onclick="f_save()">Save</button> <button type="reset">Reset</button> 
</div>  
</td>
</tr>
</table>
<%
%>
</form>
</font>
</body>
</html>