<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>

<%
String first_name=request.getParameter("f_name");
String last_name=request.getParameter("l_name");
String u_email=request.getParameter("email");
String user_login_id=request.getParameter("user_login_id");
String u_pwd=request.getParameter("u_password");
String c_pwd=request.getParameter("c_password");
try
{
Class.forName("com.mysql.jdbc.Driver");
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db", "root", "31@dec2019");
Statement st=conn.createStatement();
int i=st.executeUpdate("insert into BUSINESS_USERS(FIRST_NAME,LAST_NAME,EMAIL_ID,USER_LOGIN_ID,USER_PWD)values('"+first_name+"','"+last_name+"','"+u_email+"','"+user_login_id+"','"+u_pwd+"')");
out.println("Data is successfully inserted!");
}
catch(Exception e)
{
System.out.print(e);
e.printStackTrace();
}
%>