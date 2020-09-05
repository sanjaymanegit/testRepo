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
function f1()
{	
document.user_list_form.target = "bottomframe2";
document.user_list_form.action="User_add.jsp";
document.user_list_form.submit();
}

function f2()
{	
document.user_list_form.target = "bottomframe2";
document.user_list_form.action="User_edit.jsp";
document.user_list_form.submit();}

function f3()
{	
var input_flag = confirm(" Confirm the User which is going to delete : "+document.user_list_form.elements['edit_radio'].value);
	if(input_flag == true)
	{
		document.user_list_form.del_flag.value="Yes";
		document.user_list_form.target = "bottomframe";
		document.user_list_form.action="User_List.jsp";
		document.user_list_form.submit();
	}
}	

</script>
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="user_list_form">
<input type="hidden" name="del_flag" value="">
<input type="hidden" name="user_id" value="">
<%
String del_flag=request.getParameter("del_flag");
String user_id = request.getParameter("edit_radio");
//out.println("del_flag"+del_flag+" user_id "+user_id);
if (del_flag != null && del_flag.equals("Yes"))
{
 statement=con.createStatement(); 
 sql="DELETE FROM BUSINESS_USERS WHERE USER_ID='"+user_id+"'"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 //out.println("User deleted sccessfully !!!!!!");
 }	
%>
<h3> USERS </h3>   
<div class="btn-group">
  <button type="button" onclick="f1()"> Add User</button> 
  <button type="button" onclick="f2()">Edit</button>  
  <button type="button" onclick="f3()">Delete</button>  
</div>  
  <br> 
<table border=0 >
<tr bgcolor="grey" >
<td width="10%">User ID</td>
<td width="20%">Login ID</td>
<td width="20%">User Name</td>
<td width="20%">Role</td>
<td width="20%">Email Id</td>
</tr>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT USER_ID, USER_LOGIN_ID,CONCAT(FIRST_NAME,' ',LAST_NAME) as USER_NAME , ROLE_NAME,EMAIL_ID FROM business_users WHERE ROLE_NAME <> 'ADMIN'";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
<td><input type="radio" name="edit_radio" value="<%=resultSet.getString("USER_ID")%>"><%=resultSet.getString("USER_ID")%></td>
<td><%=resultSet.getString("USER_LOGIN_ID")%></td>
<td><%=resultSet.getString("USER_NAME")%></td>
<td><%=resultSet.getString("ROLE_NAME")%></td>
<td><%=resultSet.getString("EMAIL_ID")%></td>
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</table>


</form>
</font>
</body>
</html>