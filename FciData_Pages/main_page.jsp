<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>

  
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Users Report List</title>
</head>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import ="java.sql.*" %>
<%@page import ="javax.sql.*" %>

<% 
try {
	      String username = request.getParameter("username");
          String password = request.getParameter("password");
		  int record_count=0;
            String connectionURL = "jdbc:mysql://localhost:3306/fci";
            Connection connection = null; 
            Class.forName("com.mysql.jdbc.Driver").newInstance(); 
            connection = DriverManager.getConnection(connectionURL, "root", "31@dec2019");                       
            PreparedStatement theStatement = null;
            theStatement = connection.prepareStatement("SELECT USER_LOGIN_ID, USER_PWD, ROLE_NAME FROM business_users where USER_LOGIN_ID=? and USER_PWD=?");
            theStatement.setString(1,request.getParameter("username"));
            theStatement.setString(2,request.getParameter("password"));
            ResultSet theResult = theStatement.executeQuery();
           
            while(theResult.next()){
                //out.println("Success");  
             //String rolename=theResult.getString("ROLE_NAME");
			    record_count=record_count+1;
             
			    out.println("<frameset rows="+"12%,88%"+">");
                out.println("<frame src="+"header_page.jsp?&username="+username+"&password="+password+" name=\"Topframe\"/>");
				out.println("<frameset cols="+"25%,75%"+">");	
                out.println("<frame src="+"BatchReportsInputPage.jsp?&username="+username+"&role_name="+theResult.getString("ROLE_NAME")+" name=\"leftbottomframe\"/>");
                out.println("<frame src="+"batch_list.jsp"+" name=\"rightbottomframe\"/>");
				out.println("</frameset>");           
                out.println("</frameset></html>");            
                connection.close();
            }
			
			if(record_count <= 0)
			 out.println("<h2>  Login Failed !!!!</h2>");	
			
			
             }catch(Exception ex){
            out.println("Unable to connect to database"+ex);
           }   
%>  

