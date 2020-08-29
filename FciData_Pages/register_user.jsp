<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<html>
<head>
<script>
function f_validation()
{
	if (document.add_user.f_name.value=="") 
		{
		alert("Please add First Name of User !!!");
		return false;				
		}
	
	if (document.add_user.f_name.value=="") 
	{
	alert("Please add First Name of User !!!");
	return false;				
	}
	
	if (document.add_user.l_name.value=="") 
	{
	alert("Please add Last Name of User !!!");
	return false;				
	}
	
	if (document.add_user.user_login_id.value=="") 
	{
	alert("Please add Login User Id of User !!!");
	return false;				
	}
	if (document.add_user.u_password.value=="") 
	{
	alert("Please add Password of User !!!");
	return false;				
	}
	else
	{
	document.add_user.submit();	
	}
}
</script>
<title>Registration Form</title>
<style>
body {
  color: black;
  font-family: Calibri;
  font-size: 90%;
}
</style>
</head>
<body ALIGN="CENTER">
<h2 ALIGN="CENTER">Registration form</h2>
<form  name="add_user" action="LoadUser.jsp" method="post">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<table border="0" align="center" style="height: 300px;">
<tbody>
<tr>
<td><label for="id"> First Name: </label></td>
<td><input id="f_name" maxlength="50" name="f_name" type="text" /></td>
</tr>

<tr>
<td><label for="name">Last Name: </label></td>
<td><input id="last_name" maxlength="50" name="l_name" type="text" /></td>
</tr>


<tr>
<td><label for="email">Email Address:</label></td>
<td><input id="email" maxlength="50" name="email" type="text" /></td>
</tr>

<tr>
<td><label for="username">User Login Id:</label></td>
<td><input id="user_login_id" maxlength="50" name="user_login_id" type="text" /></td>
</tr>


<tr>
<td><label for="password">Password:</label></td>
<td><input id="password" maxlength="50" name="u_password" type="password" /></td>
</tr>

<tr>
<td><label for="password">Confirm Password:</label></td>
<td><input id="confirm_password" maxlength="50" name="c_password"
type="password" /></td>

</tr>

<tr>


</tr>

<tr>
<td align="right"><input name="button" type="button" value="Add User" onclick="f_validation()"></td>
<td align="right"><input name="reset_user" type="Reset" value="Reset User">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<input name="back" type="button" value="Back" onclick="window.history.back();">
</td>
</tr>
</tbody>
</table>
</form>
</body>
</html>