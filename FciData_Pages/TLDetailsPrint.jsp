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
String v_received_wt=null;

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
 String sql ="SELECT STATUS,BATCH_ID_DISPLAY, BATCH_ID,DATE(BATCH_DATE) as dt,FORMAT(RECV_WT_KG,3) as RECV_WT_KG,FORMAT(ACCPT_WT_KG,3) as ACCPT_WT_KG, FORMAT(TL_ACCPTED,3) as TL_ACCPTED  FROM BATCH_MST WHERE BATCH_ID= '"+BatchIDs+"' LIMIT 1";
 //out.println("sql : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	   //v_received_wt =resultSet.getString("RECV_WT_KG") 
	  //out.println("<h>RECV_WT_KG : "+v_received_wt+"</h>");
 %>

<table border="0" >
<tr > <td style="width:300px;"></td><td style="width:300px;"></td></tr>
<tr > <td></td><td></td></tr>
<tr > <td>Recipt. Id     :  <b> <%=resultSet.getString("BATCH_ID_DISPLAY")%> </b></td><td  >Status :<%=resultSet.getString("STATUS")%> </td></tr>
<tr > <td></td><td></td></tr>
<tr > <td></td><td></td></tr>
</table>
<table border="1">
<tr> <td>
<table>
<tr bgcolor="#CFF7EC"> <td style="width: 300px;" > Description </td><td style="width:100px;" > Weight in Ton</td><td style="width: 500px;" > Lost Weight in Ton </td>
</tr>
<tr> <td >Accepted Weight (Ton)     :</td><td align="left"> <%=resultSet.getString("ACCPT_WT_KG")%></td><td > </td>
</tr>
<tr> <td >Received Weight (Ton)    : </td><td ><%=resultSet.getString("RECV_WT_KG")%></td><td > </td>
</tr>
<tr > <td > <b>Accepted TL (Ton) [A] </b>        :</td><td > </td><td ><b> <%=resultSet.getString("TL_ACCPTED")%></b> </td>
</tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> Received Weight (Ton) :  </td><td >  <%=resultSet.getString("RECV_WT_KG")%></td><td > </td></tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }

%>
<%
try{ 
 statement=con.createStatement();
 String sql ="SELECT FORMAT(SUM(NET_WEIGHT_VAL),3) as NET_WEIGHT_VAL  FROM WEIGHT_MST WHERE ISSUE_ID=0 AND BATCH_ID ='"+BatchIDs+"' ";
//io.println("sql : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	   //v_received_wt =resultSet.getString("RECV_WT_KG") 
	  //out.println("<h>RECV_WT_KG : "+v_received_wt+"</h>");
 %>
<tr > <td> Dispatched Weight (Ton) :  </td><td > <%=resultSet.getString("NET_WEIGHT_VAL")%> </td><td > </td></tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td ><b>Dispatched Loss (Ton) [B] </b>        :</td><td >  </td><td ><b>345.977 </b> </td>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> Dispatched Weight (Ton) :  </td><td >  865.566</td><td > </td></tr>
<%
try{ 
 statement=con.createStatement();
 String sql ="SELECT FORMAT(SUM(NET_WEIGHT_VAL),3) as NET_WEIGHT_VAL  FROM WEIGHT_MST WHERE ISSUE_ID=0 AND BATCH_ID ='"+BatchIDs+"' ";
//out.println("sql : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	   //v_received_wt =resultSet.getString("RECV_WT_KG") 
	   //out.println("<h>RECV_WT_KG : "+v_received_wt+"</h>");
%>
<tr > <td> Arrived Weight (Ton) :  </td><td > <%=resultSet.getString("NET_WEIGHT_VAL")%> </td><td > </td></tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td ><b>Transportation Loss (Ton) [C] </b>        :</td><td >  </td><td ><b>11.213  </b></td>

<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td ><b>Storage Loss (Ton) [D] </b>        :</td><td >  </td><td ><b>32.213 </b> </td>

<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td> </td><td >  </td><td > </td></tr>
<tr > <td ><b>Net Loss (Ton) [A+B+C+D] </b>        :</td><td >  </td><td ><b> 50.213  </b> </td>
</table>
</td>
</tr>
</table>
<%
} 
}
%>


</form>

</body>
</html>