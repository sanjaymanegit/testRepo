<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
  
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Print Batch</title>
<style>
body {
  color: black;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 80%;
}
</style>

<script>
function goBack() {
    window.history.back();
}
function poponload()
{
    testwindow = window.open("BatchDetailsPrint.jsp", "mywindow", "location=1,status=1,scrollbars=1,width=1000,height=1000");
    testwindow.moveTo(800, 300);
}

</script>
</head>
<body>

<form action="BatchDetailsPrint.jsp">
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
int rec_key_count=0;	

String v_dev_id=null;
Connection connection = null;
Statement statement = null;
ResultSet resultSet = null;
v_dev_id=request.getParameter("device_id");
 %> 


<%
String BatchIdsArr[]= request.getParameterValues("chkbox_for_batch");
String BatchIDs="";
String v_batch_id="";
if(BatchIdsArr != null)
{
%>
<%
for(int i=0; i<BatchIdsArr.length; i++)
{
 BatchIDs=BatchIdsArr[i];
 try{ 
 statement=con.createStatement();
 String sql ="SELECT BATCH_ID,BATCH_DATE,RECV_WT_KG,RECV_BAGS_CNT,ACCPT_WT_KG,ACCPT_BAGS_CNT,MATERIAL_TYPE,WAGON_CNT FROM BATCH_MST WHERE BATCH_ID= '"+BatchIDs+"' LIMIT 1";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	 // v_batch_id =resultSet.getString("BATCH_ID") 
	 //out.println("<h>v_batch_id : "+v_batch_id+"</h>");
 %>
<table border="1">
<tr> <td>
<table border="0" align="left" style="width: 1000px;">
<tr > <td colspan=5>Batch Id     : <b> <%=resultSet.getString("BATCH_ID")%> </b> </td>
<td colspan=5> Batch Date        : <%=resultSet.getString("BATCH_DATE")%></td>
</tr>
<tr> <td colspan=5>Received Weight (Kg)     : <%=resultSet.getString("RECV_WT_KG")%></td>
<td colspan=5>Accepted Weight (Kg)         : <%=resultSet.getString("ACCPT_WT_KG")%>
</td>
</tr>
<tr> <td colspan=5>Received Bags     : <%=resultSet.getString("RECV_BAGS_CNT")%></td>
<td colspan=5>Accepted Bags         : <%=resultSet.getString("ACCPT_BAGS_CNT")%>
</td>
</tr>
<tr > <td colspan=5>Material         : <%=resultSet.getString("MATERIAL_TYPE")%>
</td>
<td colspan=5>Wagon Count           : <%=resultSet.getString("WAGON_CNT")%>
</td>
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }

%>
</table>
</td></tr>
<tr> <td>
<table border="0" align="left" style="width: 1000px;">
<tr bgcolor="#CFF7EC"><td> Truck.No.</td> <td> Vehicle No</td> <td> Net Weight Kg. </td>  <td> No. Of. Bags. </td>  <td> Tare Weight Kg. </td> <td> Gross Weight Kg. </td> <td> Slip No.</td></tr>
<%
try{ 
 statement=con.createStatement();
 String sql ="select CURR_TRUCK_CNT,VEHICLE_NO,NET_WEIGHT_VAL,ACCPTED_BAGS,CASE WHEN FIRST_WEIGHT_MODE='Tare' THEN FIRST_WEIGHT_VAL WHEN SECOND_WT_MODE='Tare' THEN SECOND_WT_VAL END as TARE_WT, CASE WHEN FIRST_WEIGHT_MODE='Gross' THEN FIRST_WEIGHT_VAL WHEN SECOND_WT_MODE='Gross' THEN SECOND_WT_VAL END  AS GROSS_WT , SERIAL_NO,CASE WHEN FIRST_WEIGHT_MODE='Gross' THEN FIRST_WT_CRTEATED_ON WHEN SECOND_WT_MODE='Gross' THEN SECOND_WT_CREATED_ON END as GROSS_WT_DATE,CASE WHEN FIRST_WEIGHT_MODE='Tare' THEN FIRST_WT_CRTEATED_ON WHEN SECOND_WT_MODE='Tare' THEN SECOND_WT_CREATED_ON END as TARE_WT_DATE FROM WEIGHT_MST WHERE BATCH_ID ='"+BatchIDs+"' order by CURR_TRUCK_CNT ASC";
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){   
 %>
 <tr> 
 <td><%=resultSet.getString("CURR_TRUCK_CNT") %></td> 
 <td><%=resultSet.getString("VEHICLE_NO") %></td>
 <td><%=resultSet.getString("NET_WEIGHT_VAL") %> </td>  
 <td><%=resultSet.getString("ACCPTED_BAGS") %> </td>  
 <td><%=resultSet.getString("TARE_WT") %> &nbsp; &nbsp;  [  <%=resultSet.getString("TARE_WT_DATE") %> ]  </td> 
 <td><%=resultSet.getString("GROSS_WT") %> &nbsp; &nbsp;  [  <%=resultSet.getString("GROSS_WT_DATE") %> ] </td> 
 <td><%=resultSet.getString("SERIAL_NO") %></td>
 </tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>


</table> </td>
</tr>
</table>
</td></tr>
<tr bgcolor="grey"> <td> <br> <br> </td>
</tr>
</table>
<%
} 
}
%>


</form>

</body>
</html>