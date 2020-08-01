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

function users_onchange()
{
 //document.action_user_map_form.roles.selected.value=document.action_user_map_form.roles.value;
 //document.action_user_map_form.role_id.value=document.action_user_map_form.roles.selected.value;
 //alert(document.action_user_map_form.roles.value);
 document.action_user_map_form.action = "Action_user_map.jsp";
 document.action_user_map_form.submit();	
}

function f_save()
{
//alert('eretert !!!!');
action_user_map_form.flag_save.value="Yes";
action_user_map_form.action = "Action_user_map.jsp";
action_user_map_form.submit();			
}
</script>

</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="action_user_map_form" method="post">
<%
String flag_save = request.getParameter("flag_save");
String user_id = request.getParameter("users");
//out.println("flag_save : "+flag_save);
//out.println("role_id : "+role_id);
if (flag_save != null && flag_save.equals("Yes"))
{	
String action_keyArr[]= request.getParameterValues("action_key");
String action_keys="";
if(action_keyArr != null)
{	
 statement=con.createStatement(); 
 sql="UPDATE actions_user_map set status='disabled' where user_id='"+user_id+"'"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);		
	
for(int i=0; i<action_keyArr.length; i++)
{
	 action_keys=action_keyArr[i];
	 statement=con.createStatement(); 
     sql="UPDATE actions_user_map set status='enabled' where ACTION_USER_MAP_ID='"+action_keys+"'"; 
    //out.println("sql  :"+sql); 
     statement.executeUpdate(sql);	 
}	 
    out.println("Saved Successfully !!!!<br><br>");
}
}

%> 
<h3> USER ACTIONS MAPPING  </h3>  
<SELECT NAME="users" style="width: 250px;" onchange="users_onchange()">
<option value="" >All Users</option>
<%

 try{
  statement=con.createStatement();
  String sql_1 ="SELECT USER_ID,concat(FIRST_NAME,' ',LAST_NAME,' (',ROLE_NAME,' )') as USER_NAME FROM business_users where ROLE_NAME != 'ADMIN'";
  resultSet = statement.executeQuery(sql_1);
 while(resultSet.next()){
 if(!(resultSet.getString("USER_ID").equals(user_id)))
 {
  out.println("<option value="+resultSet.getString("USER_ID")+" >"+resultSet.getString("USER_NAME")+"</option>");
 }	 
 else
 {
  out.println("<option value="+resultSet.getString("USER_ID")+" selected>"+resultSet.getString("USER_NAME")+"</option>");
 }
 }
  connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</SELECT>
<input type="hidden" value="x" name="flag_save">
<input type="hidden" value="" name="action_key">
<input type="hidden" value="" name="user_id">
<BR> <br>

<h3> All Actions are below  </h3>

<table border="0"  style="height:250px;">
<tr bgcolor="grey">
<td width="30%">Action Key  </td>
<td width="30%">Action Name`</td>
<td width="40%">Action Desc </td>
</tr>
<%
out.println("<input type=hidden value="+user_id+" name=user_id>");
if (user_id != null)
{
 try{
  statement=con.createStatement();
  sql ="SELECT ACTION_USER_MAP_ID,CASE WHEN A.STATUS = 'enabled' THEN 'checked' else null END as STATUS, B.ACTION_ID,B.ACTION_KEY, B.ACTION_NAME,B.ACTION_DESC FROM actions_user_map A, ACTION_MST B WHERE A.ACTION_KEY=B.ACTION_KEY AND A.USER_ID = '"+user_id+"'";
  //out.println("sql :"+sql);
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
 <tr>
<td width="30%"><input type="checkbox" name="action_key" value="<%=resultSet.getString("ACTION_USER_MAP_ID")%>" <%=resultSet.getString("STATUS")%>> <%=resultSet.getString("ACTION_KEY")%></td>
<td width="30%"><%=resultSet.getString("ACTION_NAME")%></td>
<td width="40%"><%=resultSet.getString("ACTION_DESC")%></td>
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
}
else 
{
	
out.println("<tr colspan=3><td> No Records Found.</td></tr>");	
}
%>
<tr>
<td width="30%"><br></td>
<td width="30%"><br></td>
<td width="40%"><br></td>
</tr>
<tr>
<td width="40%"> 
<div class="btn-group">
  <button type="submit" name="add_role" onclick="f_save()">Save</button> <button type="reset">Reset</button> 
</div>  
</td>
<td width="30%"> </td>
<td width="30%"> 

</td>
</tr>
</table>

</form>
</font>
</body>
</html>