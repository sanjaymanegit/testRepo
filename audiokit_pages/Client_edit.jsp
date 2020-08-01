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
if (document.client_edit_form.client_name.value == "")
{
    alert("Client Name must be filled out");
    return false;
 }
 else if(document.client_edit_form.client_desc.value == "")
{
    alert("Description must be filled out");
    return false;
 }
else 
{	//alert(document.client_edit_form.edit_radio.value);
	document.client_edit_form.flag_save.value='save';
	document.client_edit_form.action = "Client_edit.jsp";
	document.client_edit_form.submit();
}		
}

</script>

</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="client_edit_form" method="post">
<%
String client_id=request.getParameter("edit_radio");
String client_name ="" ;
String client_desc ="" ; 
//out.println("client_id:"+client_id);
try{	   
	statement=con.createStatement(); 
	sql= "select CLIENT_NAME,CLIENT_DESC from client_dtls WHERE client_id= '"+client_id+"'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    client_name = resultSet.getString("CLIENT_NAME");
    client_desc = resultSet.getString("CLIENT_DESC");
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
%>

<h3>  Edit New Client </h3>   
<input type="hidden" value="x" name="flag_save">
<input type="hidden" name="edit_radio" value="<%=client_id%>">
<table border=0  style="height:150px;">
<tr>
<td width="30%">Client Name :</td>
<td width="70%"> <input type="text" name="client_name" value="<%=client_name%>"></td>
</tr>
<tr>
<td width="30%">Client Description :</td>
<td width="70%"><input type="text" name="client_desc" value="<%=client_desc%>"></td>
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
  <button type="submit" name="edit_Client" onclick="f_save()">Save</button> <button type="reset">Reset</button> 
</div>  
</td>
</tr>
</table>
<%
client_name = request.getParameter("client_name");
client_desc = request.getParameter("client_desc");
String flag = request.getParameter("flag_save");
//out.println("r_id:"+r_id);
if (flag != null && flag.equals("save"))
{
 statement=con.createStatement(); 
 sql="UPDATE client_dtls SET CLIENT_NAME='"+client_name+"' ,client_desc='"+client_desc+"' WHERE client_id ='"+client_id+"'"; 
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