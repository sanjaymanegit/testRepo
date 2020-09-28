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
 String sql ="SELECT STATUS,BATCH_ID_DISPLAY FROM BATCH_MST WHERE BATCH_ID= '"+BatchIDs+"' LIMIT 1";
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
 String sql ="SELECT ID,    RECIPT_ID,    RAIL_RECIPT_WT,    RAIL_RECIPT_BAGS,    RAIL_RECIPT_AVG_BAG_WT,    DECLAIRED_WT, DECLAIRED_BAGS, DECLAIRED_AVG_BAG_WT,   ACCPT_WT,   ACCPT_BAGS,   ACCPT_AVG_BAG_WT,   ACCPT_LOSS_WT,   ACCPT_LOSS_BAGS,   ACCPT_LOSS_AVG_BAG_WT,   STORAGE_WT,   STORAGE_BAGS,   STORAGE_AVG_BAG_WT,   TRANSIT_LOSS_WT,   TRANSIT_LOSS_BAGS,   TRANSIT_LOSS_AVG_BAG_WT,   BOOKED_DEPO_LOSS_WT,   BOOKED_DEPO_LOSS_BAGS,   BOOKED_DEPO_AVG_BAGS_WT,   TOTAL_NET_LOSS_WT, TOTAL_NET_LOSS_BAGS,   TOTAL_NET_LOSS_AVG_BAG_WT FROM transit_loss_report";
 //out.println("sql : "+sql);
 resultSet = statement.executeQuery(sql);
 while(resultSet.next()){   
 %>
<table border="0">
<tr bgcolor="#CFF7EC"> <td style="width: 400px;" > Description </td><td style="width:300px;" > Net.Weight Ton</td><td style="width:150px;" > No.Of.Bags</td><td style="width:150px;" >Avg.Bag.Wt.(Kg)</td></tr>
<tr> <td style="width: 400px;" > Rail Recipt Weight  </td><td style="width:50px;" > <%=resultSet.getString("RAIL_RECIPT_WT")%></td><td style="width:150px;" ><%=resultSet.getString("RAIL_RECIPT_BAGS")%></td><td style="width:150px;" ><%=resultSet.getString("RAIL_RECIPT_AVG_BAG_WT")%></td></tr>
<tr> <td style="width: 400px;" > Declaired Weight  </td><td style="width:50px;" > <%=resultSet.getString("DECLAIRED_WT")%></td><td style="width:150px;" ><%=resultSet.getString("DECLAIRED_BAGS")%></td><td style="width:150px;" ><%=resultSet.getString("DECLAIRED_AVG_BAG_WT")%></td></tr>
<tr> <td style="width: 400px;" >Accepted Weight  </td><td style="width:50px;" > <%=resultSet.getString("ACCPT_WT")%></td><td style="width:150px;" ><%=resultSet.getString("ACCPT_BAGS")%></td><td style="width:150px;" ><%=resultSet.getString("ACCPT_AVG_BAG_WT")%></td></tr>
<tr> <td style="width: 400px;" > <b> Accepted Loss [ A ] </b>  </td><td style="width:50px;" ><b> <%=resultSet.getString("ACCPT_LOSS_WT")%> </b></td><td style="width:150px;" ><b><%=resultSet.getString("ACCPT_LOSS_BAGS")%></b></td><td style="width:150px;" ><b><%=resultSet.getString("ACCPT_LOSS_AVG_BAG_WT")%></b></td></tr>

<tr> <td style="width: 400px;" >Dispatched Weight  </td><td style="width:50px;" > <%=resultSet.getString("ACCPT_WT")%></td><td style="width:150px;" ><%=resultSet.getString("ACCPT_BAGS")%></td><td style="width:150px;" ><%=resultSet.getString("ACCPT_AVG_BAG_WT")%></td></tr>
<tr> <td style="width: 400px;" >Weight at Storage  </td><td style="width:50px;" > <%=resultSet.getString("STORAGE_WT")%></td><td style="width:150px;" ><%=resultSet.getString("STORAGE_BAGS")%></td><td style="width:150px;" ><%=resultSet.getString("STORAGE_AVG_BAG_WT")%></td></tr>
<tr> <td style="width: 400px;" > <b> Transit Loss [ B ] </b>  </td><td style="width:50px;" ><b> <%=resultSet.getString("TRANSIT_LOSS_WT")%> </b></td><td style="width:150px;" ><b><%=resultSet.getString("TRANSIT_LOSS_BAGS")%></b></td><td style="width:150px;" ><b><%=resultSet.getString("TRANSIT_LOSS_AVG_BAG_WT")%></b></td></tr>

<tr> <td style="width: 400px;" >  <b> Booked Depo Loss [ C ] </b>   </td><td style="width:50px;" ><b> <%=resultSet.getString("BOOKED_DEPO_LOSS_WT")%></b></td><td style="width:150px;" ><b><%=resultSet.getString("BOOKED_DEPO_LOSS_BAGS")%></b></td><td style="width:150px;" ><b><%=resultSet.getString("BOOKED_DEPO_AVG_BAGS_WT")%></b></td></tr>
<tr> <td style="width: 400px;" >  <b> Total Net Loss [ A+B+C ]   </td><td style="width:50px;" ><b> <%=resultSet.getString("TOTAL_NET_LOSS_WT")%></b></td><td style="width:150px;" ><b><%=resultSet.getString("TOTAL_NET_LOSS_BAGS")%></b></td><td style="width:150px;" ><b><%=resultSet.getString("TOTAL_NET_LOSS_AVG_BAG_WT")%></b></td></tr>


</table>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
<br><br>
<%
} 
}
%>
</form>

</body>
</html>