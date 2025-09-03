from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

with DAG(
    dag_id = "shopee_etl",
    schedule="@daily", 
    start_date=pendulum.datetime(2025, 9, 2, tz = "UTC"),
    catchup=False,
    tags = ["data_eng", "shopee", "databricks", "etl"],
) as dag:
    
    new_cluster_config = {
        "spark_version" : "xx",
        "node_type_id" : "Standard_D4ds_v5", 
        "num_workers" : 2,
    }
    
    notebook_job_config = {
        "notebook_task" : {
            "notebook_path" : "/Workspace/Users/thepilotrock07@gmail.com/Spark-Shopee"
        },
        "new_cluster" : new_cluster_config
    }
    
    run_job = DatabricksSubmitRunOperator(
        task_id = "job_etl_shopee", 
        json = notebook_job_config, 
        databricks_conn_id= "shopee_databricks"
    )