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
	
if (document.user_edit_form.f_name.value == "")
{
    alert("First Name must be filled out");
    return false;
 }
 else if(document.user_edit_form.l_name.value == "")
{
    alert("Last Name must be filled out");
    return false;
 }
else if(document.user_edit_form.role_id.value == "")
{
    alert("Please select Role.");
    return false;
 }	
else if(document.user_edit_form.email_id.value == "")
{
    alert("email_id must be filled out.");
    return false;
 }	
else if(document.user_edit_form.loging_id.value == "")
{
    alert("Login Id must be filled out.");
    return false;
 }	
else if(document.user_edit_form.u_password.value == "")
{
    alert("Password must be filled out.");
    return false;
 }		
else if(document.user_edit_form.re_u_password.value == "")
{
    alert("Retype Password must be filled out.");
    return false;
 }	
else if(document.user_edit_form.re_u_password.value != document.user_edit_form.u_password.value) 
{
    alert("Password and Retype Password must be same.");
    return false;
 }	 
else 
{
	document.user_edit_form.save_flag.value='Yes';	
	document.user_edit_form.action = "User_edit.jsp";
	document.user_edit_form.submit();
}		
}

</script>
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="user_edit_form">


<%
String user_id = request.getParameter("edit_radio");
String f_name = "";
String l_name = "";
String email_id = "";
String user_login_id = "";
String user_pwd = "";
String role_name = "";
String save_flag=request.getParameter("save_flag");

 user_id = request.getParameter("edit_radio");
//out.println("save_flag"+save_flag+" user_id "+user_id);
if (save_flag != null && save_flag.equals("Yes"))
{
 f_name = request.getParameter("f_name");
 l_name = request.getParameter("l_name");
 role_name = request.getParameter("role_id");
 email_id = request.getParameter("email_id");
 user_login_id = request.getParameter("loging_id");
 user_pwd = request.getParameter("u_password");
	
 statement=con.createStatement(); 
 sql="UPDATE BUSINESS_USERS SET FIRST_NAME='"+f_name+"',LAST_NAME='"+l_name+"',ROLE_NAME='"+role_name+"',EMAIL_ID='"+email_id+"',USER_LOGIN_ID='"+user_login_id+"',USER_PWD='"+user_pwd+"' WHERE USER_ID='"+user_id+"'"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 out.println("Saved sccessfully !!!!!!");
 }	
%>





<%

//out.println(" user_id "+user_id);

try{
  statement=con.createStatement();
  sql ="SELECT FIRST_NAME,LAST_NAME, ROLE_NAME,EMAIL_ID,USER_LOGIN_ID,USER_PWD FROM BUSINESS_USERS where USER_ID = '"+user_id+"'";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	f_name=resultSet.getString("FIRST_NAME");	
	l_name=resultSet.getString("LAST_NAME");
	email_id=resultSet.getString("EMAIL_ID");
	user_login_id=resultSet.getString("USER_LOGIN_ID");
	user_pwd=resultSet.getString("USER_PWD");
	role_name=resultSet.getString("ROLE_NAME");
 }
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }

%>
<h3>  EDIT USER </h3>  
<input type="hidden" name="edit_radio" value="<%=user_id%>"> 
<input type="hidden" name="save_flag" value=""> 
<table border=0  style="height:300px;">
<tr>
<td width="30%">First Name :</td>
<td width="70%"> <input type="text" name="f_name" value="<%=f_name%>"></td>
</tr>
<tr>
<td width="30%">Last Name :</td>
<td width="70%"><input type="text" name="l_name" value="<%=l_name%>"></td>
</tr>
<tr>
<td width="30%">Role :</td>
<td width="70%">
 <SELECT NAME="role_id" style="width: 150px;">
<option value="0">Select Role</option>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT ROLE_NAME FROM role_mst WHERE ROLE_NAME <> 'ADMIN'";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
if(!(resultSet.getString("ROLE_NAME").equals(role_name)))
{  
  out.println("<option value="+resultSet.getString("ROLE_NAME")+" > "+resultSet.getString("ROLE_NAME")+" </option>");
}
else
{
  out.println("<option value="+resultSet.getString("ROLE_NAME")+" selected > "+resultSet.getString("ROLE_NAME")+" </option>");
} 
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
<td width="70%"><input type="text" name="email_id" value="<%=email_id%>"></td>
</tr>
<tr>
<td width="30%">Login Id :</td>
<td width="70%"><input type="text" name="loging_id" value="<%=user_login_id%>"></td>
</tr>
<tr>
<td width="30%">Password :</td>
<td width="70%"><input type="password" name="u_password" value="<%=user_pwd%>"></td>
</tr>
<tr>
<td width="30%">Retype Password :</td>
<td width="70%"><input type="password" name="re_u_password" value="<%=user_pwd%>"></td>
</tr>
<tr>
<td width="20%">
</td>
<td width="70%">
<div class="btn-group">
  <button type="button" name="save_user_data" onclick="f_save()" >Save</button> <button type="reset">Reset</button> 
</div>  
</td>
</tr>
</table>

</form>
</font>
</body>
</html>