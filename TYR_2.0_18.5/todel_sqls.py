select FLEXURAL_STRENGTH_KG_CM from CYCLES_MST where test_id=554

SELECT round(((3*PEAK_LOAD_KG*(SELECT NEW_TEST_MAX_LOAD*0.1 FROM GLOBAL_VAR))/(2*WIDTH*0.1*THINCKNESS*0.1*THINCKNESS*0.1)),2)  from CYCLES_MST where test_id=554;


SELECT ((3*PEAK_LOAD_KG*(SELECT NEW_TEST_MAX_LOAD*0.1 FROM GLOBAL_VAR))/(2*WIDTH*0.1*THINCKNESS*0.1*THINCKNESS*0.1))  from CYCLES_MST where test_id=554; 

SELECT ((3*PEAK_LOAD_KG*(SELECT NEW_TEST_MAX_LOAD*0.1 FROM GLOBAL_VAR))/(2*WIDTH*0.1*THINCKNESS*0.1*THINCKNESS*0.1))  from CYCLES_MST where test_id=554; 


SELECT (3*PEAK_LOAD_KG*(SELECT NEW_TEST_MAX_LOAD*0.1 FROM GLOBAL_VAR)) as top,(2*WIDTH*0.1*THINCKNESS*0.1*THINCKNESS*0.1) as bottom from CYCLES_MST where test_id=554;