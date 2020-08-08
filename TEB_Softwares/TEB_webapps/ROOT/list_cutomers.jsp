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
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/tebsoftwares","sanjay","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 Statement statement1 = null; 
 ResultSet resultSet = null;
 ResultSet resultSet_1 = null;
 int record_count=0;
 int rec_key_count=0;
 %> 	
	
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Contact US</title>
<style>
body {      
  color: black;
  font-family: Calibri;
  font-size: 90%;
}
</style>
</head>
<body>
<table>
<tr><td> Customer Name </td> <td> Contact No  </td> <td> Email ID </td> <td> Comment </td> <td> Status </td> <td> Created on </td></tr>

try{
 statement=con.createStatement();
 String sql ="SELECT cust_name, phone_no, emailid, comment, status, created_on FROM contact_info WHERE 1";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %> 
 <tr>
 <td width="20%"> <%=resultSet.getString("cust_name")%> </td> 
 <td width="20%"> <%=resultSet.getString("phone_no")%> </td> 
 <td width="20%"> <%=resultSet.getString("emailid")%> </td> 
 <td width="20%"> <%=resultSet.getString("comment")%> </td> 
 <td width="20%"> <%=resultSet.getString("status")%> </td>  
 <td width="20%"> <%=resultSet.getString("created_on")%> </td>  
 </tr>

<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</table>
</body>
</html>