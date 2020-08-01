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

if (document.client_add_form.client_name.value == "")
{
    alert("Client Name must be filled out");
    return false;
 }
 else if(document.client_add_form.client_desc.value == "")
{
    alert("Description must be filled out");
    return false;
 }
else 
{	
	document.client_add_form.flag_add.value='add';
	document.client_add_form.action = "Client_add.jsp";
	document.client_add_form.submit();
}		
}

</script>

</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="client_add_form" method="post">
<h3>  ADD New Client </h3>   ( Note: All fields are mandatory)
<input type="hidden" value="x" name="flag_add">
<table border=0  style="height:150px;">
<tr>
<td width="30%">Clent Name :</td>
<td width="70%"> <input type="text" name="client_name"></td>
</tr>
<tr>
<td width="30%">Client Description :</td>
<td width="70%"><input type="text" name="client_desc"></td>
</tr>
<tr>
<td width="20%">
</td>
<td width="70%">
</td>
</tr>
<tr>
<td width="20%">
</td>
<td width="70%">
<div class="btn-group">
  <button type="button" name="add_client" onclick="f_add()">Add</button> <button type="reset">Reset</button> 
</div>  
</td>
</tr>
</table>
<%
String flag=request.getParameter("flag_add");
String client_name = request.getParameter("client_name");
String client_desc = request.getParameter("client_desc");

int u_cnt = 0;
//check for the unique login _id 
try{
	statement=con.createStatement(); 
	sql= "select count(1) as u_cnt from client_dtls WHERE ROLE_NAME= '"+client_name+"'";
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
out.println("Role Name :<b>"+client_name+"  </b>      :Already Exist please choose another !!!!!!");	
}	
	 

if (flag != null && flag.equals("add") && (u_cnt==0))
{
 statement=con.createStatement(); 
 sql="INSERT INTO client_dtls(client_name ,client_desc) values ('"+client_name+"','"+client_desc+"')"; 
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