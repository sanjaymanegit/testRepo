<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
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

<%
String user_name=request.getParameter("username");
String user_pass = request.getParameter("pass");
Integer u_cnt=0;
try{
  statement=con.createStatement();
  sql ="SELECT count(USER_ID) as U_COUNT FROM business_users WHERE USER_LOGIN_ID= '"+user_name+"' AND USER_PWD='"+user_pass+"'";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	 u_cnt=resultSet.getInt("U_COUNT");
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }

if(u_cnt== 1)
{
	
%>
<frameset rows="12%,88%">
   <frame src="header_page.jsp?user_login_id=<%=user_name%>" name="leftframe"/>
   <frame src="active_inactive_page.html?user_login_id=<%=user_name%>" name="rightframe"/>
</frameset>
</html>
<%	
}	
else 
{
out.println("<h2><b> Login Failed !!!!!!!! Please contact Administrator.</b></h2> </html>")	;	
}
%>
