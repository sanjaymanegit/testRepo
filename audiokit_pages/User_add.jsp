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
function f_add()
{
	
if (document.user_add_form.f_name.value == "")
{
    alert("First Name must be filled out");
    return false;
 }
 else if(document.user_add_form.l_name.value == "")
{
    alert("Last Name must be filled out");
    return false;
 }
else if(document.user_add_form.role_id.value == "")
{
    alert("Please select Role.");
    return false;
 }	
else if(document.user_add_form.email_id.value == "")
{
    alert("email_id must be filled out.");
    return false;
 }	
else if(document.user_add_form.loging_id.value == "")
{
    alert("Login Id must be filled out.");
    return false;
 }	
else if(document.user_add_form.u_password.value == "")
{
    alert("Password must be filled out.");
    return false;
 }		
else if(document.user_add_form.re_u_password.value == "")
{
    alert("Retype Password must be filled out.");
    return false;
 }	
else if(document.user_add_form.re_u_password.value != document.user_add_form.u_password.value) 
{
    alert("Password and Retype Password must be same.");
    return false;
 }	 
else 
{
	document.user_add_form.flag_add.value='add';
	document.user_add_form.action = "User_add.jsp";
	document.user_add_form.submit();
}		
}

</script>

</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="user_add_form" method="post">
<h3>  ADD USER </h3>   ( Note: All fields are mandatory)
<input type="hidden" value="x" name="flag_add">
<table border=0  style="height:300px;">
<tr>
<td width="30%">First Name :</td>
<td width="70%"> <input type="text" name="f_name"></td>
</tr>
<tr>
<td width="30%">Last Name :</td>
<td width="70%"><input type="text" name="l_name"></td>
</tr>
<tr>
<td width="30%">Role :</td>
<td width="70%">
 <SELECT NAME="role_id" style="width: 150px;">
<option value="">Select Role</option>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT ROLE_NAME FROM role_mst where ROLE_NAME <> 'ADMIN'";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<option value="<%=resultSet.getString("ROLE_NAME")%>"><%=resultSet.getString("ROLE_NAME")%></option>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</SELECT>
</td>
</tr>
<tr>
<td width="30%">Email ID :</td>
<td width="70%"><input type="text" name="email_id"></td>
</tr>
<tr>
<td width="30%">Login Id:</td>
<td width="70%"><input type="text" name="loging_id"></td>
</tr>
<tr>
<td width="30%">Password:</td>
<td width="70%"><input type="password" name="u_password"></td>
</tr>
<tr>
<td width="30%">Retype Password:</td>
<td width="70%"><input type="password" name="re_u_password"></td>
</tr>
<tr>
<td width="20%">
</td>
<td width="70%">
<div class="btn-group">
  <button type="button" onclick="f_add()">Add</button> <button type="reset">Reset</button> 
</div>  
</td>
</tr>
</table>
<%
String flag=request.getParameter("flag_add");
String f_name = request.getParameter("f_name");
String l_name = request.getParameter("l_name");
String role_name = request.getParameter("role_id");
String email_id = request.getParameter("email_id");
String loging_id = request.getParameter("loging_id");
String u_password = request.getParameter("u_password");
int u_cnt = 0;
//check for the unique login _id 
try{
	statement=con.createStatement(); 
	sql= "select count(1) as u_cnt from BUSINESS_USERS WHERE USER_LOGIN_ID= '"+loging_id+"'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
   u_cnt=resultSet.getInt("u_cnt");
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
//out.println("u_cnt:"+u_cnt);

if (u_cnt > 0) 
{	
out.println("Login ID :<b>"+loging_id+"  </b>      :Already Exist please choose another !!!!!!");	
}	
	 

if (flag != null && flag.equals("add") && (u_cnt==0))
{
 statement=con.createStatement(); 
 sql="INSERT INTO BUSINESS_USERS(FIRST_NAME,LAST_NAME,ROLE_NAME,EMAIL_ID,USER_LOGIN_ID,USER_PWD) values ('"+f_name+"','"+l_name+"','"+role_name+"','"+email_id+"','"+loging_id+"','"+u_password+"')"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 out.println("Added Record Sccessfully !!!!!!");
 }	
%>
</form>
</font>
</body>
</html>