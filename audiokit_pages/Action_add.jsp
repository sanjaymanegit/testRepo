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
  padding: 5px 20px; /* Some padding */
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

if (document.action_add_form.action_key.value == "")
{
    alert("Action Key must be filled out");
    return false;
 }
 else if(document.action_add_form.action_name.value == "")
{
    alert("Action Name must be filled out");
    return false;
 }
 else if(document.action_add_form.action_desc.value == "")
{
    alert("Description must be filled out");
    return false;
 }
else 
{	
	document.action_add_form.flag_add.value='add';
	document.action_add_form.action = "Action_add.jsp";
	document.action_add_form.submit();
}		
}

</script>

</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="action_add_form" method="post">
<h3>  ADD New Action </h3>   ( Note: All fields are mandatory)
<input type="hidden" value="x" name="flag_add">
<table border="0"  style="height:150px;">
<tr>
<td width="30%">Action Key  :</td>
<td width="70%"> <input type="text" name="action_key"></td>
</tr>
<tr>
<td width="30%">Action Name  :</td>
<td width="70%"><input type="text" name="action_name"></td>
</tr>
<tr>
<td width="30%"> Description  :</td>
<td width="70%"><input type="text" name="action_desc"></td>
</tr>
<tr><td width="30%"></td>
<td width="70%"><div class="btn-group">
  <button type="button" name="add_action" onclick="f_add()">Add</button> <button type="reset">Reset</button> 
</div></td>
</tr>
</table>
<%
String flag=request.getParameter("flag_add");
if (flag != null && flag.equals("add"))
{
String action_key = request.getParameter("action_key");
String action_name = request.getParameter("action_name");
String action_desc = request.getParameter("action_desc");
int u_cnt = 0;
try{
	statement=con.createStatement(); 
	sql= "select count(1) as u_cnt from ACTION_MST WHERE ACTION_KEY= '"+action_key+"'";
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
out.println("Action key :<b>"+action_key+"  </b>      :Already Exist please choose another !!!!!!");	
}	
	 

if (flag != null && flag.equals("add") && (u_cnt==0))
{
 statement=con.createStatement(); 
 sql="INSERT INTO ACTION_MST(ACTION_KEY,ACTION_NAME,ACTION_DESC) values ('"+action_key+"','"+action_name+"','"+action_desc+"')"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 out.println("Added Record Sccessfully !!!!!!");
 }	
}
%>
</form>
</font>
</body>
</html>