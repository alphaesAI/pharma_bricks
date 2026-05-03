import org.apache.spark.sql.SparkSession
import io.delta.tables._

object TestDelta {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("DeltaTest")
      .master("local[*]") // Run on your laptop's CPU
      .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
      .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
      .getOrCreate()

    // Create a simple list of data
    import spark.implicits._
    val data = Seq((1, "Claims_Alpha"), (2, "Claims_Beta")).toDF("id", "name")

    // Try to write it as a Delta Table locally
    println("Writing Delta table to ./delta-table...")
    data.write.format("delta").mode("overwrite").save("./delta-table")
    
    println("Success! Reading it back:")
    spark.read.format("delta").load("./delta-table").show()

    spark.stop()
  }
}