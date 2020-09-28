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
 String sql ="SELECT MATERIAL,   FORMAT(SUM(BAL_BAGS),0) as BAL_BAGS,FORMAT(SUM(BAL_NET_WT),3) as BAL_NET_WT ,MAX(R_DATE) as R_DATE FROM slots_mst where MATERIAL= '"+BatchIDs+"' LIMIT 1";
 //out.println("sql : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
	   //v_received_wt =resultSet.getString("RECV_WT_KG") 
	  //out.println("<h>RECV_WT_KG : "+v_received_wt+"</h>");
 %>
<table border="1" >
<tr><td>
<table border="0" >
<tr > <td style="width:300px;"></td><td style="width:300px;"></td></tr>
<tr > <td></td><td></td></tr>
<tr > <td>Material Name    :  <b> <%=resultSet.getString("MATERIAL")%> </b></td><td  >No.Of.Bags : <%=resultSet.getString("BAL_BAGS")%> </td></tr>
<tr > <td>Updated On    : <%=resultSet.getString("R_DATE")%> </td><td  > Total Net.Weight Ton : <%=resultSet.getString("BAL_NET_WT")%></td></tr>
<tr > <td></td><td></td></tr>
<tr > <td></td><td></td></tr>
</table>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<table border="0">
<tr bgcolor="#CFF7EC" > <td style="width: 30px;"> Stack No </td>
<td style="width:150px;"> Recipt Date.</td>
<td> Recipt Weight<br>(Ton)</td>
<td> Recipt Bags.</td>
<td style="width:150px;"> Issued Date</td>
<td> Issued Weight <br>(Ton)</td>
<td> Issued Bags.</td>
<td> Balanced Bags.</td>
<td> Balanced Weight(Ton).</td>
<td> Loss (Ton) .</td>
<td> Lost Bags.</td>
<td> Lost Avg.Bag Wt <br>(Kg).</td>
<td> Loss (%)</td>
<td> Status</td>
</tr>
<%
try{ 
 statement=con.createStatement();
 String sql ="select  SLOT_NO,R_DATE,FORMAT(R_NET_WT,3) as R_NET_WT,FORMAT(R_BAGS,0) as R_BAGS,I_DATE,FORMAT(I_NET_WT,3) as I_NET_WT,FORMAT(I_BAGS,0) as I_BAGS ,FORMAT(BAL_BAGS,0) as BAL_BAGS,FORMAT(BAL_NET_WT,3) as BAL_NET_WT,FORMAT(LOSS_NET_WT,3) as LOSS_NET_WT,FORMAT(LOSS_BAGS,0) as LOSS_BAGS ,FORMAT(LOSS_AVG_BAG_WT,3) as LOSS_AVG_BAG_WT, FORMAT(LOSS_PERC,0) as LOSS_PERC,STATUS FROM slots_mst where MATERIAL= '"+BatchIDs+"'";
  //out.println("sql : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){   
 %>
<tr > <td>  <%=resultSet.getString("SLOT_NO")%> </td>
<td ><%=resultSet.getString("R_DATE")%></td>
<td> <%=resultSet.getString("R_NET_WT")%></td> 
<td> <%=resultSet.getString("R_BAGS")%></td> 
<td><%=resultSet.getString("I_DATE")%> </td> 
<td><%=resultSet.getString("I_NET_WT")%></td>
<td><%=resultSet.getString("I_BAGS")%></td> 
<td><%=resultSet.getString("BAL_BAGS")%></td> 
<td><%=resultSet.getString("BAL_NET_WT")%></td> 
<td><%=resultSet.getString("LOSS_NET_WT")%></td> 
<td><%=resultSet.getString("LOSS_BAGS")%></td>  
<td><%=resultSet.getString("LOSS_AVG_BAG_WT")%></td>   
<td><%=resultSet.getString("LOSS_PERC")%></td> 
<td><%=resultSet.getString("STATUS")%></td> </tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>

</table>
</td></tr>
</table>
<br><br>
<%
}
}
%>
</form>

</body>
</html>