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
if (document.role_edit_form.r_name.value == "")
{
    alert("Role Name must be filled out");
    return false;
 }
 else if(document.role_edit_form.r_desc.value == "")
{
    alert("Description must be filled out");
    return false;
 }
else 
{	//alert(document.role_edit_form.edit_radio.value);
	document.role_edit_form.flag_save.value='save';
	document.role_edit_form.action = "Role_edit.jsp";
	document.role_edit_form.submit();
}		
}

</script>

</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="role_edit_form" method="post">
<%
String r_id=request.getParameter("edit_radio");
String r_name ="" ;
String r_desc ="" ; 
//out.println("r_id:"+r_id);
try{	   
	statement=con.createStatement(); 
	sql= "select ROLE_NAME,COMMENT from ROLE_MST WHERE ROLE_id= '"+r_id+"'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    r_name = resultSet.getString("ROLE_NAME");
    r_desc = resultSet.getString("COMMENT");
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
%>

<h3>  Edit New Role </h3>   
<input type="hidden" value="x" name="flag_save">
<input type="hidden" name="edit_radio" value="<%=r_id%>">
<table border=0  style="height:150px;">
<tr>
<td width="30%">Role Name :</td>
<td width="70%"> <input type="text" name="r_name" value="<%=r_name%>"></td>
</tr>
<tr>
<td width="30%">Role Description :</td>
<td width="70%"><input type="text" name="r_desc" value="<%=r_desc%>"></td>
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
  <button type="submit" name="add_role" onclick="f_save()">Save</button> <button type="reset">Reset</button> 
</div>  
</td>
</tr>
</table>
<%
r_name = request.getParameter("r_name");
r_desc = request.getParameter("r_desc");
String flag = request.getParameter("flag_save");
//out.println("r_id:"+r_id);
if (flag != null && flag.equals("save"))
{
 statement=con.createStatement(); 
 sql="UPDATE ROLE_MST SET ROLE_NAME='"+r_name+"' ,COMMENT='"+r_desc+"' WHERE ROLE_id ='"+r_id+"'"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 out.println("Saved Record Sccessfully !!!!!!");
 }	
%>
</form>
</font>
</body>
</html>