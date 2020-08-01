<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
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
 ResultSet resultSet_edit = null; 
 %>    
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
<script>
function f1(var_in)
{	

if (var_in == 'users')	
{
document.reportInput.target = 'bottomframe';	
document.reportInput.action="User_List.jsp";
document.reportInput.submit();
document.reportInput.target = 'bottomframe2';
document.reportInput.action="User_add.jsp";
document.reportInput.submit();

}
else if(var_in == 'roles')
{
document.reportInput.target = 'bottomframe';
document.reportInput.action="Role_List.jsp";
document.reportInput.submit();
document.reportInput.target = 'bottomframe2';
document.reportInput.action="Role_add.jsp";
document.reportInput.submit();
}
else if(var_in == 'actions')
{
document.reportInput.target = 'bottomframe';
document.reportInput.action="Actions_List.jsp";
document.reportInput.submit();
document.reportInput.target = 'bottomframe2';
document.reportInput.action="Action_add.jsp";
document.reportInput.submit();
}
else if(var_in == 'clients')
{
document.reportInput.target = 'bottomframe';
document.reportInput.action="Client_List.jsp";
document.reportInput.submit();
document.reportInput.target = 'bottomframe2';
document.reportInput.action="Client_add.jsp";
document.reportInput.submit();
}
else
{
	alert(' Not valid input')
	return false;
}
document.reportInput.submit();
}



</script>
<style>
body {
  color: black;
  font-family: Calibri;
  font-size: 90%;
}

.btn-group button {
  background-color: grey ; /* Green background #4CAF50*/
  border: 1px solid green; /* Green border */
  color: white; /* White text */
  padding: 10px 60px; /* Some padding */
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
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"' >
<form action="" name="reportInput" >
<h3> Admin Tasks </h3>
<table border="0" width='100%'>
<tr>
<td align='center'>
<div class="btn-group">
  <button type="button" onclick="f1('users')" style="width:100%">  USERS  </button>   
</div>
</td>
</tr>
<tr>
<td>
<div class="btn-group">
  <button type="button" onclick="f1('roles')" style="width:100%">  ROELS  </button>   
</div>  
</td>
</tr>
<tr>
<td>
<div class="btn-group">
  <button type="button" onclick="f1('actions')" style="width:100%">ACTIONS</button> 
</div>  
</td>
</tr>
<tr>
<td>
<div class="btn-group">
  <button type="button" onclick="f1('clients')" style="width:100%">CLIENTS</button> 
</div>  
</td>
</tr>
 </table> 
  </form>
  </font>
</body>
</html>