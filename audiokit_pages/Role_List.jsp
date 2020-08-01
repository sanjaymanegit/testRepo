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
document.role_list_form.target = "bottomframe2";
document.role_list_form.action="Role_add.jsp";
document.role_list_form.submit();
}

function f2()
{	
//alert(document.role_list_form.radio_edit.value);
//alert('hiffff');
document.role_list_form.target = "bottomframe2";
document.role_list_form.action="Role_edit.jsp";
document.role_list_form.submit();}

function f3()
{	
var input_flag = confirm(" Confirm the Role which is going to delete : "+document.role_list_form.elements['edit_radio'].value);
	if(input_flag == true)
	{
		document.role_list_form.del_flag.value="Yes";
		document.role_list_form.target = "bottomframe";
		document.role_list_form.action="Role_List.jsp";
		document.role_list_form.submit();
	}
}	

</script>
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="role_list_form">
<input type="hidden" name="del_flag" value="">
<input type="hidden" name="role_name" value="">
<%
String del_flag=request.getParameter("del_flag");
String role_id = request.getParameter("edit_radio");
//out.println("del_flag"+del_flag+" role_id: "+role_id);
if (del_flag != null && del_flag.equals("Yes"))
{
 statement=con.createStatement(); 
 sql="DELETE FROM ROLE_MST WHERE ROLE_ID='"+role_id+"'"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 //out.println("User deleted sccessfully !!!!!!");
 }	
%>
<h3>  ROLES </h3>   
<div class="btn-group">
  <button type="button" onclick="f1()"> Add Role</button> 
  <button type="button" onclick="f2()">Edit Role</button>  
  <button type="button" onclick="f3()">Delete Role</button>  
</div>  
  <br> 
<table border=0 >
<tr bgcolor="grey" >
<td width="10%">Role Name</td>
<td width="20%">Description</td>
</tr>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT ROLE_ID,ROLE_NAME,COMMENT FROM role_mst";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
<td><input type="radio" name="edit_radio" value="<%=resultSet.getString("ROLE_ID")%>"><%=resultSet.getString("ROLE_NAME")%></td>
<td><%=resultSet.getString("COMMENT")%></td>
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