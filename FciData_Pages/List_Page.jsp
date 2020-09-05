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
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fci","root","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 ResultSet resultSet = null;
 String sql =""; 
 %>   

<%
String user_name=request.getParameter("username");
String user_pass = request.getParameter("password");
//out.println("user_name:"+user_name);  
Integer u_cnt=0;
try{
  statement=con.createStatement();
  sql ="SELECT count(USER_ID) as U_COUNT FROM business_users WHERE USER_LOGIN_ID= '"+user_name+"' AND USER_PWD='"+user_pass+"'";  
  //out.println("sql:"+sql);
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	 u_cnt=resultSet.getInt("U_COUNT");
	 out.println("<frameset rows="+"12%,88%"+">");
     out.println("<frame src=header_page.jsp?&username="+user_name+"&password="+user_pass+" name=topframe />");
	 out.println("<frame src=batch_frame.jsp?&username="+user_name+" name=bottomframe />");
     out.println("</frameset></html>");            
     connection.close();
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }

if(u_cnt != 1)
{
out.println("<h2><b> Login Failed !!!!!!!! Please contact Administrator.</b></h2> </html>")	;	
}
%>
