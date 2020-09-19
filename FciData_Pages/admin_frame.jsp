<!DOCTYPE html>
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
String username = request.getParameter("username");
String password = request.getParameter("password");	
String status_str ="disabled" ;
//out.println("username :"+username);
//out.println("password :"+password);
 %> 	
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<frameset cols="20%,80%">
   <frame src="admin_buttons.jsp?&username=<%=username%>" name="leftframe"/>
  <frameset cols="70%,30%"> 
   <frame src="User_List.jsp" name="rightmidframe"/>
   <frame src="User_add.jsp" name="rightframe"/>
</frameset>
</frameset>
</html>


