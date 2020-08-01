package beans;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;


import java.sql.*;  

 
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;



//import beans.*;



@Path("/LoadIndData")
public class loadIndicatorData {

	@GET
    @Path("ping")
    public String getServerTime() {
        System.out.println("RESTful WEB service Service 'loadIndicatorDataWS' is running .......");
        return "received ping on "+new Date().toString();
    }	
	
			
	@POST
    @Path("load_batch_data")
	@Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.APPLICATION_JSON}) 
    public String getBatchAllData( BatchAllData msg) throws Exception{   
		
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019");
		ResultSet resultSet = null;
		String DEV_ID_UPD = null;
		
		try{
   		 Statement stmt=con.createStatement();
   		 String sql = "SELECT DATE_FORMAT(NOW(), '%Y%m%d%T') as DEVICE_ID_FOR_UPD;";    		 
   		 resultSet =stmt.executeQuery(sql);
	   		while(resultSet.next())
	   		{
	   			DEV_ID_UPD = msg.getBatchMstData().getDeviceId()+"_"+resultSet.getString("DEVICE_ID_FOR_UPD");	
	   		}
   		
		}catch(Exception e){ System.out.println(e);}
		
	    try{
    		 Statement stmt=con.createStatement();  
    		 String sql = "INSERT INTO batch_dtls (batch_id_from_device,vehicle_no,recipe_no,design_mix,cycle_size,cycle_size_type,work_order_id,device_id_str,unique_batch_id,batch_created_on)VALUES('"+msg.getBatchMstData().getBatchIdFromDevice()+"','"+msg.getBatchMstData().getVehicleNo()+"','"+msg.getBatchMstData().getRecipeNo()+"','"+msg.getBatchMstData().getDesignMix()+"','"+msg.getBatchMstData().getCycleSize()+"','"+msg.getBatchMstData().getCycleSizeType()+"','"+msg.getBatchMstData().getWorkOrderId()+"','"+msg.getBatchMstData().getDeviceId()+"','"+DEV_ID_UPD+"',STR_TO_DATE('"+msg.getBatchMstData().getBatchDt()+"', '%Y-%m-%d %T'))";    		 
    		 stmt.executeUpdate(sql);
    			}catch(Exception e){ System.out.println(e);}
	
		try{
   		Statement stmt=con.createStatement();
   		String sql = "";
   		for (int i=0; i < msg.recipeDataArr.size(); i++ )
		{
   		 sql = "INSERT INTO batch_recipe_dtls(recipe_no,col1_key,col1_value,batch_id_device,unique_batch_id)VALUES('"+msg.recipeDataArr.get(i).getRecipeNo()+"','"+msg.recipeDataArr.get(i).getCol1Key()+"','"+msg.recipeDataArr.get(i).getCol1Value()+"','"+msg.recipeDataArr.get(i).getBatchIdFromDevice()+"','"+DEV_ID_UPD+"')"; 
   		 stmt.executeUpdate(sql);
   		 System.out.println("Inserterd record in batch_recipe_dtls for index i:"+i);
		}
   		 }catch(Exception e){ System.out.println(e);}		
		
		try{
	   		Statement stmt=con.createStatement();
	   		String sql = "";
	   		for (int i=0; i < msg.batchCyclesArr.size(); i++ )
			{
	   		 sql = "INSERT INTO batch_cycles_dtls(batch_id_device,col1_value,col2_value,col3_value,col4_value,col5_value,col6_value,col7_value,col8_value,col9_value,col10_value,recipe_no,cycle_time,cycle_id_device,unique_batch_id)VALUES('"+msg.batchCyclesArr.get(i).getBatchIdFromDevice()+"','"+msg.batchCyclesArr.get(i).getCol1Value()+"','"+msg.batchCyclesArr.get(i).getCol2Value()+"','"+msg.batchCyclesArr.get(i).getCol3Value()+"','"+msg.batchCyclesArr.get(i).getCol4Value()+"','"+msg.batchCyclesArr.get(i).getCol5Value()+"','"+msg.batchCyclesArr.get(i).getCol6Value()+"','"+msg.batchCyclesArr.get(i).getCol7Value()+"','"+msg.batchCyclesArr.get(i).getCol8Value()+"','"+msg.batchCyclesArr.get(i).getCol9Value()+"','"+msg.batchCyclesArr.get(i).getCol10Value()+"','"+msg.batchCyclesArr.get(i).getRecipeNo()+"','"+msg.batchCyclesArr.get(i).getCycleTime()+"','"+msg.batchCyclesArr.get(i).getCycleId()+"','"+DEV_ID_UPD+"')"; 
	   		 stmt.executeUpdate(sql);	   		
	   		 System.out.println("Inserterd record in batch_cycles_dtls for index i:"+i);
			}
	   		 
	   		 }catch(Exception e){ System.out.println(e);}
		
		
		try{
	   		Statement stmt=con.createStatement();	   		 
	   		String sql = "UPDATE batch_recipe_dtls a, batch_dtls b  SET a.batch_id = b.batch_id  WHERE a.batch_id_device =b. batch_id_from_device and a.unique_batch_id=b.unique_batch_id and b.unique_batch_id='"+DEV_ID_UPD+"'";  
	   		stmt.executeUpdate(sql);
	   		 System.out.println("updated batch_recipe_dtls for batch_id");
	   		 }catch(Exception e){ System.out.println(e);}
		
		
		try{
	   		Statement stmt=con.createStatement();
	   		String sql = "UPDATE batch_cycles_dtls a, batch_dtls b  SET a.batch_id = b.batch_id  WHERE a.batch_id_device =b. batch_id_from_device and a.unique_batch_id=b.unique_batch_id and b.unique_batch_id='"+DEV_ID_UPD+"'"; 
	   		 stmt.executeUpdate(sql);
	   		System.out.println("updated batch_cycles_dtls for batch_id");
	   		 }catch(Exception e){ System.out.println(e);}
		
		 con.close();
		return "Data Loaded Successfully !!";
    }
	
}
