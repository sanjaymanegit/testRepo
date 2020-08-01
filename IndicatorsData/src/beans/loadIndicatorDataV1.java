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

import org.codehaus.jackson.map.ObjectMapper;
import java.io.*;

//import beans.*;



@Path("/LoadIndDataV1")
public class loadIndicatorDataV1 {

	@GET
    @Path("ping")
    public String getServerTime() {
        System.out.println("V1-RESTful WEB service Service 'LoadIndDataV1' is running .......");
        return "V1-received ping on "+new Date().toString();
    }	
	
			
	@POST
    @Path("load_batch_data")
	@Consumes({MediaType.APPLICATION_JSON})
    @Produces({MediaType.APPLICATION_JSON}) 
    public String getBatchAllData( BatchAllData msg) throws Exception{
		
		// Convert msg object ot JSON string 
		// open log file for append and append in file 
		String Input_Json_str=null;
		Input_Json_str="Data Loaded Successfully xxxxxxx !!";		
				
		 // Creating Object of ObjectMapper define in Jakson Api 
        ObjectMapper Obj = new ObjectMapper(); 
  
        try { 
  
            //get Oraganisation object as a json string 
            String jsonStr = Obj.writeValueAsString(msg); 
  
            // Displaying JSON String 
            System.out.println(" My JSON STRING is :"+jsonStr); 
            
            //append the log file 
            
            String fileName = "incomming_batches.txt"; 
            try { 
                 BufferedWriter out = new BufferedWriter(new FileWriter(fileName,true)); 
                 out.write(jsonStr+"\n"); 
                 out.close();
            } 
            catch (IOException e) { 
                System.out.println("Exception Occurred" + e); 
            } 
            
            
            
            
            
            
        	} 
             catch(Exception e){ System.out.println(e);}
        
        
		Class.forName("com.mysql.jdbc.Driver");  
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/indicators_db","root","31@dec2019");
		ResultSet resultSet = null;
		
		try{
	   		 Statement stmt=con.createStatement();
	   		 String sql = "DELETE FROM batch_dtls WHERE unique_batch_id ='"+msg.getBatchMstData().getBatchIdFromDevice()+"'";
	   		 stmt.executeUpdate(sql);
		   		
			}catch(Exception e){ System.out.println(e);}	
			
			try{
		   		 Statement stmt=con.createStatement();
		   		 String sql = "DELETE FROM batch_recipe_dtls WHERE unique_batch_id ='"+msg.getBatchMstData().getBatchIdFromDevice()+"'";
		   		 stmt.executeUpdate(sql);
			   		
				}catch(Exception e){ System.out.println(e);}
			
			try{
		   		 Statement stmt=con.createStatement();
		   		 String sql = "DELETE FROM batch_cycles_dtls WHERE unique_batch_id ='"+msg.getBatchMstData().getBatchIdFromDevice()+"'";
		   		 stmt.executeUpdate(sql);
			   		
				}catch(Exception e){ System.out.println(e);}
			
		
	    try{
    		 Statement stmt=con.createStatement();  
    		 String sql = "INSERT INTO batch_dtls (batch_id_from_device,vehicle_no,recipe_no,design_mix,cycle_size,cycle_size_type,work_order_id,device_id_str,unique_batch_id,batch_created_on)VALUES('"+msg.getBatchMstData().getBatchIdFromDevice()+"','"+msg.getBatchMstData().getVehicleNo()+"','"+msg.getBatchMstData().getRecipeNo()+"','"+msg.getBatchMstData().getDesignMix()+"','"+msg.getBatchMstData().getCycleSize()+"','"+msg.getBatchMstData().getCycleSizeType()+"','"+msg.getBatchMstData().getWorkOrderId()+"','"+msg.getBatchMstData().getDeviceId()+"','"+msg.getBatchMstData().getBatchIdFromDevice()+"',STR_TO_DATE('"+msg.getBatchMstData().getBatchDt()+"', '%Y-%m-%d %T'))";    		 
    		 stmt.executeUpdate(sql);
    			}catch(Exception e){ System.out.println(e);}
	
		try{
   		Statement stmt=con.createStatement();
   		String sql = "";
   		
   		for (int i=0; i < msg.recipeDataArr.size(); i++ )
		{
   		 sql = "INSERT INTO batch_recipe_dtls(recipe_no,col1_key,col1_value,batch_id_device,unique_batch_id)VALUES('"+msg.recipeDataArr.get(i).getRecipeNo()+"','"+msg.recipeDataArr.get(i).getCol1Key()+"','"+msg.recipeDataArr.get(i).getCol1Value()+"','"+msg.recipeDataArr.get(i).getBatchIdFromDevice()+"','"+msg.recipeDataArr.get(i).getBatchIdFromDevice()+"')"; 
   		 stmt.executeUpdate(sql);
   		 System.out.println("Inserterd record in batch_recipe_dtls for index i:"+i);
		}
   		 }catch(Exception e){ System.out.println(e);}		
		
		try{
	   		Statement stmt=con.createStatement();
	   		String sql = "";
	   		String SQL_DEL = "";
	   		String sql_upd = "";
	   		for (int i=0; i < msg.batchCyclesArr.size(); i++ )
			{
	   		 
	   		  SQL_DEL= "DELETE FROM batch_cycles_dtls WHERE unique_batch_id ='"+msg.batchCyclesArr.get(i).getBatchIdFromDevice()+"' and cycle_id_device='"+msg.batchCyclesArr.get(i).getCycleId()+"'";	
	   		 
	   		 stmt.executeUpdate(SQL_DEL);
	   		 sql = "INSERT INTO batch_cycles_dtls(batch_id_device,col1_value,col2_value,col3_value,col4_value,col5_value,col6_value,col7_value,col8_value,col9_value,col10_value,recipe_no,cycle_time,cycle_id_device,unique_batch_id)VALUES('"+msg.batchCyclesArr.get(i).getBatchIdFromDevice()+"','"+msg.batchCyclesArr.get(i).getCol1Value()+"','"+msg.batchCyclesArr.get(i).getCol2Value()+"','"+msg.batchCyclesArr.get(i).getCol3Value()+"','"+msg.batchCyclesArr.get(i).getCol4Value()+"','"+msg.batchCyclesArr.get(i).getCol5Value()+"','"+msg.batchCyclesArr.get(i).getCol6Value()+"','"+msg.batchCyclesArr.get(i).getCol7Value()+"','"+msg.batchCyclesArr.get(i).getCol8Value()+"','"+msg.batchCyclesArr.get(i).getCol9Value()+"','"+msg.batchCyclesArr.get(i).getCol10Value()+"','"+msg.batchCyclesArr.get(i).getRecipeNo()+"','"+msg.batchCyclesArr.get(i).getCycleTime()+"','"+msg.batchCyclesArr.get(i).getCycleId()+"','"+msg.batchCyclesArr.get(i).getBatchIdFromDevice()+"')"; 
	   		 stmt.executeUpdate(sql);	
	   		
	   		 sql_upd = "UPDATE batch_cycles_dtls a, batch_dtls b  SET a.batch_id = b.batch_id  WHERE a.batch_id_device =b. batch_id_from_device and a.unique_batch_id=b.unique_batch_id and b.unique_batch_id='"+msg.batchCyclesArr.get(i).getBatchIdFromDevice()+"'";
	   	    stmt.executeUpdate(sql_upd);
	   		 System.out.println("Inserterd record in batch_cycles_dtls for index i:"+i);
			}
	   		 
	   		 }catch(Exception e){ System.out.println(e);}
		
		
		try{
	   		Statement stmt=con.createStatement();	   		 
	   		String sql = "UPDATE batch_recipe_dtls a, batch_dtls b  SET a.batch_id = b.batch_id  WHERE a.batch_id_device =b. batch_id_from_device and a.unique_batch_id=b.unique_batch_id and b.unique_batch_id='"+msg.getBatchMstData().getBatchIdFromDevice()+"'";  
	   		stmt.executeUpdate(sql);
	   		 System.out.println("updated batch_recipe_dtls for batch_id");
	   		 }catch(Exception e){ System.out.println(e);}		
		
		 con.close();
		//return "Data Loaded Successfully !!";	
		return Input_Json_str;
    }
	
}
