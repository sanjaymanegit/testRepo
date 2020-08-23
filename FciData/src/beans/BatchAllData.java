package beans;

import java.util.List;
import java.util.ArrayList;

//import bean.*;

public class BatchAllData {
	
	private BatchMstData BatchMstData;
	private RecipeData RecipeData;
	private BatchCyclesData BatchCyclesData;
	
	
	 List<RecipeData> recipeDataArr = new ArrayList<>();
	 
	 List<BatchCyclesData> batchCyclesArr = new ArrayList<>();

	 public BatchMstData getBatchMstData() {
	        return BatchMstData;
	    }
	 
	 public void setBatchMstData(BatchMstData BatchMstData ) {
		 this.BatchMstData =BatchMstData;
	    }
	 
	 public  List<RecipeData> getRecipeDataArr() {
	        return recipeDataArr;
	    }
	 
	 public  List<BatchCyclesData> getBatchCyclesArr() {
	        return batchCyclesArr;
	    }
	 
	 
	//private RecipeData RecipeDataf;
		//private BatchCycles BatchCyclesf;
		
		
		///private List<RecipeData> RecipeData;
		
		//private List<BatchCyclesData> BatchCycles; 
}
