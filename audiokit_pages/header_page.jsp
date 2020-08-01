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
 String sql = "";
 %> 
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
<style>
body {  
    background-color: Gainsboro;
  color: black;
  font-family: Calibri;
  font-size: 90%;
}
</style>

<script>
function f_active_inactive()
{
document.header_form.target = "rightframe";
document.header_form.action="active_inactive_page.html";
document.header_form.submit();
}

function f_setup()
{
document.header_form.target = "rightframe";
document.header_form.action="setup_frames_page.html";
document.header_form.submit();
}

function f_admin()
{
document.header_form.target = "rightframe";
document.header_form.action="admin_frame.html";
document.header_form.submit();
}

function f_ch_password()
{
document.header_form.target = "rightframe";
document.header_form.action="change_password.jsp";
document.header_form.submit();
}

</script>


</head>
<body>
<form name="header_form">

<table border="0" width="1800">
<tr> <td width="20%">
<marquee><h1> Online data is available. <h1></marquee> 
<!--<img src="health_check.png" alt="" width="320" height="100">-->
</td>
 <td width="55%" >   
 <table border="0">
 <tr> 
 <%
String user_login_id=request.getParameter("user_login_id");
//out.println(" user_login_id: "+user_login_id);
String user_id="";
try{	   
	statement=con.createStatement(); 
	sql= "SELECT user_id from business_users WHERE user_login_id ='"+user_login_id+"'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    user_id= resultSet.getString("user_id");    
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
//out.println(" user_id: "+user_id);
String status_str ="disabled" ;
%>

<%
try{	   
	statement=con.createStatement(); 
	sql= "SELECT status  as  STATUS_STR FROM ACTIONS_USER_MAP WHERE USER_ID ='"+user_id+"' and ACTION_KEY='ONLINE_OFFLINE_LIST'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    status_str = resultSet.getString("STATUS_STR");    
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
 //out.println(" status_str: "+status_str);
%>
   <td>  <input type="button" name="active_inactive_List" value="Online/Offline List"  onclick="f_active_inactive()" <%=status_str%>>  </td>
   
<%
 status_str ="disabled" ;
try{	   
	statement=con.createStatement(); 
	sql= "SELECT status  as  STATUS_STR FROM ACTIONS_USER_MAP WHERE USER_ID ='"+user_id+"' and ACTION_KEY='SETUP_DEVICE'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    status_str = resultSet.getString("STATUS_STR");    
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
 //out.println(" status_str: "+status_str);
%>
   
   <td>  <input type="button"    name="setup_button" value="Setup Device"  onclick="f_setup()" <%=status_str%>>  </td> 
 
<%
  status_str ="disabled" ;
try{	   
	statement=con.createStatement(); 
	sql= "SELECT status  as  STATUS_STR FROM ACTIONS_USER_MAP WHERE USER_ID ='"+user_id+"' and ACTION_KEY='ADMIN'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    status_str = resultSet.getString("STATUS_STR");    
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
 //out.println(" status_str: "+status_str);
%>
  
   <td>  <input type="button" name="admin_button" value="Admin"  onclick="f_admin()" <%=status_str%> ></td>
   
<%
 status_str ="disabled11" ;
try{	   
	statement=con.createStatement(); 
	sql= "SELECT status  as  STATUS_STR FROM ACTIONS_USER_MAP WHERE USER_ID ='"+user_id+"' and ACTION_KEY='REPORTS'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    status_str = resultSet.getString("STATUS_STR");    
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
 //out.println(" status_str: "+status_str);
%>
   <td>  <input type="button" name="report_button" value="Reports"  onclick="f_report()" <%=status_str%>></td>

<%
 status_str ="disabled" ;
try{	   
	statement=con.createStatement(); 
	sql= "SELECT status  as  STATUS_STR FROM ACTIONS_USER_MAP WHERE USER_ID ='"+user_id+"' and ACTION_KEY='MONITOR'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    status_str = resultSet.getString("STATUS_STR");    
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
 //out.println(" status_str: "+status_str);
%>
  
   <td>  <input type="button" name="Monitor_button" value="Monitor"  onclick="f_active_inactive()" <%=status_str%>></td>

<%
 status_str ="disabled" ;
try{	   
	statement=con.createStatement(); 
	sql= "SELECT status  as  STATUS_STR FROM ACTIONS_USER_MAP WHERE USER_ID ='"+user_id+"' and ACTION_KEY='BULK_UPLOAD'";
    resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
    status_str = resultSet.getString("STATUS_STR");    
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }	 
 //out.println(" status_str: "+status_str);
%>
   
   <td>  <input type="button" name="Monitor_button" value="Bulk Data Upload"  onclick="" <%=status_str%>></td>


   <td>  <input type="button" name="Monitor_button" value="Change Password"  onclick="f_ch_password()" ></td>
 </tr>  
 </table>
 </td>
 <td width="25%" > 
 <table border="0" align="left">
<% 

try {	
statement=con.createStatement();  
 sql="SELECT FIRST_NAME, LAST_NAME,ROLE_NAME,EMAIL_ID FROM business_users where USER_LOGIN_ID='"+user_login_id+"'";
resultSet=statement.executeQuery(sql);
while(resultSet.next())
{				
 %>
<tr><td>Login By:</td><td><%=resultSet.getString("FIRST_NAME")%> <%=resultSet.getString("LAST_NAME")%></td></tr>
<tr><td>Role    :</td><td><%=resultSet.getString("ROLE_NAME")%></td></tr>
<tr><td>Email:</td><td><%=resultSet.getString("EMAIL_ID")%></td></tr>
 <%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<input type="hidden" name="user_login_id" value="<%=user_login_id%>">
<tr><td><a href="index.html" target="_top"> Sign Out </a></td><td></td></tr>
 </table>
 </td>
 </tr>
 </table> 
 </form>
</body>
</html>